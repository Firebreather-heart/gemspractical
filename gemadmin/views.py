from django.shortcuts import render, get_object_or_404, redirect
from .models import Fee,Payment 
from users.models import CustomUser,Profile
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
# Create your views here.

@login_required
@permission_required('is_staff', raise_exception=True)
def make_payments(request, id):
    user = get_object_or_404(CustomUser, id=id)
    if request.method =='POST':
        print('starting payment')
        desc = request.POST.get('desc')
        amount_paid = request.POST.get('amount_paid')
        user_id = request.POST.get('user_who')
        user = Profile.objects.get(id = user_id).user
        amount_paid = int(amount_paid)
        try:
            payment = Payment(student = user, description = desc, amount = amount_paid, )
            print(payment)
            payment.save()
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, 'Payment Not Successful')
        else:
            messages.add_message(request, messages.SUCCESS, 'Payment Successful')

    return redirect('gemadmin')


@login_required
@permission_required('is_staff', raise_exception=True)
def index(request):
    
    profiles = Profile.objects.all()
    ctx = {
        'prof':profiles
    }
    return render(request, 'gemadmin.html', ctx)

@login_required
@permission_required('is_staff', raise_exception=True)
def get_student_by_class(request, arg):
    profiles = Profile.objects.filter(cls = arg)
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
            ctx = {'prof': profile} 
            return render(request, 'gemadmin.html', ctx) 

        if class__ is not None:
            lookup = Q(first_name__icontains= class__) | Q(last_name__icontains = class__)
            profile = Profile.objects.filter(lookup).distinct()
            ctx = {'prof': profile} 
            return render(request, 'gemadmin.html', ctx)
    return render(request, 'gemadmin.html')
        