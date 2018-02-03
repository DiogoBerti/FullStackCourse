from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from blog.models import Post, Comments
from blog.forms import PostForm, CommentForm
from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
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

##############
'''
Views de Comments
'''
################

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk )

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk)
    post.publish()
    return redirect('post_detail', pk=post.pk)
