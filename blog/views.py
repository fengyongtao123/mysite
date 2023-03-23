from django.shortcuts import render,HttpResponse
from  app01 import models
# Create your views here.
def timer(request):
    import time
    cimer=time.ctime()
    return render(request,'timer.html',{"citme":cimer})



def special_case_2003(request):

    return HttpResponse('special_case_2003')


def arivch_year(request,year):
    return  HttpResponse(year)

def arivch_year_moth(request,m,y):
    return HttpResponse(y+"-"+m)

def  login(request):

    if request.method=="GET":

        return  render(request,'login.html')
    else:

        user=request.POST.get('user')
        password=request.POST.get('pwd')


        if user=='fyt' and password=='123':
            return HttpResponse("login success")
        else:
            return HttpResponse("登录失败")

def path_year(request,year):
    return  HttpResponse('path_year')

def path_month(request,month):
    return  HttpResponse(month)


def index(request):
    if request.method=="GET":
        i=10

        return render(request,'index.html',locals())
    #locals()将本地变量以字典的形式全部传过去
    else:
        ne=request.POST.get('name')
        age1=request.POST.get('age')
        if ne=='fyt' and age1=='19':
            return HttpResponse('提交成功')
        else:
            return HttpResponse(request.get_full_path())

# def base(request):
#     return  render(request,"base.html")


def db(request):
    #添加表记录
    #方式一
    # book_obj=models.Book_stu(id=1,title="python",price=100,pub_data="2022-10-13",publish="人名出版社")
    # book_obj.save()
    #方式二
    # book_obj=models.Book_stu.objects.create(title="php",price=200,pub_data="2022-10-13",publish="人名出版社")
    # print(book_obj)
    # return HttpResponse('ok')

    #查询表记录
   #all()返回的是queryset对象
   # book_list=models.Book_stu.objects.all()
   # print(book_list)
   # print(book_list[1].title)
   # print(models.Book_stu.objects.all().first())
   # print(models.Book_stu.objects.all().last())
   # print(models.Book_stu.objects.filter(price=200).first())
   # print(models.Book_stu.objects.all())
   print(models.Book_stu.objects.filter(price__lt=100))
   return HttpResponse('ok')