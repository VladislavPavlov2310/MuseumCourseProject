# Generated by Django 3.1.7 on 2021-04-09 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.collection'),
        ),
        migrations.AlterField(
            model_name='work',
            name='exhibition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.exhibition'),
        ),
    ]