# Generated by Django 3.2.8 on 2022-10-05 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gemadmin', '0005_alter_payment_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='fee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fee', to='gemadmin.fee'),
        ),
    ]
