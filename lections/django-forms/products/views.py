from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            form = ProductForm(initial={
                "user": request.user
            })
            return render(request, "products/add.html", {"form": form})
        else:
            form = ProductForm(request.POST)
            # print("HELO ================================= ")
            # print(form.is_valid())
            # print(form.__dict__)
            if form.is_valid():
                form.save(user=request.user)
                return redirect("/")
            else:
                return render(request, "products/add.html", {"form": form})

    else:
        return redirect("/")


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product": product})
