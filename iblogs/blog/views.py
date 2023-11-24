from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from django.utils import timezone
from blog.models import Post,Category,Comment

# Create your views here.
def home(request):
    #load all the post from db(10)
    posts=Post.objects.all()[:11]
    # print(posts)

    cats=Category.objects.all()

    data={
        'posts':posts,
        'cats':cats
    }
    return render(request,'home.html', data)

def post(request, url):
    post=Post.objects.get(url=url)
    cats = Category.objects.all()
    # print(post)
    return render(request,'posts.html', {'post':post,'cats':cats})

def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,'category.html', {'cat':cat,'posts':posts})

def about(request):
    return render(request,'about.html',{})


# def Add_Comment(request,id):
#     post = Post.objects.get(id=id)
#     com=Comment.objects.all()
#     return render(request,'Add_Comment.html',{'post':post,'com':com})

def add_comment(request,url):
    if request.method == "POST":
        ob = Comment()
        ob.post = Post.objects.get(url=url)
        ob.commenter_name = request.POST.get('com_name')
        ob.commenter_body = request.POST.get('com_body')
        ob.date_added=date.today()
        ob.save()
    return render(request,"Add_Comment.html")
