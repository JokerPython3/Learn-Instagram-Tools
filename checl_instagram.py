#جزء ثاني من شرح برمجة اداة متاحات انستكرام
#راح اشرح تحميل نسخة انسته مكسوره ssl و تحميل reqable و وتحميل شهادته
#الي عنده pc يكدر يحمل ميمو محاكي
#تضغطون ضغط مطوله على download وبعدها download link
#نتي ضعيف يتاخر تحميل نسخة 
#الي عنده موبايل يبحث CA شهادة 
#ننتضر تحمل نسخة
#هذا اتصال يفحص ايميل اذا انطيته ايميل وينطيك ريست ايميل مربوط عليه حساب يعني يجيبلك ريست
import requests
def check_instagram(email):
    url = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"
   
    payload = {
    'signed_body': "85f26e5aa7d338e13be620d27c7f2ce83c7336455b307e66bfd876c04c17eb17.{\"_csrftoken\":\"Vm31NsssriEJByPhggSCkfyEQIM0DTfL\",\"adid\":\"7fc8e978-8950-4073-9986-96284e37108a\",\"guid\":\"3f19f183-0663-4238-8cbe-f18e3afb4021\",\"device_id\":\"android-a719ff17c7d1186c\",\"query\":\""+email+"\"}",
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

    print(response.text)
    #اذا بيه شسمه يعني غير متاح يعني ايميل مستخدم
    if "can_recover_with_code" in response.text:
        print(True)
    else:
        print(False)
check_instagram("atro@gmail.com")
#انتضرونا بي جزء ثالث
#by => s1 