from django.shortcuts import render,HttpResponse,redirect
from book import models
# Create your views here.

from django.db.models import Avg,Count,Sum,Count
def add_book(request):

    if request.method=="POST":

        title=request.POST.get('title')
        price=request.POST.get('price')
        date=request.POST.get('data')
        publish=request.POST.get('publish')
        book_ojb=models.Book1.objects.create(title=title,price=price,pub_data=date,publish=publish)
        return  redirect('/book/select_book/')
    return render(request,'add_book.html')




def select_book(request):
    book_list=models.Book1.objects.all()


    return render(request,'select_book.html',locals())

def delbook(reqeust,id):

    models.Book1.objects.filter(id=id).delete()

    return redirect("/book/select_book/")

def upbook(request,id):
  if request.method=="GET":
   book_ojb=models.Book1.objects.filter(id=id).first()

   return  render(request,'update_book.html',locals())
  else:
        title=request.POST.get('title')
        price=request.POST.get('price')
        date=request.POST.get('data')
        publish=request.POST.get('publish')
        book_obj=models.Book1.objects.filter(id=id).update(title=title,price=price,pub_data=date,publish=publish)
        return redirect('/book/select_book/')


def add_duo(request):

    # #publish_obj=models.Publish.objects.get(nid=1)
    # book_obj=models.Book.objects.create(title="追风筝的人",price=200,publishDate="2012-11-12",publish_id=1)
    # #
    # #publish_obj2=models.Publish.objects.get(nid=2)
    # book_obj1=models.Book.objects.create(title="京瓶梅",price=500,publishDate="2012-01-12",publish_id=2)
    #
    # fyt=models.Author.objects.filter(name='fyt').first()
    # sxy=models.Author.objects.filter(name='sxy').first()
    # book_obj.authors.add(fyt)
    # book_obj1.authors.add(sxy)

    authordeali_ojb=models.AuthorDetail.objects.get(nid=3)
    author_ojb=models.Author.objects.create(nid=3,name='zsp',age=28,authordetail=authordeali_ojb)

    return  HttpResponse('ok')



def se(request):
    # ret=models.Author.objects.filter(name="fyt").values('authordetail__telephone')
    # print(ret)

    # ret=models.AuthorDetail.objects.filter(author__name='fyt').values('telephone')
    # print(ret)
    # ret=models.Book.objects.filter(authors__authordetail__telephone="123").values('title','publish__name')
    # print(ret)
    ret=models.Book.objects.filter(title__startswith='京').values('pk').annotate(c=Count("authors__name")).values('c','title')
    print(ret)
    return  HttpResponse('查询成功')



def duo_add(request):
    if request.method=="POST":
        title=request.POST.get('title')
        price=request.POST.get('price')
        pub_data=request.POST.get('data')
        publish_id=request.POST.get('publish_id')
        authors_id_list=request.POST.getlist('authors_id_list')
        book_obj=models.Book.objects.create(title=title,price=price,publishDate=pub_data,publish_id=publish_id)
        book_obj.authors.add(*authors_id_list)
        return  redirect('/book/s_book/')

    publish_list=models.Publish.objects.all()
    author_list=models.Author.objects.all()

    return  render(request,'duo_add.html',{'author_list':author_list,"publish_list":publish_list})

def s_book(request):


    book_list=models.Book.objects.all()



    return  render(request,'s_book.html',{'book_list':book_list})

def change(request,edit_book_id):
    if request.method=="POST":
        title=request.POST.get('title')
        price=request.POST.get('price')
        pub_data=request.POST.get('data')
        publish_id=request.POST.get('publish_id')
        authors_id_list=request.POST.getlist('authors_id_list')
        models.Book.objects.filter(pk=edit_book_id).update(title=title,price=price,publishDate=pub_data,publish=publish_id)
        edit_book=models.Book.objects.filter(pk=edit_book_id).first()
        # edit_book.authors.clear()
        # edit_book.authors.add(*authors_id_list)
        edit_book.authors.set(authors_id_list)
        return redirect('/book/s_book/')
    else:
        publish_list=models.Publish.objects.all()
        author_list=models.Author.objects.all()
        edit_book=models.Book.objects.filter(pk=edit_book_id).first()
        return  render(request,'up.html',{'edit_obj':edit_book,'publish_list':publish_list,'author_list':author_list})


def shanchu(request,de_id):

    models.Book.objects.filter(pk=de_id).delete()
    return redirect('/book/s_book/')








