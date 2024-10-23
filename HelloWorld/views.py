import os

from django.http import HttpResponse,HttpResponseNotFound,JsonResponse,StreamingHttpResponse,FileResponse
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView

from HelloWorld.models import StudentInfo


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


def to_login(request):
    """
    跳转登录页面
    :param request:
    :return:
    """
    return render(request,"login.html")


def login(request):
    """
    跳转
    :param request:
    :return:
    """
    user_name=request.POST.get("user_name")
    pwd=request.POST.get("pwd")
    if user_name=="123" and pwd=="123456":
        request.session['currentUserName']=user_name    #session中存一个用户名
        print("session获取",request.session['currentUserName'])
        response=render(request,"main.html")
        response.set_cookie("remember_me",True) #设置cookie
        return response
    else:
        context_value={"error_info":"用户名或密码错误"}
        return render(request,"login.html",context=context_value)



def to_upload(request):
    """
    跳转文件上传页面
    :param request:
    :return:
    """
    return render(request,"upload.html")

def upload(request):
    """
    文件上传处理
    :param request:
    :return:
    """
    #获取上传的文件，如果没有文件，则默认返回None
    myfile=request.FILES.get("myfile",None)
    if myfile:
        #打开特定的文件，进行二进制写操作
        f=open(os.path.join("D:\\myfile",myfile.name),"wb+")
        #分块写入
        for chunk in myfile.chunks():
            f.write(chunk)
        f.close()

        return HttpResponse("文件上传成功")
    else:
        return HttpResponse("没发现文件")



class List(ListView):
    #设置模板文件
    template_name='student/list.html'
    #设置模型外的数据
    extra_context={'title':'学生信息列表'}
    #定义结果集
    queryset=StudentInfo.objects.all()
    #每页展示5条数据
    paginate_by = 5
    #设置上下文对象名称
    context_object_name = 'student_list'

class Detail(DetailView):
    #设置模板文件
    template_name = 'student/detail.html'
    #设置模型外的数据
    extra_context={'title':'学生信息详情'}
    #设置查询模型
    model=StudentInfo
    #设置上下文对象名称
    context_object_name='student'
