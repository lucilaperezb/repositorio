from django.shortcuts import render

app_name = "clientes"

def index(request):
    return render(request, 'clientes/index.html')