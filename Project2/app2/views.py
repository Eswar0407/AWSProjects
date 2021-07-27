from django.shortcuts import render,redirect
from app2.models import productinfoModel

# Create your views here.
def showIndex(request):
    return render(request,'index.html')

def saveProduct(request):
    if request.method == "POST":

        name = request.POST.get("product_name")
        price = request.POST.get("product_price")
        photo = request.FILES["product_photo"]

        productinfoModel(name=name,price=price,photo=photo).save()
        return redirect('main')

def viewProduct(request):
    return render(request, "index.html", {"product":productinfoModel.objects.all()})

def delete(request,id):
    product_details = productinfoModel.objects.get(number=id)
    if request.method == "POST":
        product_details.delete()
        return render(request,'index.html',{"product_info" : product_details})
    else:
        return render(request, "delete.html", {"product_info": product_details})
