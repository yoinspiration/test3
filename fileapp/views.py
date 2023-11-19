from django.http import JsonResponse
from django.shortcuts import render
from .models import File

def upload_file(request):
    if request.method == 'POST':
        file_model = File(file=request.FILES['file'])
        file_model.save()
        return JsonResponse({'message': 'File uploaded successfully'})

# Create your views here.
def home(request):
    return render(request, "home.html")