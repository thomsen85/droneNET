from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Drone

# Create your views here.
def drone(request, id):
    obj, created = Drone.objects.get_or_create(name=id)
    print(created)
    if not created:
        obj.x_pos = request.GET.get('x', 0)
        obj.y_pos = request.GET.get('y', 0)
        obj.speed = request.GET.get('speed', 0)
        obj.altimeter = request.GET.get('alt', 0)
        obj.save()
    return HttpResponse("200")

def drone_data(request, id):
    response = {}
    try:
        obj = Drone.objects.get(name=id)
        response["name"] = obj.name
        response["x_pos"] = obj.x_pos
        response["y_pos"] = obj.y_pos
        response["speed"] = obj.speed
        response["altimeter"] = obj.altimeter
        response["task"] = obj.task
    except:
        print(f"no drone called: {id}")

    return JsonResponse(response)

def overview(request):
    context = None
    return render(request, "dashboard/overview.html", context)

def s_map(request):
    return render(request, "map/map.html")