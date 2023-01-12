from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeFood.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('category/<int:category_id>/', FoodBYCategory.as_view(), name='category'),
    path('food/<int:pk>/', ViewFood.as_view(), name='view_food'),
    path('food/view_recipes/', ViewRecipes.as_view(), name='view_recipes'),
    path('food/add-food/', CreateFood.as_view(), name='add_food')
]