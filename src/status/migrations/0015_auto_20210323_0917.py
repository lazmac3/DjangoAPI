# Generated by Django 3.0.2 on 2021-03-23 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('status', '0014_auto_20210322_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='Like',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Like', to='status.Status'),
        ),
        migrations.AlterField(
            model_name='reaction',
            name='reaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frommaterial', to=settings.AUTH_USER_MODEL),
        ),
    ]