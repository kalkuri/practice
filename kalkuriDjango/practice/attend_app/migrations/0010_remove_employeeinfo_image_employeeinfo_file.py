# Generated by Django 4.2.7 on 2023-12-21 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend_app', '0009_employeeinfo_image_alter_employeeinfo_date_of_join'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeinfo',
            name='image',
        ),
        migrations.AddField(
            model_name='employeeinfo',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
