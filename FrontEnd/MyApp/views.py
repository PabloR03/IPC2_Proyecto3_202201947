from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests

def myform_view(request):
    return render(request, 'myform.html')

def consulta_hashtag(request):
    try:
        response = requests.get('http://127.0.0.1:5000/consulta/Hashtag')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)

def consulta_menciones(request):
    try:
        response = requests.get('http://127.0.0.1:5000/consulta/Menciones')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)

def consulta_sentimiento(request):
    try:
        response = requests.get('http://127.0.0.1:5000/consulta/Sentimiento')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)
    
def grafica_hashtag(request):
    try:
        response = requests.get('http://127.0.0.1:5000/grafica/Hashtag')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)

def grafica_menciones(request):
    try:
        response = requests.get('http://127.0.0.1:5000/grafica/Menciones')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)

def grafica_sentimiento(request):
    try:
        response = requests.get('http://127.0.0.1:5000/grafica/Sentimientos')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)
    
def datos_estudiante(request):
    try:
        response = requests.get('http://127.0.0.1:5000/informacion/Estudiante')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)