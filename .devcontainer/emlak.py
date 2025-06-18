import requests

url = "https://www.hepsiemlak.com/api/realty-list/ankara-kiralik"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "tr",
    "referer": "https://www.hepsiemlak.com/",
    "sec-ch-ua": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-arch": "x86",
    "sec-ch-ua-bitness": "64",
    "sec-ch-ua-full-version": "137.0.7151.55",
    "sec-ch-ua-full-version-list": '"Google Chrome";v="137.0.7151.55", "Chromium";v="137.0.7151.55", "Not/A)Brand";v="24.0.0.0"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": '""',
    "sec-ch-ua-platform": '"Windows"',
    "sec-ch-ua-platform-version": '"15.0.0"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "cookies":"i18n_redirected=tr; _gcl_gs=2.1.k1$i1748170254$u121904786; _gcl_au=1.1.2065065628.1748170258; optimizelyEndUserId=oeu1748170258429r0.6323975939384798; _fbp=fb.1.1748170258706.592984501919930374; _tt_enable_cookie=1; _ttp=01JW3H2ECKDJ258YTXSW9XTB6E_.tt.1; _gcl_aw=GCL.1748170260.Cj0KCQjw_8rBBhCFARIsAJrc9yA-dP1CXVH0ou-0N_uo8S2stxYkkHpLydKax_7M4EEBxlwkvLITMtsaAk1xEALw_wcB; _ga=GA1.1.2113585620.1748170260; optimizelySession=0; ttcsid=1748197366624::jHlCI-cdsroMFu4Cldkx.2.1748197521191; ttcsid_C8UQB3FRAOSJ17FR7I80=1748197366623::j5Wgtj-DiRc9ehF-UEJx.2.1748197522701; device_info=%7B%22platform%22%3A%22desktop%22%2C%22os_type%22%3A%22windows%22%2C%22os_version%22%3A%2210.0%22%2C%22app_version%22%3A%225.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F137.0.0.0%20Safari%2F537.36%22%2C%22device_model%22%3A%22PC%22%2C%22device_brand%22%3A%22Windows%22%2C%22browser_type%22%3A%22chrome%22%2C%22user_agent%22%3A%22Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F137.0.0.0%20Safari%2F537.36%22%2C%22network%22%3A%224g%22%7D; unregistered_user_id=567a9bfb-5334-48cf-a543-70a2be9decf1; _dn_sid=932496df-3584-4cc4-a0e7-ee6d91216a00; _clck=1de5hjh%7C2%7Cfw9%7C0%7C1971; optimizelyStatus=true; xpid=dmFsdWUlM0QxNzQ4MTcwMjU4MTIwLTg4NC01MDgtdjEuNC44JTJDbHMlM0QxNzQ4Mzc4ODgwOTE4JTJDcnQlM0Qx; preventAsyncData=false; xsid=dmFsdWUlM0QxNzQ4Mzc4ODgwOTE1LTgwLTQ4Ni12MS40LjglMkNzcyUzRDElMkNydCUzRDE=; ShowUnlistedBanner=false; visited_city=6; visited_name=Ankara; visited_city_url=ankara; cto_bundle=r1OL_l80T0tybzdsSkU5QUlMOEU3N2dqVDNEbk5DdWlMJTJCaG9wZmVEOUdocmpQeVVwNHhjVEFTc0pnMlRBbXRVeWsxaiUyQkNYZFVja3ljd0l0N1NxdG9sYnV2dHdaY0R2c3VLQUZFUXRZeGoyMDFzYnpTdWZxUE1hektERlZlbTAyZlQxWTBOR0ZNUU9EZ3M4Yzh4UlZpMXM2S1ZjM0lmTVJoJTJCSHRkUjRRdHQ4U0g5bkphVmlpeFFuU281d3dTcCUyRm9LSW5LVzhqOFVCOWJBd0MwbGMzMiUyRnV1cGlNMjZpY1NaTUFBV09kMXhjWkdYWG9CZ21LVzYwOUtLVnVCakJDR1lreE9mVGFRakxNWDBrTWtjbmRHbFdYRER3eXdGVjNaTXVHd2t0V0VZNHp4bWQzQk9aVE81eWE5NWEzRTV2M053Snd5Skg; __gads=ID=aa21e9629ca051a4:T=1748170262:RT=1748379750:S=ALNI_MYKRmcO18VYjOWIFmsqTJZ5HkJW6g; __gpi=UID=000010ca6e47d7d1:T=1748170262:RT=1748379750:S=ALNI_MaX8cwtxtbZl-u1F9RiFoiuCfJGFg; __eoi=ID=50de0f2f9858779e:T=1748170262:RT=1748379750:S=AA-AfjakfzjjgM0n2bwVfPE-_UEz; new_vp=0; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22undefined%22%2C%22expiryDate%22%3A%222026-05-27T21%3A04%3A26.621Z%22%7D; _ga_1JXMT6R17H=GS2.1.s1748378880$o3$g1$t1748379866$j57$l0$h0$d3BA-aO-5C4e8CB9nh30z61xpTkJBtr7zBg; _uetsid=e09d2aa03b3b11f0908ad76a5d76d12f; _uetvid=e443cb4030db11f09b401d756b452dba; _clsk=18f92at%7C1748379869372%7C1%7C1%7Ca.clarity.ms%2Fcollect; __cf_bm=M5R5P_CAzEUWNYlAlF.YK80LgZch0Ho7neD4oYQuGuc-1748379959-1.0.1.1-zXhMGz63Rx8UytlC1Ua1CwemW6ygoPIn7vTvsN_U4e.LwAzONmw3GsvcrPNXUja3v7ApNhY4eUF90Cs4yPLvCaIXz4dXPX5yssbbqxzxwig; cf_clearance=2mfXsA0m5362baaRsM.z9nhH5sl2HdLmOXzLTPOAjuY-1748379965-1.2.1.1-Jrvnrq8ANknk9ZYFQGLodSQucgXDtF7gRDTAxyPg.ndoSPvw8uXWhvKdrKwjxA10R_O_tNEdesKKL6wUsIG__M1WAehjhQpXvelDByO7ISZKflp_M_R1KRGTvQrE.RgWvabUtTOccm9dj2uTMh6GO..cXHJ2CavTUkCBvMAyWFv20vKEdUh3nku4CrCmMB.DuJZpPbM_aKCCjfpPec4606_QcPI7rDLqMWYlS8OgY.VkWOMGNE5thomltF5iIufN.pktRVxwR1xH1.r3dUNkyFMzUmrwgR.W9Dr0rlzy1Gn1Hy98d6UTgVfXrbTbB0mhYDzWPGFdYKMvJVkIDtp5unDgwHw.XxpL9uQwCEy2stOcy0d4QyocbkYllUbKyHR8; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22o0dq7jfAgbO0AqKeV2u6%22%2C%22expiryDate%22%3A%222026-05-27T21%3A06%3A06.515Z%22%7D"
}



response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Hata: HTTP {response.status_code}")
    print(response.text)
