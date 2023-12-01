from django.shortcuts import render

# Create your views here.
def bootstrap_generic(request):
    return render(request,'bootstrap_generic.html')