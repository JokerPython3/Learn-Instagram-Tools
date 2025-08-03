#جزء رابع من شرح برمجة اداة متااحات انستكرام
#راح اسحب اخر اتصال هو اتصال معلومات
#تبحثون عن هذا رابط
#https://www.instagram.com/jelif71926/?__a=1
#وتفعلون  ادوات مطور
#تبحثون عن اتصال web_profile_info

import requests
def get_info(username):
    if "@" in username:username=username.split("@")[0]
    #اذا بيه @ شيل ال @ واخذ نص الي قبله
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.6',
        'priority': 'u=1, i',
        'referer': 'https://www.instagram.com/{}/?__a=1'.format(username),
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Brave";v="138"',
        'sec-ch-ua-full-version-list': '"Not)A;Brand";v="8.0.0.0", "Chromium";v="138.0.0.0", "Brave";v="138.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        'x-asbd-id': '359341',
        'x-csrftoken': 'kj0osUm9Cc2q2dmLQk3CcSRpOxMLAgIE',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-requested-with': 'XMLHttpRequest',
        'x-web-session-id': 'lyi8ng:oe0boo:ghq549',
    
    }

    params = {
        'username': username, 
    }

    response = requests.get(
        'https://www.instagram.com/api/v1/users/web_profile_info/',
        params=params,
        
        headers=headers,
    )
    try:
        data=response.json()['data']['user']
        bio = data['biography']
        followers=data['edge_followed_by']['count']
        following = data['edge_follow']['count']
        name = data['full_name']
        bussinec = data['is_business_account']
        id=data['id']
        praivet=data['is_private']
        verf=data['is_verified']
        photo =data['profile_pic_url']
        post =data['edge_owner_to_timeline_media']['count']
        #تكدرون تطلعون اي معلومة من response انا راح اكتفي بي معلومات اساسيه
        message=f"""
    --------[HIT]--------
    username : {params['username']}
    bio : {bio}
    followes : {followers}
    following : {following}
    name : {name}
    is_business_account : {bussinec}
    id : {id}
    praivet : {praivet}
    verif : {verf}
    photo link : {photo}
    post : {post}

        """
        print(message)
    except:
      
        message=f"""
    --------[HIT]--------
    username : {params['username']}
        """
        print(message)
get_info("atro")
#انتضرونا بي شرح اخير هو شرح تجميع اتصالات بي اداة واحده
#by => s1