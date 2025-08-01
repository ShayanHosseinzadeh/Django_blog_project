from django.db.models.aggregates import Count
from django.db.models.query_utils import Q
from django.shortcuts import render, reverse, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from .models import Post, Tag
from .forms import PostForm, CommentForm


class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts_list'
    paginate_by = 3

    def get_queryset(self):
        queryset = Post.objects.filter(status='pub').order_by('-datetime_modified')
        query = self.request.GET.get('q')

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(text__icontains=query)
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_posts = Post.objects.filter(status='pub').order_by('-datetime_created')[:5]
        context['recent_posts'] = recent_posts
        context['query'] = self.request.GET.get('q')

        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.id)

        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
