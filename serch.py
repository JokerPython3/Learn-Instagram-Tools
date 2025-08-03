#10000 // 2011
#21254029834 // 2023
#جزء ثالث من شرح برمجة اداة متاحات انسته جيميل
#راح اشرح سحب اتصال توليد يورزرات من ايدي
#تحتاجون حساب انسته وهمي  حتى تسحبون اتصال 
#اذا انته بل موبايل شغل ادوات مطور بي متصفح كيوي
#تبحثون عن اتصال query

import requests,random
def generate_username():
    response = requests.post('https://www.instagram.com/graphql/query').cookies.get_dict()
    csrftoken=response['csrftoken']

    headers = {
        
        'content-type': 'application/x-www-form-urlencoded',
    
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
        
        'x-csrftoken': csrftoken,
    
    
    }

    data = {
    
        'lsd':csrftoken,
    
        
        'variables': '{"id":'+str(random.randint(10000,21254029834))+',"render_surface":"PROFILE"}', #تعرفون اتصال صح من هذا اذا بيه id و بيه render_surface
    
        'doc_id': '24059491867034637',
    }
    #هذا يولد ايديات من 2011 الى 2023 
    response = requests.post('https://www.instagram.com/graphql/query', headers=headers, data=data)
    try:
        user = response.json()['data']['user']['username']
        print(user)
    except:
        pass
generate_username()
#نتضرونا بي جزء رابع
#by => s1