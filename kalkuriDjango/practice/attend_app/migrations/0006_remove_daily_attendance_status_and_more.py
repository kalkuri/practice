# Generated by Django 4.2.7 on 2023-12-20 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend_app', '0005_daily_attendance_alter_employee_date_of_join'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='daily_attendance',
            name='status',
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_join',
            field=models.DateField(default=datetime.date(2023, 12, 20)),
        ),
    ]