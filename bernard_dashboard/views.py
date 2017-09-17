from django.shortcuts import render

def render_dashboard_home(request):
    return render(request, "index.html", {})


def render_home(request):
    return render(request, "home.html", {})

def render_urdf(request):
        return render(request, "controls.html", {})

def render_ros(request):
    return render(request, "ros.html", {})