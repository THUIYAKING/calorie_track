from django.shortcuts import render, redirect
from .models import Food

# Create your views here.

def default_view(request):
    return render(request, 'home.html')
#add a new food item.  
def add_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        calories = request.POST['calories']
        food = Food(name=name, calories=calories)
        food.save()
        return redirect('food_list')
    return render(request, 'add_food.html')
#displays a list of all the food items in the database.
def food_list(request):
    foods = Food.objects.all()
    total_calories = sum(food.calories for food in foods)
    return render(request, 'food_list.html', {'foods': foods, 'total_calories': total_calories})

# remove a specific food item. It deletes the food object
def remove_food(request, food_id):
    food = Food.objects.get(id=food_id)
    food.delete()
    return redirect('food_list')
#resets the food list
def reset_calories(request):
    Food.objects.all().delete()
    return redirect('food_list')
