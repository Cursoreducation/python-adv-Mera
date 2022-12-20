from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Product, Category, CategoryProduct


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            categories = Category.objects.all()
            return render(request, "products/add.html", {"categories":categories})
        else:
            product = Product()
            product.title = request.POST.get("title")
            product.description = request.POST.get("description")
            product.user = request.user
            product.save()
            return redirect("/")
    else:
        return redirect("/")


def edit_product(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        categories = Category.objects.all()
        product_categories = CategoryProduct.objects.filter(product_id=product.id)
        return render(request, "products/add.html", {
            "product": product,
            "product_categories": product_categories,
            "categories": categories
        })
    else:
        raise PermissionDenied

def add_category(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/category/add.html")
        else:
            category = Category()
            category.title = request.POST.get("title")
            category.save()
            return redirect("/")


def update_product(request, id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=id)
        product.title = request.POST.get("title")
        product.description = request.POST.get("description")
        product.save()
        CategoryProduct.objects.filter(product_id = product.id).delete()
        for category in request.POST.getlist('categories', []):
            category_product = CategoryProduct()
            category_product.product = product
            category_product.category = Category.objects.get(id=int(category))
            category_product.save()
        return redirect("/")


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product": product})
