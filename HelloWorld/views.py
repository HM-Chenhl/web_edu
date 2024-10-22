from django.http import HttpResponse,HttpResponseNotFound,JsonResponse,StreamingHttpResponse,FileResponse
from django.shortcuts import render,redirect


# Create your views here.
def index(request):
    return render(request,'http.html')
    # return redirect('/blog/2',permanent=True)
    # return redirect('/static/new.html',permanent=True)

    # return JsonResponse({'hello':'world'})

    # return HttpResponseNotFound()
    # html="12345678999999999"
    # return HttpResponse(html)

    #print("页面请求处理中")
    # content_value={'msg':"hell0123"}
    # return render(request,'index.html',context=content_value)

def blog(request,id):
    if id==0:
        return redirect("/static/error.html")
    else:
        return HttpResponse("id是"+str(id)+"的博客页面")

def blog2(request,year,month,day,id):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day)+"id是"+str(id)+"的博客页面")

def blog3(request,year,month,day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day)+"的博客页面")


#定义文件路径
file_path='D:\\gui.exe'

def down_file_1(request):
    file=open(file_path,'rb')   #打开文件
    response = HttpResponse(file)#创建HttpResponse对象
    response['Content_Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename=file1.exe'
    return response

def down_file_2(request):
    file=open(file_path,'rb')   #打开文件
    response = StreamingHttpResponse(file)#创建StreamingHttpResponse对象
    response['Content_Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename=file1.exe'
    return response

def down_file_3(request):
    file=open(file_path,'rb')   #打开文件
    response = FileResponse(file)#创建FileResponse对象
    response['Content_Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename=file1.exe'
    return response

def get_test(request):
    """
    get请求测试
    :param request:
    :return:
    """
    # print(request.method)   #请求方式/GET
    # #常用属性
    # print(request.content_type)#text/plain
    # print(request.content_params)#{}
    # print(request.COOKIES)  #{}
    # print(request.scheme)   #http
    # #常用方法
    # print(request.is_secure())  #False
    # print(request.get_host())   #127.0.0.1:8000
    # print(request.get_full_path())  #/get?name=123&pas=123456

    print(request.GET.get('name'))
    print(request.GET.get('pas'))
    print(request.GET.get('aaa','没获取到'))
    return HttpResponse('http get ok')


def post_test(request):
    """
    post请求测试
    :param request:
    :return:
    """
    print(request.method)   #请求方式/GET
    # #常用属性
    # print(request.content_type)#text/plain
    # print(request.content_params)#{}
    # print(request.COOKIES)  #{}
    # print(request.scheme)   #http
    # #常用方法
    # print(request.is_secure())  #False
    # print(request.get_host())   #127.0.0.1:8000
    # print(request.get_full_path())  #/get?name=123&pas=123456

    print(request.POST.get('name'))
    print(request.POST.get('pas'))
    print(request.POST.get('aaa','没获取到'))
    return HttpResponse('http post ok')


