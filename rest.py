import requests
def get_rest(username):
    if "@" in username:
        username=username.split("@")[0]
        #اذا بيه @ يشيله وياخذ الكلام او نص الذي قبله
    url = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
   
    payload = {
    'signed_body': "85f26e5aa7d338e13be620d27c7f2ce83c7336455b307e66bfd876c04c17eb17.{\"_csrftoken\":\"Vm31NsssriEJByPhggSCkfyEQIM0DTfL\",\"adid\":\"7fc8e978-8950-4073-9986-96284e37108a\",\"guid\":\"3f19f183-0663-4238-8cbe-f18e3afb4021\",\"device_id\":\"android-a719ff17c7d1186c\",\"query\":\""+username+"\"}",
    'ig_sig_key_version': "4"
    }

    headers = {
    'User-Agent': "Instagram 100.0.0.17.129 Android (28/9; 300dpi; 900x1600; Asus; ASUS_I005DA; ASUS_I005DA; intel; en_US; 161478664)",
    'Accept-Encoding': "gzip, deflate",
    'X-Pigeon-Session-Id': "6cb7e0fb-ed2b-45f1-a2f6-3c95f482cfa3",
    'X-Pigeon-Rawclienttime': "1754160756.716",
    'X-IG-Connection-Speed': "-1kbps",
    'X-IG-Bandwidth-Speed-KBPS': "-1.000",
    'X-IG-Bandwidth-TotalBytes-B': "0",
    'X-IG-Bandwidth-TotalTime-MS': "0",
    'X-Bloks-Version-Id': "009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0",
    'X-IG-Connection-Type': "WIFI",
    'X-IG-Capabilities': "3brTvw==",
    'X-IG-App-ID': "567067343352427",
    'Accept-Language': "en-US",
    'X-FB-HTTP-Engine': "Liger",
    'Cookie': "mid=aI5eagABAAHeEg1UJ1DjMfOXrNAH; csrftoken=Vm31NsssriEJByPhggSCkfyEQIM0DTfL"
    }

    response = requests.post(url, data=payload, headers=headers)

    try:
        return response.json()["email"]
    except:
        return "error"
    
print(get_rest("ntro"))
#تنطيه يوزر حساب حتى ينطيك ريست صحيح لاتطيه ايميل