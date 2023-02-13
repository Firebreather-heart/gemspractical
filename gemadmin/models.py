from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404
# Create your models here.
fee_dict = dict((('J1',10000), ('J2',12000), ('J3', 14000), ('S1',16000), ('S2',18000), ('S3', 20000)))

class PaidSchFeeManager(models.Manager):
    def get_queryset(self):
        return super(PaidSchFeeManager, self).get_queryset().filter(paid=True, desc='school fees')

class UnpaidSchFeeManager(models.Manager):
    def get_queryset(self) :
        return super(UnpaidSchFeeManager, self).get_queryset().filter(paid=False, desc='uniforms')


class Fee(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_fee')
    desc = models.CharField(max_length=30, choices=(('school fees', 'SCH FEES'),
                                                     ('uniforms','UNIFORM'),
                                                     ('sport wear','SPORTWEAR'),
                                                     ('friday wear', 'FRIDAYWEAR'),
                                                     ('lab coat','LABCOAT'),
                                                     ('cardigan', 'CARDIGAN'),
                                                     ('hat', 'HAT'),
                                                     ('junior waec','JWAEC'),
                                                     ('senior waec', 'SSCE'),
                                                     ('neco','NECO') ), 
                                                     default='school fees')

    TERM_CHOICES = (('F','first'), ('S','second'), ('T','third'))
    amount = models.PositiveIntegerField(default=17000)
    term = models.CharField(max_length=10, choices = TERM_CHOICES, default='')
    amount_paid = models.PositiveIntegerField(default=0)
    #paid = models.BooleanField(default=False)
    objects = models.Manager()
    schfeespaid = PaidSchFeeManager()
    schfees_notpaid = UnpaidSchFeeManager()

    def __str__(self):
        return f"{self.desc}"
    
    
    def balance(self):
        return self.amount - self.amount_paid

    def paid(self):
        if self.balance() == 0:
            return 'Paid'
        else:
            if self.amount_paid == 0:
                return "No payment"
            else: 
                return f'Incomplete Payment ({self.amount_paid})'
    
    def get_name(self):
        return f"{self.student.first_name} {self.student.last_name}"
    
    def save(self,*args, **kwargs) -> None:
        if self.amount == self.amount_paid:
            self.paid =True 
        if self.amount < self.amount_paid:
            raise ValueError("you must have made a mistake, cross check your entry")
        return super().save(*args, **kwargs)
    
class Payment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student', db_index=True)
    description = models.CharField(max_length=30, choices=(('school fees', 'SCH FEES'),
                                                     ('uniforms','UNIFORM'),
                                                     ('sport wear','SPORTWEAR'),
                                                     ('friday wear', 'FRIDAYWEAR'),
                                                     ('lab coat','LABCOAT'),
                                                     ('cardigan', 'CARDIGAN'),
                                                     ('hat', 'HAT'),
                                                     ('junior waec','JWAEC'),
                                                     ('senior waec', 'SSCE'),
                                                     ('neco','NECO') ), 
                                                     default='school fees')
    payment_date = models.DateTimeField(auto_now_add=True, db_index=True)
    amount = models.PositiveIntegerField(default=0)
   
    
    def __str__(self):
        return f"Payment made by {self.student.first_name} {self.student.last_name} for {self.description} on {self.payment_date}"
    
    def value(self):
        return self.amount
    
    def desc(self):
        return self.description
    
    def save(self, *args, **kwargs):
        fee = get_object_or_404(Fee, student = self.student, desc = self.description )
        assert self.amount <= fee.balance()
        fee.amount_paid += self.amount 
        fee.save()
        print(f"\n\n\n\n\npaid fee today, {fee.amount_paid}, bal-{fee.balance()}\n\n\n\n\n\n")
        return super().save(*args, **kwargs)
    
    def get_queryset(self):
        objs =  self.objects.order_by('payment_date')
        return objs


class WeeklyIncome(models.Model):
    total_income = models.PositiveIntegerField(default=0)
    weekname = models.CharField(max_length=100)