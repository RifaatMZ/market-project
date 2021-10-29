from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shops'),
    path('my_shop/', views.my_shop, name='my_shop'),
    path('create/', views.CreateShop.as_view(), name='create_shop'),
    path('<int:pk>/', views.DetailShop.as_view(), name='detail_shop'),
    path('<int:pk>/update', views.UpdateShop.as_view(), name='update_shop'),
    # path('<int:pk>/delete', views.DeleteShop.as_view(), name='delete_shop'),

]