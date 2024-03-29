from django.shortcuts import render
from blog.models import blog
from django.utils.text import slugify
from math import ceil
from blog.models import contact_me

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

    # 1 : 0 - 3  here 3 is excluded
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
    print(myblog)
    return render(request,'blogpost.html',context)
    
def search(request):
    return render(request,"search.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        obj = contact_me(name = name,email = email,message = message)
        obj.save()

    return render(request,'contact.html')
                            