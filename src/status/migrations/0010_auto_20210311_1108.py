# Generated by Django 3.0.2 on 2021-03-11 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('status', '0009_auto_20210311_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='reaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='frommaterial', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Like', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Like', to='status.Status')),
            ],
        ),
    ]
