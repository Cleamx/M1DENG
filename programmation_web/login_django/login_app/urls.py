from django.urls import path
from .views import login_view, welcome_view, logout_view, signup_view, inventory_list, add_item, update_item, delete_item

urlpatterns = [
    path('login/', login_view, name='login'),
    path('welcome/', welcome_view, name='welcome'),
    path('signup/', signup_view, name='signup'),
    path('inventory/', inventory_list, name='list'),
    path('inventory/add/', add_item, name='add_item'),
    path('inventory/update/<int:item_id>/', update_item, name='update_item'),
    path('inventory/delete/<int:item_id>/', delete_item, name='delete_item'),
    path('logout/', logout_view, name='logout'), 
]
