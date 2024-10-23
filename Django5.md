Django5

## 创建项目

### 创建方法

+ cmd—**django-admin startproject** python222_site
+ pycharm

### 文件介绍

+ manage.py

```
项目管理命令行工具，内置多种方式与项目进行交互，包括启动项目，创建app,数据管理等。在命令提示符窗口下，将路径切换到项目并输入python manage.py help，可以查看该工具的指令信息;
```

<img src="../AppData/Roaming/Typora/typora-user-images/image-20241018162223490.png" alt="image-20241018162223490" style="zoom:25%;" />

+ \_\_init\_\_.py：初始化文件，一般不需修改
+ settings.py

```
项目的配置文件，项目的所有功能都需要在该文件中进行配置;
```

+ urls.py:项目的路由设置，设置网站的具体网址内容;
+ wsgi.py

```
全称为Python Web Server Gateway Interface，即Python服务器网关接口，是Python应用与Web服务器之间的接口，用于Django项目在服务器上的部署和上线;【不用修改】
```

+ asgi.py

```
开启一个ASGI服务，ASGI是异步网关协议接口;【不用修改】
```



## Django操作命令

```
在项目下——terminal——输入python代码
Tool——Run manage.py task ctrl+alt+r
```

## Django应用创建

```
startapp app01
注册应用到项目的settings.py中
创建网页代码
编写视图处理层请求代码
编写请求映射函数配置
开启服务 runserver
```

<img src="../AppData/Roaming/Typora/typora-user-images/image-20241018162345903.png" alt="image-20241018162345903" style="zoom:33%;" />

> 应用的结构如下

<img src="../AppData/Roaming/Typora/typora-user-images/image-20241018161445281.png" alt="image-20241018161445281" style="zoom:25%;" />

+ admin.py:默认提供了admin后台管理，用作网站的后台管理站点配置相关
+ apps.py : 应用配置文件。
+ models.py:用于应用操作数据库的模型
+ `tests.py :做单元测试。
+ views.py:用于编写Web应用视图，接收数据，处理数据，与Model(模型)，Template(模版)进行交互，返回应答
+ \-\-init\-\-.py：说明目录是一个python模块
+ migrations.py目录:用于存放数据库迁移历史文件



## Settings.py文件

### 基本配置

```
Django的配置文件settings,py用于配置整个网站的环境和功能，核心配置必须有
1、项目路径
2、密钥配置
3、域名访问权限
4、App列表
5、中间件
6、资源文件
7、模板配置
8、数据库的连接方式。
```

```python
#项目路径
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

#秘钥配置
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bew6iza5+zyi4e!b3crpay=j_)&_qz2sx^k$$8i(5kkze^cf7#'

#调试模式
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#域名访问权限
ALLOWED_HOSTS = []


# Application definition
#app列表
INSTALLED_APPS = [
    'django.contrib.admin', #后台管理
    'django.contrib.auth',  #用户认证
    'django.contrib.contenttypes',  #记录项目中的model元数据
    'django.contrib.sessions',  #表示用户身份，记录信息
    'django.contrib.messages',  #消息提示功能
    'django.contrib.staticfiles',   #寻找静态资源路径
    'HelloWorld.apps.HelloworldConfig',
]
```

### 资源文件配置

#### 静态资源配置

```
#静态资源配置：只能访问应用下面的static文件夹
STATIC_URL = 'static/'
```

```
#设置静态资源文件集合
STATICFILES_DIRS =[BASE_DIR /"static",BASE_DIR /"HelloWorld/images"]
```

+ 静态资源部署配置-STATIC_ROOT
  静态资源配置还有STATIC_ROOT，其作用是在服务器上部署项目，实现服务器和项目之间的映射。STATIC_ROOT主要收集整个项目的静态资源并存放在一个新的文件夹，然后由该文件夹与服务器之间构建映射关系。STATIC_ROOT配置如下:

![image-20241018171751862](../AppData/Roaming/Typora/typora-user-images/image-20241018171751862.png)



#### 媒体资源配置

![image-20241018172133610](../AppData/Roaming/Typora/typora-user-images/image-20241018172133610.png)

#### 模板配置

项目模板与应用模板冲突时，根据dis的顺序来的

```
TEMPLATES = [
    {
        #定义模板引擎，用于识别模板里面的变量和指令。内置的模板引擎有D]angoTemplates和jinja2.jinja2，
        # 每个模板引擎都有自己的变显和指令语法。
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #设置模板所在路径，告诉Django在哪个地方查找模板的位置，默认为空列表。
        'DIRS':[BASE_DIR/'templates',BASE_DIR/'HelloWorld/templates'],
        #是否在App里查找模板文件
        'APP_DIRS': True,
        #用于填充在RequestContext的上下文(模板里面的变量和指令)，一般情况下不做任何修改。
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



#### 数据库配置

> 支持的数据库

+ django.db.backends.postgresql
+ django.db.backends.mysql
+ django.db.backends.sqlite3
+ django.db.backends.oracle

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_web_edu',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'localhost',
        'PORT':'3306'
    }
}
```



#### 中间件

```
中间件(Middleware)是一个用来处理Diango的请求(Request)和响应(Response)的框架级别的钩子.
它是一个轻量、低级别的插件系统，用于在全局范围内改变 Django的输入和输出。
当用户在网站中进行某个操作时，这个过程是用户向网站发送HTTP请求(Request)而网站会根据用户的操作返回相关的网页内容，这个过程称为响应处理(Response)。
从请求到响应的过程中，当Django接收到用户请求时，首先经过中间件处理请求信息，执行相关的处理，然后将处理结果返回给用户。
```

```
MIDDLEWARE = [
    #内置的安全机制，保护用户与网站的通信安全
    'django.middleware.security.SecurityMiddleware',
    #会话Session功能
    'django.contrib.sessions.middleware.SessionMiddleware',
    #处理请求信息，规范化请求内容
    'django.middleware.common.CommonMiddleware',
    #开启CSRE防护功能
    'django.middleware.csrf.CsrfViewMiddleware',
    #开启内置的用户认证系统
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #开启内置的信息提示功能
    'django.contrib.messages.middleware.MessageMiddleware',
    #防止恶意程序单击劫持
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

> 自定义中间件

![image-20241021141417544](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20241021141417544.png)



#### 其他配置

+ ROOT_URLCONF

  ```
  ROOT_URLCONF = 'djangoProject_1.urls'
  ```



## 路由定义与使用

```
URL:uniform resource locator
路由称为URL(Uniform Resource Locator，统一资源定位符)，也可以称为URLconf，是对可以从互联网上得到的资源位置和访问方法的一种简洁的表示，是互联网上标准资源的地址。互联网上的每个文件都有一个唯一的路由，用于指出网站文件的路径位置。简单地说，路由可视为我们常说的网址，每个网址代表不同的网页。
```

+ 视图函数
+ 可选变量
+ 路由命名

### 路由变量

```
在平时开发中，有时候一个路由可以代表多个不同的页面，比如博客系统里面，有1千个博客页面，按照前面学习的方式，需要写1千个路由才能实现，这种做法显然不可取，维护也麻烦。我们可以通过路由变量，来实现一个路由代表多个页面。
```

+ 变量类型
  + 字符类型：匹配任何非空字符串，但不含斜杠。如果没有指定类型，就默认使用该类型。
  + 整型：:匹配O和正整数
  + slug：可理解为注释、后缀或附属等概念，常作为路由的解释性字符。可匹配任何ASCIl字符以及连接符和下画线，能使路由更加清晰易懂。比如网页的标题是"15岁的孩子”，其路由地址可以设置为"15-sui-de-hai-zi"。
  + uuid：匹配一个uuid格式的对象。为了防止冲突，规定必须使用""并且所有字母必须小写，例如175194d3-6885-437e-a8a8-6c231e272f00。

```
path('blog2/<int:year>/<int:month>/<int:day>/<int:id>',HelloWorld.views.blog2),

def blog2(request,year,month,day,id):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day)+"id是"+str(id)+"的博客页面")
```

### 正则路由

```
re_path('blog3/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})',HelloWorld.views.blog3),
```

+ 正则urls匹配，必须用re_path方法
+ 正则表达式？P开头是固定格式



### 路由重定向

```
重定向称为HTTP协议重定向，也可以称为网页跳转，它对应的HTTP状态码为301、302、303、317、308。简单来说，网页重定向就是在浏览器访问某个网页的时候，这个网页不提供响应内容，而是自动跳转到其他网址，由其他网址来生成响应内容。
```

+ 路由重定向

```
使用Django内置的视图类RedirectlIew实现的，默认支持HTTP的GET请求
path( 'redirectTo',RedirectView.as_view(url="index/")),
```

+ 自定义视图重定向

```
是在自定义视图的响应状态设置重定向，能让开发者实现多方面的开发需求。
```

```
def blog(request,id):
    if id==0:
        return redirect("/static/error.html")
    else:
        return HttpResponse("id是"+str(id)+"的博客页面")
```



### 命名空间Namespace

```
path('user/',include(('user.urls','user'),namespace='user')),
path('order/',include(('order.urls','order'),namespace='order'))
```



### 路由命名与反向解析reverse与resolve

```
我们在urls.py里定义的路由信息，有时候需要动态获取路由信息，然后进行一些处理，统计，日志等操作，这时候我们需要在其他代码里用到路由信息，比如views.py，后面要学到的模型models.py，Admin系统等，因此我们引入路由反向解析reverse与resolve方法，再使用这两个方法前，我们还需要给路由取名，否则我们无法找到我们需要的那个路由的信息。
reverse方法根据路由名称得到路由地址。
resolve方法根据路由地址得到路由所有信息。
```

```
route_url=reverse('order:index')
print("reverse反向解析得到的路由地址:",route_url)
result=resolve(route_url)
print("resolve通过路由地址得到路由信息:",result)
```



![image-20241022140244211](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20241022140244211.png)



## 视图定义与使用

### 设置视图响应状态

```
客户端请求后端服务，在view.py视图层方法最终return返回视图响应。Python内置提供了响应类型，来实现不同的返回不同的http状态码;
```

![image-20241022144042575](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20241022144042575.png)

```
html="12345678999999999"
return HttpResponse(html)
```



render

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20241022145819051.png" alt="image-20241022145819051" style="zoom:50%;" />

+ request:浏览器向服务器发送的请求对象，包含用户信息、请求内容和请求方式等
+ template_name:设置模板文件名，用于生成网页内容。
+ context:对模板上下文（模板变量）赋值，以字典格式表示，默认情况下是一个空字典
+ content_type:响应内容的数据格式，一般情况下使用默认值即可。
+ status: HTTP状态码，默认为200.
+ using:设置模板引擎，用于解析模板文件，生成网页内容。



### 重定向响应

```
重定向的状态码分为301和302，前者是永久性跳转的，后者是临时跳转的，两者的区别在于搜索引擎的网页抓取。301重定向是永久的重定向，搜索引擎在抓取新内容的同时会将旧的网址替换为重定向之后的网址。302跳转是暂时的跳转，搜索引擎会抓取新内容而保留l旧的网址，因为服务器返回302代码，所以搜索引擎认为新的网址只是暂时的。
```

+ HttpResponseRedirect:302
+ HttpResponsePermanentRedirect:301



### 二进制文件下载响应

+ HttpResponse是所有响应过程的核心类，它的底层功能类是HttpResponseBase.
+ StreamingtittpResponse是在httpResponseBase的基础上进行继承与重写的，它实现流式响应输出（流式响应输出是使用Python的迭代器将数据进行分段处理并传输的)。适用于大规模数据响应和文件传输响应。
+ FileResponse是在StreamingHttpResponse的基础上进行继承与重写的，它实现文件的流式响应输出，只适用于文件传输响应.



### http请求&httprequest请求类

#### http请求

```
超文本传输协议(Hypertext Transfer Protocol，HTP)是一个简单的请求·响应协议，它通常运行在TCP之上。它指定了客户端可能发送给服务器什么样的消息以及得到什么样的响应。
当在浏览器上访问某个网址时，其实质是向网站发送一个HTTP请求，HTTP请求分为8种请求方式，每种请求方式的说明如下:
```

+ optional:返回服务器针对特定资源所支持的请求方法
+ **get:向特定资源发出请求(访问网页)**
  + GET请求的请求参数是在路由地址后添加“?”和参数内容，参数内容以key-value形式表示，等号前面的是参数名，后面的是参数值，如果涉及多个参数，每个参数之间就使用"&"隔开，如127.0.0.1:800b/?name=python222&pw=123456。
+ **post:向指定资源提交数据处理请求(提交表单、上传文件)**
  + POST请求的请求参数一般以表单的形式传递，常见的表单使用HTML的form标签，并且form标签的method属性设为POST.
+ put:向指定资源位置上传数据内容
+ delete:请求服务器删除request-URL所标示的资源
+ head:与GET请求类似，返回的响应中没有具体内容,用于获取报头
+ trace:回复和显示服务器收到的请求，用于测试和诊断
+ connect:HTTP/1.1协议中能够将连接改为管道方式的代理服务器

```
Diango5中,Http请求信思都被封装到了HttpRequest类中。
HttpReguest类的常用属性如下:
```

> 常用属性

+ cookie:获取客户端（浏览器）的Cookie信息，以字典形式表示，并且键值对都是字符串类型。
+ files:diango.http.request.QueryDict对象，包含所有的文件上传信息。
+ get:获取GET请求的请求参数，它是diango.http.request.QueryDict对象，操作起来类似于字典。
+ post:获取POST请求的请求参数，它是diango.http.request.QueryDict对象，操作起来类似于字典。
+ meta:获取客户端（浏览器）的请求头信息，以字典形式存储。
+ method:获取当前请求的请求方式(GET请求或POST请求).
+ path:获取当前请求的路由地址
+ session:一个类似于字典的对象，用来操作服务器的会话信息，可临时存放用户信息。
+ user:当Django启用AuthenticationMiddleware中间件时才可用。它的值是内置数据模型User的对象，表示当前登景的用户。如果用户当前没有登录，那么user将设为diango.contrib.auth.models.AnonymousUser的一个实例。

> 常用方法

+ is_secure():是否是采用HTTPS协议。
+ get_host():获取服务器的域名。如果在访问的时候设有端口，就会加上端口号，如127.0.0.1:8000.
+ get_full_path():返回路由地址。如果该请求为GET请求并且设有请求参数，返回路由地址就会将请求参数返回，如/?name=python2228pM=123456。



### 会话管理（Cookies&Session)

```
HTTP是一种无状态协议，每次客户端访问web页面时，客户端打开一个单独的浏览器窗口连接到web服务器，由于服务器不会自动保存之前客户端请求的相关倍息，所有无法识别一个HTTP请求是否为第一次访问。这就引进了web客户端和服务器端之间的会话，这就是会话管理。
```

+ #### Cookie:通过在客户端记录信息确定用户身份

  ```
  cookie是某些网站为了辨别用户身份，进行Session跟踪而储存在用户本地终端上的数据（通常经过加密)
  由用户客户端计算机暂时或永久保存的信息。
  Cookie定义了一些HTTP请求头和HTTP响应头，通过这些HTTP头信息使服务器可以与客户进行状态交互。
  客户端请求服务器后，如果服务器需要记录用户状态，服务器会在响应信息中包含一个Set-cookie的响应头，客户端会根据这个响应头存储Cookie信息。
  再次请求服务器时，客户端会在请求信息中包含一个Cookie请求头，而服务器会根据这个请求头进行用户身份、状态等较验
  ```

  <img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20241023101047962.png" alt="image-20241023101047962" style="zoom:67%;" />

+ #### Session:通过在服务器端记录信息确定用户身份

```
Session是另一种记录客户状态的机制，不同的是Cookie保存在客户端浏览器中，而Session保存在服务器上。
客户端浏览器访问服务器的时候，服务器把客户端信息以某种形式记录在服务器上。这就是Session。
客户端浏览器再次访问时只需要从该Session中查找该客户的状态就可以了。
当程序需要为某个客户端的请求创建一个session的时候，服务器首先检查这个客户端的请求里是否已包含了一个session标识，称为session id，如果已包含一个session id则说明以前已经为此客户端创建过session，服务器就按照session id把这个session检索出来使用(如果检索不到，可能会新建一个)，如果客户端请求不包含session id，则为此客户端创建一个session并且生成一个与此session相关联的session id ，session id的值应该是一个既不会重复，又不容易被找到规律以仿造的字符串，这个session id将被在本次响应中返回给客户端保存。
```

<img src="C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20241023101634689.png" alt="image-20241023101634689" style="zoom:60%;" />

#### session与cookie的区别

+ 数据存储位置: cookie数据存放在客户的浏览器上，session数据放在服务器上。
+ 安全性: cookie不是很安全，别人可以分析存放在本地的cookie并进行cookie欺骗，考虑到安全应当使用session。
+ 服务器性能: session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能，考虑到减轻服务器性能方面，应当使用cookie。
+ 数据大小:单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie。
+ 信息重要程度:可以考虑将用户信息等重要信息存放为session，其他信息如果需要保留，可以放在cookie中。



#### django实例



### 文件上传

![image-20241023135208985](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20241023135208985.png)



### 列表视图ListView

```
为了实现快速开发，Django提供了视图类功能，封装了视图开发常用的代码
这种基于类实现的响应与请求称为CBV(Class Base Views)
我们先介绍列表视图ListView
该视图类可以将数据库表的数据以列表的形式显示到页面，常用于数据的查询和展示。
首先为了得到数据库数据，我们先定义模型，来映射数据库表;
```

listview的属性

+ model：指定要使用的模型
+ template_name：指定要使用的模板名称
+ context_object_name：指定上下文变量名称，默认为object_list
+ paginate_by：指定分页大小
+ extra_context：设置模型外的数据



paginator常用属性与方法

+ count
+ num_pages
+ page_range

![image-20241023144411879](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20241023144411879.png)

page常用属性与方法

+ has_next
+ has_previous
+ next_page_number
+ previous_page_number
+ number
+ start_index
+ end_index



### 详细视图DetailView

![image-20241023145452601](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20241023145452601.png)



### 新增视图CreateView



































