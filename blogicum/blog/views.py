from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.utils import timezone

# Create your views here.


def index(request):
    dt_now = timezone.now()
    posts = Post.objects.filter(
        pub_date__lte=dt_now,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[0:5]
    # posts.order_by('pub_date')
    return render(request, 'blog/index.html', {'post_list': posts})


def post_detail(request, post_id):
    dt_now = timezone.now()
    post = get_object_or_404(
        Post,
        pk=post_id,
        pub_date__lte=dt_now,
        is_published=True,
        category__is_published=True
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    dt_now = timezone.now()
    posts = Post.objects.filter(
        pub_date__lte=dt_now,
        is_published=True,
        category=category
    )
    return render(
        request,
        'blog/category.html',
        {
            'post_list': posts,
            'category': category
        }
    )
