# Generated by Django 4.2.1 on 2023-06-06 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authapp', '0026_user_enrollment_biceps_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='FullName',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
