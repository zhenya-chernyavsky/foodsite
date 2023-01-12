from django.shortcuts import render, redirect
from .forms import FoodForm, UserRegisterForm, UserLoginForm
from .models import Food, Category, Recipes
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages

def user_logout(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'food/register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'food/login.html', context)

class HomeFood(MyMixin, ListView):
    model = Food
    context_object_name = 'food'

    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['category'] = categories
        context['title'] = 'Список блюд'
        return context

    def get_queryset(self):
        return Food.objects.filter(is_published=True)

class FoodBYCategory(MyMixin, ListView):
    model = Food
    template_name = 'food/home_food_list.html'
    context_object_name = 'food'
    allow_empty = True
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['category'] = categories
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return Food.objects.filter(category=self.kwargs['category_id'], is_published=True)

class ViewFood(DetailView):
    model = Food
    context_object_name = 'food_item'

class CreateFood(LoginRequiredMixin, CreateView):
    form_class = FoodForm
    template_name = 'food/add_food.html'
    raise_exception = True
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['category'] = categories
        return context


class ViewRecipes(MyMixin, ListView):
    model = Recipes
    template_name = 'food/recipes_food.html'
    raise_exception = True
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        recipes = Recipes.objects.all()
        context['category'] = categories
        context['recipes'] = recipes
        context['title'] = 'Рецепты'
        return context

    def get_queryset(self):
        return Recipes.objects.all()
















# def get_category(request, category_id):
#     food = Food.objects.filter(category__id=category_id)
#     categories = Category.objects.all()
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'food': food,
#         'categories': categories,
#         'category': category,
#     }
#     return render(request, 'food/category.html', context)



# def view_recipes(request):
#    categories = Category.objects.all()
#    recipes = Recipes.objects.all()
#    context = {
#        'recipes': recipes,
#        'title': 'Рецепты',
#        'category': categories
#    }
#    return render(request, 'food/recipes_food.html', context)

# def add_food(request):
#     categories = Category.objects.all()
#     if request.method == "POST":
#         form = FoodForm(request.POST)
#         if form.is_valid():
#             food = form.save()
#             return redirect(food)
#     else:
#         form = FoodForm()
#
#     context = {
#         'form': form,
#         'category': categories
#     }
#     return render(request, 'food/add_food.html', context)

# def view_food(request, food_id):
#     food_item = get_object_or_404(Food, pk=food_id)
#     categories = Category.objects.all()
#     # food_item = Food.objects.get(pk=food_id)
#     context = {
#         'food_item': food_item,
#         'category': categories
#     }
#     return render(request, 'food/view_food.html', context)

# def index(request):
#     food = Food.objects.order_by('create_at')
#     categories = Category.objects.all()
#     context = {
#         'food': food,
#         'title': 'список блюд',
#         'category': categories,
#     }
#     return render(request, 'food/index.html', context)

    # extra_context = {'title': 'список блюд'}