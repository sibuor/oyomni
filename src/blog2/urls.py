from django.conf.urls import patterns, url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from . import views
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import login, logout
#from rumors.views import UserProfileDetailView
#from django.contrib.auth.decorators import login_required as auth #for authentication
#from kadel.views import UserProfileEditView

urlpatterns = [
    url(r'^$', views.NewsIndex.as_view(), name="entry_list"),
    url(r'^entry/(?P<slug>\S+)$', views.NewsDetail.as_view(), name="news_detail"),
    #url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^archive/$', views.ArchiveView.as_view(), name="archive"),
    url(r'^category/$', views.CategoryView.as_view(), name="category"),
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}, name="login"), 
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

    #url(r'^login/$', 'django.contrib.auth.views.login', {
    #'template_name': 'login.html'}, name="login"),
    #url(r'^logout/$', 'django.contrib.auth.views.logout_then_login',
    #name="logout"),
    #url(r'^search/$', views.search, name="search"),
    #url(r'^post/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    #url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    #url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    #url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    #url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    #url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    #url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
]