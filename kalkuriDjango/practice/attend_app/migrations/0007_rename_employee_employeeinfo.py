# Generated by Django 4.2.7 on 2023-12-20 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attend_app', '0006_remove_daily_attendance_status_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='EmployeeInfo',
        ),
    ]
