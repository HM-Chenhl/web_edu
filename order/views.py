from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse,resolve


# Create your views here.

def index(request):
    route_url=reverse('order:index')
    print("reverse反向解析得到的路由地址:",route_url)
    result=resolve(route_url)
    print("resolve通过路由地址得到路由信息:",result)
    return HttpResponse("订单信息")

def list(request,year,month,day):
    #kwargs={'year':2023,'month':11,'day':10}
    args=[year,month,day]
    route_url=reverse('order:list',args=args)
    print("reverse反向解析得到的路由地址:",route_url)
    result=resolve(route_url)
    print("resolve通过路由地址得到路由信息:",result)
    return HttpResponse("订单列表")