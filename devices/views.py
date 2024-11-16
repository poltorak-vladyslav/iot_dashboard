from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
from .models import DeviceData

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            DeviceData.objects.create(
                device_id=data['device_id'],
                temperature=data['temperature'],
                humidity=data['humidity']
            )
            return JsonResponse({'status': 'success'}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'invalid method'}, status=405)

def dashboard(request):
    data = DeviceData.objects.all().order_by('-timestamp')[:50]
    return render(request, 'devices/dashboard.html', {'data': data})