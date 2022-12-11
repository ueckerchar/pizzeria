from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('pizza_name')

    context = {'allpizzas':pizzas}
    return render(request, 'MainApp/pizzas.html', context)

def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza=p)
    context = {'pizza':p, 'toppings':toppings}
    return render(request, 'MainApp/pizza.html', context)

def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
    else:
        form = CommentForm()
        return redirect('MainApp:pizza',pizza_id=pizza_id)
    context = {'form':form, 'pizza':pizza}
    return render(request, 'MainApp/comment.html', context)