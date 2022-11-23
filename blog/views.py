from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView, View
from django.views.generic import DetailView, ListView, FormView
from .forms import CommentFormView
from django.urls import reverse

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


class DetailedPostView(View):
    # template_name = "blog/post-detail.html"
    # model = Post
    # context_object_name = "post"
    # slug_field = "slug"
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentFormView()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentFormView(request.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
            "post": post,
            "post-tags": post.tags.all(),
            "comment_form": CommentFormView()
        }

        return render(request, "blog/post-detail.html", context)

        # This is comment out as we cannot POST the request while using FormView as we need
        # comment POST needs tobe handelled
        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #     context["post_tags"] = self.object.tags.all()
        #     context["comment_form"] = CommentFormView()
        #     return context

        # def post_detail(request, slug):
        #     identified_post = get_object_or_404(
        #         Post, slug=slug)  # Post.obejcts.get(slug=slug)
        #     return render(request, "blog/post-detail.html", {
        #         "post": identified_post,
        #         "post_tags": identified_post.tags.all()
        #     }
        #     )
