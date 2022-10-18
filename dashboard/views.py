from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from users.models import Profile
from users.forms import ProfileEditForm
from gemadmin.models import Fee,Payment

# Create your views here.
@login_required
def dashboard(request,):
    print(request.user.username)
    prof = Profile.objects.get(user = request.user,)
    schfee = Fee(student=request.user, desc='school fees')
    paid = schfee.paid()
    cont_dict = {
        'profile':prof,
        'paid':paid
    }
    return render(request,'dashboard.html', cont_dict)

@login_required
@permission_required('is_staff')
def admin_student_dashboard(request, id):
    prof = Profile.objects.get(user = request.user, id=id)
    schfee = Fee(student=request.user, desc='school fees')
    paid = schfee.paid()
    cont_dict = {
        'profile':prof,
        'paid':paid
    }
    return render(request,'dashboard.html', cont_dict)

@login_required
def changePic(request):
    if request.method == 'POST':
        new_pic = request.FILES['photo'] 
        print(new_pic)
        prof = Profile.objects.get(user=request.user)
        prof.photo = new_pic
        prof.save()
        return redirect('dashboard')
    return render(request, 'cap.html')

