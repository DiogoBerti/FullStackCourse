from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)

from blog.models import Post, Comments
from blog.forms import PostForm, CommentForm
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        # __lte == less than or equal..
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


# O LoginRequiredMixin é uma classe que funciona como uma autenticaçao
# Ou seja, permite apenas que algo seja feito caso o User esteja logado...
# Os decorators tbm fazem isso, mas em classes baseadas em view, a melhor
# maneira é essa..
class CreatePostView(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = '/blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(UpdateView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = '/blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(DeleteView,LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(ListView,LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = '/blog/post_detail.html'
    model = Post

    def get_queryset(self):
        # __isnull == Checa se o campo não esta preenchido
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')
