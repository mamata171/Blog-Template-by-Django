from django.shortcuts import render,HttpResponse
from blog.models import blog
from django.utils.text import slugify
from math import ceil
# Create your views here.

# {% load django.template %}

def home(request):
    # blog.objects.filter(title='').delete()

    return render(request,'index.html')

def blogs(request):
    no_of_blogs = 3
    page = request.GET.get('page')

    if page is None:
        page = 1
    else:
        page = int(page)

    # 1 : 0 - 3
    # 2 : 3 - 6
    # 3 : 6 - 9

    # Formula to slice three post 
    # (page-1)*no_of_blogs to page*no_of_blogs

    blogs = blog.objects.all()
    length = len(blogs)
    print(length)
    blogs = blogs[(page-1)*no_of_blogs : page*no_of_blogs]

    if page>1:
        prev = page - 1
    else:
        prev = None
    
    if page<ceil(length/no_of_blogs):
        nxt = page + 1
    else:
        nxt = None

    print(prev,nxt)

    context = {'blogs' : blogs,'prev': prev,'nxt':nxt}
    return render(request,'blogs.html',context)

def blogpost(request,slug):
    
    myblog = blog.objects.filter(slug = slug).first()
    context = {'blog' : myblog}
    return render(request,'blogpost.html',context)
    
def search(request):
    return render(request,"search.html")

def contact(request):
    return render(request,'contact.html')
                            