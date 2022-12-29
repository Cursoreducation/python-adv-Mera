from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MenuItem
from products.models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q


def home(request):
    menu_items = MenuItem.objects.all()
    products = Product.objects.filter(display_on_main_page=True, approved=True).order_by("-id")
    print(request.user)
    return render(request, 'main/index.html', {
        "menu_items": menu_items,
        "products": products,
        "count_cart": len(request.session.get("cart", {"products": [], "total": 0})["products"])
    })


def sign_up(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.set_password(request.POST.get("password"))
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("/")
    else:
        return render(request, "main/sign-up.html", {})


def sign_in(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        print("================USER ===============")
        print(user)
        if user:
            login(request, user)
        return redirect("/")
    else:
        return render(request, "main/sign-in.html", {})


def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    if request.session.get("cart", False):
        is_product_already_added = False
        for el in request.session.get("cart", {"products": [], "total": 0})["products"]:
            if el["id"] == id:
                el["count"] = el["count"] + 1
                request.session["cart"]["total"] = request.session["cart"]["total"] + product.price
                el["price"] = el["price"] + product.price
                is_product_already_added = True
        if not is_product_already_added:
            request.session["cart"]["total"] = request.session["cart"]["total"] + product.price
            request.session["cart"]["products"].append({
                "id": product.id,
                "title": product.title,
                "price": product.price,
                "count": 1
            })
    else:
        request.session["cart"] = {
            "products": [],
            "total": 0
        }
        request.session["cart"]["total"] = product.price
        request.session["cart"]["products"].append({
            "id": product.id,
            "title": product.title,
            "description": product.description,
            "price": product.price,
            "count": 1
        })
    request.session.modified = True
    return redirect("/cart")


def show_cart(request):
    return render(request, "main/cart.html", {
        "count_cart": len(request.session.get("cart", {"products": [], "total": 0})["products"]),
        "products": request.session.get("cart", {"products": [], "total": 0})["products"],
        "total": request.session.get("cart", {"products": [], "total": 0})["total"],
    })


def delete_cart(request, id):
    if request.session.get("cart", False):
        products = request.session["cart"]["products"]
        for i in range(len(products)):
            print(products[i])
            print(id)
            if products[i]["id"] == int(id):
                request.session["cart"]["total"] = request.session["cart"]["total"] - products[i]["price"]
                del request.session["cart"]["products"][i]
                request.session.modified = True
                break
        return redirect("/cart")



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")
