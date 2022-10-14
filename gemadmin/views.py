from django.shortcuts import render, get_object_or_404, redirect
from .models import Fee,Payment 
from users.models import CustomUser,Profile
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def make_payments(request, student_id):
    if request.method =='POST':
        student = get_object_or_404(CustomUser, id=student_id )
        student_fees = student.fee.all()
    return render(request,)


@login_required
@permission_required('is_staff')
def index(request):
    profiles = Profile.objects.all()
    ctx = {
        'prof':profiles
    }
    return render(request, 'gemadmin.html', ctx)

@login_required
@permission_required('is_staff')
def adminchangePic(request, user):
    if request.method == 'POST':
        new_pic = request.FILES['photo'] 
        print(new_pic)
        prof = Profile.objects.get(user = user)
        prof.photo = new_pic
        prof.save()
        return redirect('gemadmin')
    return render(request, 'cap.html')

@login_required
@permission_required('is_staff')
def search(request):
    if request.method == 'GET':
        print('\n searching.............\n')
        name = request.GET.get('student-name')
        class__ = request.GET.get('q')

        if name is not None:
            lookup = Q(first_name__icontains=name) | Q(last_name__icontains = name)
            profile = Profile.objects.filter(lookup).distinct()
            ctx = {'profile': profile} 
            return render(request, 'search.html', ctx) 

        if class__ is not None:
            lookup = Q(first_name__icontains= class__) | Q(last_name__icontains = class__)
            profile = Profile.objects.filter(lookup).distinct()
            ctx = {'profile': profile} 
            return render(request, 'search.html', ctx)
    return render(request, 'search.html')
        