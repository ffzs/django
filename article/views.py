from django.shortcuts import render
from django.http import HttpResponse
from article.models import Artical

# Create your views here.
def home(request):
    post_list = Artical.objects.all()

    return render(request,'home.html',{'post_list':post_list})

def detail(request,my_args):
    print(my_args)
    post = Artical.objects.get(id= int(my_args))
    return render(request,'post.html',{'post':post})




