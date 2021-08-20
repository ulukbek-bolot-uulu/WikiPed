from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Posts
from .forms import PostForm, CategoryForm



def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', context={'categories_list': categories})


def posts_list(request, pk):
    category = Category.objects.get(pk=pk)
    posts_list = Posts.objects.filter(category_id=category)
    return render(request, 'posts_list.html', context={'posts_list': posts_list})

def post_detail(request, pk):
    category = Category.objects.get(pk=pk)
    posts_list = Posts.objects.filter(category_id=category)
    # post_detail = get_object_or_404(Posts, pk=pk)
    return render(request, 'post_detail.html', {'post_detail': posts_list})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'post_add.html', {'form': form})

def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = CategoryForm()
    return render(request, 'category_add.html', {'form': form})

def about(request):
    return render(request, 'about.html')
