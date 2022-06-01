# Generated by Django 4.0.4 on 2022-06-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_user_first_name_alter_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_verified',
            field=models.BooleanField(default=True, help_text="Designates whether this user's email is verified. ", verbose_name='email verified'),
        ),
    ]