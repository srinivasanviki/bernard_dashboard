from django.shortcuts import render

def render_dashboard_home(request):
    return render(request, "index.html", {})


def render_home(request):
    return render(request, "home.html", {})