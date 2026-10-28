from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Article

def archive(request):
    posts = Article.objects.select_related('author').all()
    return render(request, 'articles/archive.html', {'posts': posts})

def get_article(request, article_id):
    post = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/article.html', {'post': post})

from .forms import ArticleForm

def create_post(request):
    if not request.user.is_authenticated:
        raise Http404
    form = ArticleForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        return redirect('get_article', article_id=article.pk)
    return render(request, 'articles/create_post.html', {'form': form})
