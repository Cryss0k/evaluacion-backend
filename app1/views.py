from django.shortcuts import render

# Create your views here.
def vista_uno(request):
    return render(request, 'app1/vista1.html')

def vista_dos(request):
    return render(request, 'app1/vista2.html')