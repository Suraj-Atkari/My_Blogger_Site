from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic.base import TemplateView, View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, FormView, UpdateView

# Create your views here.


# def get_date(post):
#     return post["date"]
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
#     # sorted_post = sorted(all_posts, key=get_date)
#     # latest_posts = sorted_post[-3:]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts
#     })


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_post"
    ordering = ["-date"]


# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_post": all_posts
#     })


class DetailedPostView(DetailView,):
    template_name = "blog/post-detail.html"
    model = Post
    # context_object_name = "post"
    # slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context


# def post_detail(request, slug):
#     identified_post = get_object_or_404(
#         Post, slug=slug)  # Post.obejcts.get(slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     }
#     )
