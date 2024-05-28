from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

from .forms import ContactForm


def index(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    certificates = Certificate.objects.filter(is_active=True)
    blogs = Blog.objects.filter(is_active=True)
    portfolio = Portfolio.objects.filter(is_active=True)
    context = {
        'testimonials': testimonials,
        'certificates': certificates,
        'blogs': blogs,
        'portfolio': portfolio
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you. We will be in touch soon.")
            return redirect('/')

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def portfolio(request):
    portfolios = Portfolio.objects.filter(is_active=True)
    context = {'portfolios': portfolios}
    return render(request, 'portfolio.html', context)


def portfolio_detail(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    context = {'portfolio': portfolio}
    return render(request, 'portfolio-detail.html', context)


def blog(request):
    blogs = Blog.objects.filter(is_active=True)
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {'blog': blog}
    return render(request, 'blog-detailcl.html', context)
