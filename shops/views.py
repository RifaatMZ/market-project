from django.shortcuts import render, redirect
from .models import Shop 
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

def home(request):
    return render(request, 'shops/home.html')

def my_shop(request):
    shop = Shop.objects.filter(user=request.user)
    return render(request, 'shops/my_shop.html', {'shop': shop})

class CreateShop(generic.CreateView):
    model = Shop
    fields = ['name', 'location', 'delevery_zone', 'address', 
            'description', 'phone', 'email', 'logo', 'image']
    tempalte_name = 'shops/shop_form.html'
    success_url = reverse_lazy('my_shop')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateShop, self).form_valid(form)
        return redirect('my_shop')

class DetailShop(generic.DetailView):
    model = Shop
    tempalte_name = 'shops/shop_detail.html'

class UpdateShop(generic.UpdateView):
    model = Shop
    tempalte_name = 'shops/shop_update.html'
    fields = ['name', 'location', 'address', 'delevery_zone', 
            'description', 'phone', 'email', 'logo', 'image']
    success_url = reverse_lazy('my_shop')
    