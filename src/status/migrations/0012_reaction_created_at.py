# Generated by Django 3.0.2 on 2021-03-14 15:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0011_auto_20210311_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]