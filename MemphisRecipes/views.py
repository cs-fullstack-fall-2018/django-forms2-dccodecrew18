from django.shortcuts import render

from .models import food
def goodeats (request):
    MemphisRecipes_list = food.objects.all()
    context = {"MemphisRecipes_list": MemphisRecipes_list}
    return render(request,'FoodTemplates/index',context)
# make templates and static

# Create your views here.
