from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category


def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_home=False),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)

    return render(request, "blog/blog-details.html", {
        "blog": blog
    })


def blogs_by_category(request, slug):
    category = Category.objects.get(slug=slug)

    context = {
        "blogs": category.blog_set.filter(is_active=True),
#        "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category": slug
    }

    return render(request, "blog/index.html", context)