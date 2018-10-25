# from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy, reverse
# from django.contrib.auth.mixins import LoginRequiredMixin,              PermissionRequiredMixin
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect, HttpResponse
# from django.utils import timezone

# from .models import Post
# from .forms import PostForm
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin,              PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from django.contrib.auth import get_user_model
from braces.views import SelectRelatedMixin
from django.utils import timezone
from django.contrib import messages


from . import models, forms

User = get_user_model()


class AboutView(generic.TemplateView):
    template_name = 'Blog/about.html'


class PostListView(generic.ListView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        return models.Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class UserPost(generic.ListView):
    model = models.Post
    template_name = 'Blog/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetailView(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )


class CreatePostView(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('text', 'group')
    model = models.Post

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.author = self.request.user
        self.obj.save()
        return super().form_valid(form)


# class UpdatePostView(LoginRequiredMixin, UpdateView):
#     login_url = '/login/'
#     redirect_field_name = 'Blog/post_detail.html'
#     form_class = PostForm
#     model = Post


class DeletePostView(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
