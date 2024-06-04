from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolios'),
    path('portfolio/<slug:slug>', views.portfolio_detail, name='portfolio'),
    path('blog/', views.blog, name ='blogs'),
    path('blog/<slug:slug>', views.blog_detail, name='blog'),

]
