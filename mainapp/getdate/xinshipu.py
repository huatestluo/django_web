import requests
import re

host = 'https://www.xinshipu.com'
url_name = host + '/chishenme/114072/'
header = {'Content-Type':'application/json'}
body = {'':''}

def cookbook():
    shipu_name = []
    zuofa_id = []
    for i in range(1,7):
        url_numbers = url_name + '?page=%s'%i
        print(url_numbers)
        r = requests.post(url_numbers, json=body, headers=header, verify=False)
        text = r.content.decode('utf-8')
        shipu_name_01 = re.findall('alt="(.*?)" class=', text)
        zuofa_id_01 = re.findall('<a href="/zuofa(.*?)"', text)
        for name in shipu_name_01:
            shipu_name.append(name)
        for id in zuofa_id_01:
            zuofa_id.append(id)
    return  shipu_name,zuofa_id
# url = cookbook()[1]
def zuofa():
    url = cookbook()[1]
    zuofa_01 = []
    for i in url:
        zuofa_url = host + '/zuofa' + i
        r = requests.post(zuofa_url, json=body, headers=header, verify=False)
        text_zuofa = r.content.decode('utf-8')
        zuofa_cailiao = re.findall('<p>(.*?)</p>', text_zuofa)
        zuofa_01.append(zuofa_cailiao)
        print(zuofa_url)
    return zuofa_01

# number = cookbook()[0]
# zuofa_1 = zuofa()
# for i in range(len(number)):
#     print(number[i])
#     print(zuofa_1[i])

