# Generated by Django 3.0.6 on 2020-11-25 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employ', '0004_employee_employer'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='employer',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Employ.Employer'),
            preserve_default=False,
        ),
    ]