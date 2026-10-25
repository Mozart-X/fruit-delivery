from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Product
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello World !!")

def mainpage(request):
    products = Product.objects.all()
    return render(request, "index.html", {
        'products': products
        })

def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)

        cart = request.session.get("cart", {})
        cart[str(product.id)] = cart.get(str(product.id), 0) + 1
        request.session["cart"] = cart
        print("======================")
        print(request.session["cart"])
        print("======================")

    return redirect("mainpage")
