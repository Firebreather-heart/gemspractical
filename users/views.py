from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from .models import Profile
from gemadmin.models import Fee,fee_dict
from django.contrib import messages 
# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            cd = user_form.cleaned_data
            new_user.set_password(
                cd['password']
            )
            try:
                new_user.save()
            except Exception as e:
                print('exception!!!!')
                print(e)
                return messages.error(request, "Enter a unique username")
            prof = Profile(user=new_user,first_name=cd['first_name'], last_name=cd['last_name'], cls=cd['cls'], date_of_birth=cd['date_of_birth'], gender = cd['gender'])
            prof.save()
            schfee = Fee( student=new_user, amount = fee_dict.get(new_user.cls), desc = 'school fees')
            schfee.save()
            uniformfee = Fee(student = new_user, amount=2500, desc = "uniforms")
            uniformfee.save()
            cardiganfee = Fee(student = new_user, amount=1200, desc = "cardigan")
            cardiganfee.save()
            s_wear = Fee(student = new_user, amount=2500, desc = "sport wear")
            s_wear.save()
            f_wear = Fee(student = new_user, amount=2500, desc = "friday wear")
            f_wear.save()
            print(cd['gender'])
            if cd['gender'] == 'FM':
                hat = Fee(student = new_user, amount=1400, desc = "hat")
                hat.save()
            if cd.get('department') == 'SCI':
                lab_coat = Fee(student = new_user, amount=1200, desc = "lab coat")
                lab_coat.save()
            if cd['cls'] == 'J3':
                jwaec = Fee(student = new_user, amount=30000, desc = "junior waec")
                jwaec.save() 
            elif cd['cls'] == 'S3':
                s_waec = Fee(student = new_user, amount=40500, desc = "senior waec")
                s_waec.save()
                neco = Fee(student = new_user, amount=40500, desc = "neco")
                neco.save()

            return redirect('login')
    else:
        user_form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'user_form':user_form})