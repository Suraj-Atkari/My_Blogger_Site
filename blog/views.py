from datetime import date
from django.shortcuts import render
from .models import Post

# Create your views here.
all_posts = [

]


def get_date(post):
    return post["date"]


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_post = sorted(all_posts, key=get_date)
    # latest_posts = sorted_post[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_post": all_posts
    })


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
