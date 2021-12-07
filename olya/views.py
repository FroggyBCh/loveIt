from django.shortcuts import render

# Create your views here.
def first_page(request):
    return render(request, "first_page.html")
def second_page(request):
    return render(request, "second_page.html")