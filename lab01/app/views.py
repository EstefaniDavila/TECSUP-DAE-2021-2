from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Saludos desde la vista app")

def suma(request,num1,num2):
    op1 = int(num1)
    op2 = int(num2)
    html = "<html><body>La suma de los numeros es: %s </body></html>" % (op1+op2)
    return HttpResponse(html)

def resta(request,num1,num2):
    op1 = int(num1)
    op2 = int(num2)
    html = "<html><body>La resta de los numeros es: %s </body></html>" % (op1-op2)
    return HttpResponse(html)

def multiplicacion(request,num1,num2):
    op1 = int(num1)
    op2 = int(num2)
    html = "<html><body>El resultado de la multliplicación es: %s </body></html>" % (op1*op2)
    return HttpResponse(html)