from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def index(request):
    # to render a template, the first parameter is always request
    #it's a django thing 
    return render(request, "index.html")

def people(request, name):
    # context is a django thing again for using variables in html
    #we use a dictionary as in "name we use in html": name we use in this file
    context = {
        "htmlname": name
    }
    return render(request, "hello_name.html", context)

def root_method(request):
    return HttpResponse("String response from root_method")
def another_method(request):
    return redirect("/redirected_route")
def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})
