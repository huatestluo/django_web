
from django.http import HttpResponse,JsonResponse

from meal.models import Tsukiko

from getdate.xinshipu import cookbook,zuofa
from django.core import serializers
import json
from django.forms.models import model_to_dict


def add_db(request):
    number = cookbook()[0]
    url = cookbook()[1]
    zuofa_1 = zuofa()
    for i in range(0,len(zuofa_1)):
        add = Tsukiko(name='%s'%number[i],practice='%s'%zuofa_1[i],url='https://www.xinshipu.com/zuofa%s'%url[i])
        add.save()
    return  HttpResponse('月子餐食谱添加到数据库成功!快去看看吧！')

def select_db(request,id):
    name = Tsukiko.objects.get(id='%s'%id).name
    practice = Tsukiko.objects.get(id='%s'%id).practice
    url = Tsukiko.objects.get(id='%s'%id).url
    return name,practice,url

def select_all(request):
    # name=''
    # practice = ''
    # url = ''
    # ret = Tsukiko.objects.all()
    #
    # for i in ret:
    #     name += ','+i.name
    #     practice += ','+i.practice
    #     url += ',' +i.url
    # return HttpResponse('''<p>查询菜名结果:%s</p>
    #                         <p>查询做法结果:%s</p>
    #                         <p>查询链接结果:%s</p>
    #                         '''%(name,practice,url))

    ret = Tsukiko.objects.all()
    json_list = []
    for i in ret:
        json_dict = model_to_dict(i)
        json_list.append(json_dict)
    return JsonResponse(json_list,safe=False,json_dumps_params={'ensure_ascii':False})
