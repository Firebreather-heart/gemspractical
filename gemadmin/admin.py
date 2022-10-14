from django.contrib import admin
from .models import Fee ,Payment
from users.models import Profile,CustomUser
# Register your models here.

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ['get_name', 'desc','amount', 'paid','balance', 'term',]

class UserInline(admin.TabularInline):
    model = Profile
    extra = 0

class FeeInline(admin.TabularInline):
    model = Fee 
    extra = 0

class PaymentInline(admin.TabularInline):
    model = Payment 
    extra = 0

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name', 'gender','date_of_birth', 'cls']
    list_filter = ['cls','gender']
    inlines = [ UserInline, FeeInline, PaymentInline  ]

admin.site.register(CustomUser, StudentAdmin)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['student', 'desc', 'value', 'payment_date']
    list_filter = ['payment_date']