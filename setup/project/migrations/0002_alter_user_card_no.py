# Generated by Django 4.0.4 on 2022-05-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='card_no',
            field=models.CharField(max_length=20, unique=True, verbose_name='card_no'),
        ),
    ]
