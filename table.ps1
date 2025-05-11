# Get the current script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Set file paths relative to the script location
$csvPath = Join-Path $scriptDir "test.csv"
$outputHtml = Join-Path $scriptDir "test.html"

# Load the System.Web assembly for HTML encoding
Add-Type -AssemblyName System.Web

# Read the CSV
$data = Import-Csv -Path $csvPath

# Begin HTML
$html = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>People Table</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css" rel="stylesheet">
</head>
<body>
<div class="container mt-5">
    <h2 class="mb-4">Mock People Dataset</h2>
    <table id="peopleTable" class="table table-striped table-bordered" style="width:100%">
        <thead>
            <tr>
"@

# Add table headers
$data[0].PSObject.Properties.Name | ForEach-Object {
    $html += "                <th>$_</th>`n"
}

$html += @"
            </tr>
        </thead>
        <tbody>
"@

# Add table rows with proper HTML encoding
foreach ($row in $data) {
    $html += "            <tr>`n"
    foreach ($value in $row.PSObject.Properties.Value) {
        $escaped = [System.Web.HttpUtility]::HtmlEncode($value)
        $html += "                <td>$escaped</td>`n"
    }
    $html += "            </tr>`n"
}

$html += @"
        </tbody>
    </table>
</div>

<!-- Scripts -->
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/dataTables.bootstrap5.min.js"></script>
"@

# DataTables init with default config
$html += @'
<script>
    $(document).ready(function () {
        $("#peopleTable").DataTable();
    });
</script>
</body>
</html>
'@

# Output the HTML file
$html | Out-File -Encoding UTF8 -FilePath $outputHtml

Write-Host "HTML Table created at $outputHtml"