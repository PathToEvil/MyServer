from django.conf.urls import url
from website import views

urlpatterns = [
    url(r'post/(?P<id>\d+)/$', views.Detail, name="blog_detail"),
    url(r'home/', views.home, name="blog_home"),
    url(r'^test/', views.Test, name="website_test"),
]