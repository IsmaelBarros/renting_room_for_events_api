# Generated by Django 4.1 on 2022-08-25 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_room_user_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.event'),
        ),
    ]
