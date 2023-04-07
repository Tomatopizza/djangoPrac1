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
        exist_calc.save()
        if(exist_calc.num != None):
            return HttpResponse(exist_calc.num)

def first_view(request):
    return render(request, 'calc.html')
# Create your views here.
        
