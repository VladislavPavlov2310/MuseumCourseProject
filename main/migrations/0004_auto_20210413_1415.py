# Generated by Django 3.1.7 on 2021-04-13 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210409_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workpicture',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_pictures', to='main.work'),
        ),
    ]
