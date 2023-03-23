from django.shortcuts import render,HttpResponse
from app01 import models
import json
from django.core.paginator import   Paginator
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


def ajx(request):


    return render(request,'ajx.html')


def test_ajx(request):

    print(request.GET)
    return HttpResponse('ok')

def cal(request):


    a=int(request.POST.get('a'))
    b=int(request.POST.get('b'))
    c=a+b
    return HttpResponse(c)

def login(request):

    user=request.POST.get('user')
    pwd=request.POST.get('pwd')
    print(user,pwd)
    user1=models.User.objects.filter(name=user,pwd=pwd).first()
    status={'user':None,'message':None}
    if user1:
        status['user']=user
    else:
        status['message']="用户名或密码错误"
    print(status)
    return HttpResponse(json.dumps(status))


def fy(request):
    '''

    :param 批量导入:
    :return:
    '''
    # book_list=[]
    # for i in range(100):
    #     book=models.Shu(title='book_%s'%i,price=i*i)
    #     book_list.append(book)
    # models.Shu.objects.bulk_create(book_list)
    shu_list=models.Shu.objects.all()
    paginator=Paginator(shu_list,10)
    print(paginator.count) #数据总页数
    print(paginator.num_pages) #总页数
    print(paginator.page_range)#页码列表
    current_page_num=int(request.GET.get("page",1))
    current_page=paginator.page(current_page_num) #第几页的所有数据对象


    return  render(request,'fy.html',locals())


