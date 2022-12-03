from django.db import models

# Create your models here.
# super user pass: Snoopy#Callie23
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=50)
    text = models.TextField()
