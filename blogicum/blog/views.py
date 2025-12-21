from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from blog.models import Category
from django.http import Http404


# Дата сейчас
cur_date = timezone.now()


def index(request):
    """View функция главной страницы"""
    posts = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(pub_date__lte=cur_date,
             is_published=True,
             category__is_published=True)[0:5]
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, id):
    """Обработчик для страницы поста"""
    try:
        post = Post.objects.select_related('category').filter(id=id)[0]
        publish = post.is_published and post.category.is_published
        if post and post.pub_date <= cur_date and publish:
            return render(request, 'blog/detail.html', {'post': post})
        else:
            return render(request, 'blog/detail.html', {'post': {}})
    except Exception:
        raise Http404('пост не найден')


def category_posts(request, category):
    """Обработчик для страницы категории"""
    try:
        finded_category = Category.objects.get(slug=category)
        posts = []
        if finded_category.is_published:
            posts = Post.objects.select_related(
                'category').filter(category__slug=category,
                                   is_published=True,
                                   pub_date__lte=cur_date)
            return render(request, 'blog/category.html',
                          {'category': finded_category, 'posts': posts})
        else:
            raise Http404('category is not published')
    except Exception:
        raise Http404('category is not published')

