# Generated by Django 4.0.2 on 2022-03-14 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_category_sabt_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='sabt',
            name='author',
            field=models.ForeignKey(default=1 , on_delete=django.db.models.deletion.CASCADE, related_name='sabts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
