# Generated by Django 4.2.7 on 2024-02-20 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend_app', '0011_employeeinfo_video_alter_employeeinfo_date_of_join_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='date_of_join',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
