# Generated by Django 3.2.8 on 2021-10-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]