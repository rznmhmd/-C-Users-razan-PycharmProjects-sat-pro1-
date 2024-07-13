from django.shortcuts import render
from .models import Category, Post
from django.http import HttpResponse
from django.template import loader
def blog(request):
  myblogs = blog.objects.all().values()
  template = loader.get_template('base.html')
  context = {
    'myblogs': myblogs,
  }
  return HttpResponse(template.render(context, request))

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def details(request, id):
    myblogs = blog.objects.get(id=id)
    template = loader.get_template('post_detail.html')
    context = {
        'myblogs': myblogs,
    }
    return HttpResponse(template.render(context, request))
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})