from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'posts/index.html')
    
    
import random

numbers = [1, 2, 3, 4, 5]
rand_numbers = random.sample(numbers, 3)
print(rand_numbers)