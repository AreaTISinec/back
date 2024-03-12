import json
import requests
from django.http import JsonResponse

def get_access_token(request):
    # Datos para la solicitud
    data = {
        'client_id': '4b10663a-043e-42b7-abd5-4b6a2f9db7a7',
        'scope': 'https://analysis.windows.net/powerbi/api/App.Read.All',
        'grant_type': 'password',
        'username': 'despinoza@sinecsa.onmicrosoft.com',
        'password': 'Sinec2024'
    }

    # Cabeceras para la solicitud
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Realizar la solicitud POST al endpoint de Microsoft
    response = requests.post('https://login.microsoftonline.com/a1ae3011-4801-490b-a107-9cd8ab6d5817/oauth2/v2.0/token', data=data, headers=headers)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Convertir la respuesta a un diccionario JSON
        response_data = response.json()
        # Devolver la respuesta al frontend
        return JsonResponse(response_data)
    else:
        # Si la solicitud falló, devolver un mensaje de error
        return JsonResponse({'error': 'Error al obtener el token de acceso'}, status=response.status_code)