from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Exoplanet

def home(request):
    return render(request, 'exoplanets/index.html')

# Create your views here.

@csrf_exempt
def create_exoplanet(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            exoplanet = Exoplanet.objects.create(
                name=data['name'],
                type=data.get('type', 'other'),  # Default to 'other' if not specified
                distance=data['distance'],
                discovery_year=data['discovery_year'],
                description=data.get('description', ''),  # Empty string if not provided
                image_url=data.get('image_url', '')  # Empty string if not provided
            )
            return JsonResponse({
                'message': 'Exoplanet created successfully',
                'id': exoplanet.id,
                'name': exoplanet.name
            }, status=201)
        except KeyError as e:
            return JsonResponse({'error': f'Missing required field: {str(e)}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

def read_exoplanets(request):
    if request.method == 'GET':
        exoplanets = Exoplanet.objects.all().values(
            'id', 'name', 'type', 'distance', 
            'discovery_year', 'description', 'image_url',
            'created_at', 'updated_at'
        )
        return JsonResponse(list(exoplanets), safe=False)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def update_exoplanet(request, pk):
    if request.method in ['PUT', 'PATCH']:
        try:
            exoplanet = get_object_or_404(Exoplanet, pk=pk)
            data = json.loads(request.body)
            
            # Update fields if they exist in the request
            if 'name' in data:
                exoplanet.name = data['name']
            if 'type' in data:
                exoplanet.type = data['type']
            if 'distance' in data:
                exoplanet.distance = data['distance']
            if 'discovery_year' in data:
                exoplanet.discovery_year = data['discovery_year']
            if 'description' in data:
                exoplanet.description = data['description']
            if 'image_url' in data:
                exoplanet.image_url = data['image_url']
            
            exoplanet.save()
            return JsonResponse({
                'message': 'Exoplanet updated successfully',
                'id': exoplanet.id,
                'name': exoplanet.name
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def delete_exoplanet(request, pk):
    if request.method == 'DELETE':
        try:
            exoplanet = get_object_or_404(Exoplanet, pk=pk)
            exoplanet_name = exoplanet.name
            exoplanet.delete()
            return JsonResponse({
                'message': f'Exoplanet {exoplanet_name} deleted successfully'
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
