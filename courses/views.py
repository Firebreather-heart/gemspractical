from django.shortcuts import render
from .models import Subject,Task 
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')