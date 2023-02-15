from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np
from .models import Category, Modul
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.


def calculator(request):
    res = 0
    if request.method == 'POST':
        number1 = request.POST.get('number1')
        char = request.POST.get('char')
        number2 = request.POST.get('number2')
        res = 0
        if char == '+':
            res = int(number1) + int(number2)
        elif char == '-':
            res = int(number1) - int(number2)
        elif char == '*':
            res = int(number1) * int(number2)
        elif char == '/':
            try:
                res = int(number1) / int(number2)
            except ZeroDivisionError:
                res = 'Number2 enter all without 0'
    return render(request, 'math_modul/calculator.html', context={'res':res})


def graph(request):
    res = 0
    res1 = 0
    res2 = 0
    y = []
    X = []
    if request.method == 'POST':
        x = request.POST.get('x')
        k = request.POST.get('k')
        b = request.POST.get('b')
        res = x.split(' ')
        for i in res:
            X.append(int(i))
            y.append(np.sin(int(i)))
            # y.append(6 / int(i))
        res1 = X
        res2 = y
        f = plt.figure(figsize=(10, 6), dpi=300)
        plt.plot(res1, res2, color='r', lw=4, ls='--', label='sin(x)')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend(loc=0)
        plt.grid()
        res = plt.gcf()
        buf = io.BytesIO()
        res.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        res = uri
        f.clear()
    return render(request, 'math_modul/graph.html', context={'data':res, 'res1':res1, 'res2':res2})



class InfoCategoryListView(ListView):
    template_name = 'math_modul/info.html'

    def get(self, request):
        search_info = request.GET.get('search')

        if search_info:    
            category_list = Category.objects.filter(Q(name__icontains=search_info))
        else:    
            category_list = Category.objects.all()
        return render(request, self.template_name, {'category_list': category_list})

    

class InfoModulListView(ListView):
    template_name = 'math_modul/info_modul.html'

    def get(self, request, id):
        search_info = request.GET.get('search')
        info_list = Category.objects.filter(pk=id)

        if search_info:   
            info_list = Category.objects.filter(pk=id)
        else:    
            info_list = Category.objects.filter(pk=id)

        return render(request, self.template_name, context={'info_list':info_list})
    