from django.shortcuts import render, HttpResponseRedirect
from .forms import RegisterForm
from myappproducts.models import *

def landing(request):
    name = 'my friend'
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        new_form = form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, 'myapp/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    products_images_headphones = products_images.filter(product__category__id=3)
    products_images_tablets = products_images.filter(product__category__id=4)
    return render(request, 'myapp/home.html', locals())


