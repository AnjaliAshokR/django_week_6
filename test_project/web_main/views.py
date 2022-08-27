from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control

from .models import Product
# Create your views here.

# view function for home page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if 'user' in request.session:
        product = Product.objects.all()
        products = {'products': product}
        return render(request,'home.html', products)
    else:
        return redirect('credentials:login')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def welcome_page(request):
    request.session.flush()
    return render(request,'welcomepage.html')