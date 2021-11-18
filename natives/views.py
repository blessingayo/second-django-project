from django.shortcuts import render


# Create your views here.

def create_native(request):
    return render(request, "create_native.html")


def get_natives(request):
    return render(request, "get_natives.html")


def get_native(request):
    return render(request, "get_native.html")


def update_native(request):
    return render(request, "update_native.html")


def delete_native(request):
    return render(request, "delete_native.html")
