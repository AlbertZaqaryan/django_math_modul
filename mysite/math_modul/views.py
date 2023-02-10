from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
import io
import urllib, base64
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
            y.append((int(k) * int(i) + int(b)))
        res1 = X
        res2 = y
        f = plt.figure(figsize=(10, 6), dpi=300)
        plt.plot(res1, res2)
        res = plt.gcf()
        buf = io.BytesIO()
        res.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())
        uri = urllib.parse.quote(string)
        res = uri
        f.clear()
    return render(request, 'math_modul/graph.html', context={'data':res, 'res1':res1, 'res2':res2})