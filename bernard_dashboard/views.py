from django.shortcuts import render,render_to_response

from django.views.decorators.csrf import csrf_exempt


def render_dashboard_home(request):
    return render(request, "index.html", {})


def render_home(request):
    return render(request, "home.html", {})

@csrf_exempt
def render_urdf(request):
    return render(request,"controls.html",{})

def render_ros(request):
    return render(request, "ros.html", {})



