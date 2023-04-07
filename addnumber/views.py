from django.shortcuts import render
from django.http import HttpResponse
from .models import Calculator

def calculate(request):
    if request.method == 'GET':
        return render(request, 'calc.html')
    elif request.method == 'POST':
        number = request.POST.get('number',None)
        number = int(number)
        exist_calc = Calculator.objects.get()
        exist_calc.num += number
        result = exist_calc.num
        exist_calc.save()
        return render(request, 'calc.html', {'calculate': result})
        
        

def first_view(request):
    return render(request, 'calc.html')
# Create your views here.
        
