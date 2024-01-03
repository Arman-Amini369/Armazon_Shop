from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AddCartForm, AddCommentForm
from .models import Category, Product, Comment, Cart

def home(request):
    category = Category.objects.all()
    return render(request, "store/index.html", {"categories" : category})

def category_product(request, category_title):
    products = Product.objects.filter(category__name=category_title)
    return render(request, "store/category_products.html", {"products" : products})

def product_info(request, product_id):
    products = Product.objects.filter(id=product_id)
    for product in products:
        image = product.image.name
    comments = Comment.objects.filter(product__id=product_id)
    return render(request, "store/product_info.html", {"products" : products, "image" : image, "comments" : comments})

@login_required(login_url="accounts:user_login")
def add_cart(request, product_id):
    if request.method == "POST":
        form = AddCartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            product = Product.objects.filter(id=product_id)
            cart = form.save(commit=False)
            cart.product = product.first()
            cart.user = request.user
            cart.save()
            messages.success(request, "Product added to cart successfully", 'success')
            return redirect("store:home")
    else:
        form = AddCartForm()
    return render(request, "store/add_cart.html", {"form" : form})

@login_required(login_url="accounts:user_login")
def cart_info(request, user_id):
    cart = Cart.objects.filter(user__id=user_id)
    return render(request, "store/cart_info.html", {"carts" : cart})

@login_required(login_url="accounts:user_login")
def add_comment(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.product = product
            comment.save()
            messages.success(request, "Comment added successfully", 'success')
            return redirect("store:product_info", product_id)
    else:
        form = AddCommentForm()
    return render(request, "store/add_comment.html", {"form" : form})