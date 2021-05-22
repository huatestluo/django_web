from django.shortcuts import render
import random
# Create your views here.
from django.http import HttpResponse
from mainapp import getdb

def index(request):
    return HttpResponse("五一，go start django")

def huahua(request):
    return HttpResponse("华华，好好学习")

def demo(request):
    meal_random = "<a href='/meal_random' style='text-decoration:none;'>点击这里随机选餐咯</a>"
    return render(request,'demo.html',{"meal_random":meal_random})

def meal_random(request):
    data = getdb.select_db(request,random_id())
    meal_name = data[0]
    zuofa = data[1].replace("['","").replace("']","").split("', '")
    url = "<a href='%s' target='_blank' style='text-decoration:none;'>点击跳转原文链接</a>"%data[2]
    demo = "<a href='/' style='text-decoration:none;'>返回demo页签重新选择</a>"
    return render(request,'meal_random.html',{"meal_name":meal_name,
                                              "zuofa":zuofa,
                                              "url":url,
                                              "demo":demo})

def random_id():
    random_id = random.randint(0,126)
    return random_id