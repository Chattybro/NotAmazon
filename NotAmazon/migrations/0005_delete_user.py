# Generated by Django 4.2.7 on 2024-03-14 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NotAmazon', '0004_alter_user_user_pass'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
