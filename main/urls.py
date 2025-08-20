from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.CatalogView.as_view(), name='catalog'),
    path('item/<slug:slug>', views.ClothingItemDetailView.as_view(), name='clothing_item_detail')
]
