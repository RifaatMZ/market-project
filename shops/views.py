from django.shortcuts import render, redirect
from .models import Shop, ItemDetail
from django.views import generic
from django.urls import reverse_lazy
from .forms import ItemDetailForm

# Create your views here.

def home(request):
    return render(request, 'shops/home.html')

def my_shop(request):
    shop = Shop.objects.filter(user=request.user)
    return render(request, 'shops/my_shop.html', {'shop': shop})

def add_item(request, pk):
    form = ItemDetailForm()

    if request.method == 'POST':
        filled_form = ItemDetailForm(request.POST)
        if filled_form.is_valid():
            item = ItemDetail()
            item.item = filled_form.cleaned_data['item']
            item.price = filled_form.cleaned_data['price']
            item.in_stock = filled_form.cleaned_data['in_stock']
            item.quantity = filled_form.cleaned_data['quantity']
            item.shop = Shop.objects.get(pk=pk)
            item.save()

    return render(request, 'shops/add_item.html', {'form': form})


class CreateShop(generic.CreateView):
    model = Shop
    fields = ['name', 'location', 'delevery_zone', 'address', 
            'description', 'phone', 'email', 'logo', 'image']
    template_name = 'shops/create_shop.html'
    success_url = reverse_lazy('my_shop')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateShop, self).form_valid(form)
        return redirect('my_shop')

class DetailShop(generic.DetailView):
    model = Shop
    template_name = 'shops/detail_shop.html'

class UpdateShop(generic.UpdateView):
    model = Shop
    template_name = 'shops/update_shop.html'
    fields = ['name', 'location', 'address', 'delevery_zone', 
            'description', 'phone', 'email', 'logo', 'image']
    success_url = reverse_lazy('my_shop')
    
class DeleteShop(generic.DeleteView):
    model = Shop
    template_name = 'shops/delete_shop.html'
    success_url = reverse_lazy('home')
    
