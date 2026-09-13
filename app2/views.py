from django.shortcuts import render

# Create your views here.
def vista_tres(request):
    return render(request, 'app2/vista3.html')

def vista_cuatro(request):
    return render(request, 'app2/vista4.html')