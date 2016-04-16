from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db.models import Q
from . import models
from .models import Entry, Comment
from .forms import EntryForm, CommentForm
from django.utils import timezone
# Create your views here.


class NewsIndex(generic.ListView):
	model = models.Entry
	queryset = models.Entry.objects.published()
	template_name = "blog2/Entry_list.html"
	paginate_by = 5


class NewsDetail(generic.DetailView):
    model = models.Entry
    template_name = "blog2/news_detail.html"


class ArchiveView(generic.ListView):
    model = models.Entry
    queryset = models.Entry.objects.all().order_by("-created")
    template_name = "blog2/archive.html"
    paginate_by = 5

class CategoryView(generic.ListView):
    model = models.Entry
    queryset = models.Entry.objects.all().order_by("-tags")
    template_name = "blog2/category.html"
    paginate_by = 5


class AboutPage(generic.TemplateView):
    template_name = "blog2/about.html"


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog2.views.news_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog2/add_comment_to_post.html', {'form': form})



@login_required
def post_new(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('news_detail', kwargs={"slug":self.slug})
    else:
        form = EntryForm()
    return render(request, 'blog2/post_edit.html', {'form': form})




@login_required
def post_edit(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('news_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog2/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    posts = Entry.objects.filter(created__isnull=True).order_by('-created')
    return render(request, 'blog2/post_draft_list.html', {'posts': posts})
