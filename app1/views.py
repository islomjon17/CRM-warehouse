from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from .models import Product, Client, Ombor

from statistika.models import Stats


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    def post(self, request):
        u = request.POST.get("login")
        p = request.POST["password"]
        users = authenticate(request, username=u, password=p)
        if users is None:
            return redirect("login")
        else:
            login(request, users)
            return redirect("bolim")

class BolimView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        else:
            return redirect("login")

class MahsulotView(View):
    def get(self, request):
        if request.user.is_authenticated:
            print(request.user)
            o = Ombor.objects.get(user=request.user)
            p = Product.objects.filter(ombor=o)
            return render(request, 'products.html', {"all_products":p})
        else:
            return redirect("login")
    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        Product.objects.create(
            nom=request.POST["pr_name"],
            brend_nomi=request.POST["pr_brand"],
            kelgan_narxi=request.POST["pr_price"],
            sotuvdagi_narx=request.POST["pr_sotuvdagi_narx"],
            miqdor=request.POST["pr_amount"],
            ombor=ombor
        )
        return redirect("mahsulotlar")

class MahsulotEdit(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            product = Product.objects.get(id=son)
            return render(request, 'product_update.html', {"product":product})
        else:
            return redirect("login")
    def post(self, request, son):
        if request.user.is_authenticated:
            product = Product.objects.get(id=son)
            product.nom=request.POST["name"]
            product.brend_nomi=request.POST["brand_name"]
            product.kelgan_narxi=request.POST["price"]
            product.sotuvdagi_narx=request.POST["price2"]
            product.miqdor=request.POST["amount"]
            product.save()
            return redirect("mahsulotlar")
        else:
            return redirect("login")


class ClientView(View):
    def get(self, request):
        if request.user.is_authenticated:
            o = Ombor.objects.get(user=request.user)
            clients = Client.objects.filter(ombor=o)
            return render(request, 'clients.html', {"all_clients":clients})
        else:
            return redirect("login")
    def post(self, request):
        ombor = Ombor.objects.get(user=request.user)
        Client.objects.create(
            ism=request.POST["ism"],
            dokon_nomi=request.POST["dokon_nomi"],
            tel=request.POST["tel"],
            joylashuv=request.POST["joylashuv"],
            qarz=request.POST["qarz"],
            ombor=ombor
        )
        return redirect("clientlar")
        
        
class ClientEdit(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            # stats = Stats.objects.get(id=son)
            # o = Ombor.objects.get(user=request.user)
            client = Client.objects.get(id=son)
            ombor = Ombor.objects.get(user=request.user)
            return render(request, 'client_update.html', { "ombor":ombor, "client":client})
        else:
            return redirect("login")
    def post(self, request, son):
        if request.user.is_authenticated:
            ombor = Ombor.objects.get(user=request.user)
            client = Client.objects.get(id=son)
            client.ism=request.POST["ism"]
            client.dokon_nomi=request.POST["dokon_nomi"]
            client.tel=request.POST["tel"]
            client.joylashuv=request.POST["joylashuv"]
            client.qarz=request.POST["qarz"]
            client.ombor=ombor
            client.save()
            
            
            return redirect("clientlar")
        else:
            return redirect("login")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

