# Generated by Django 4.2.7 on 2024-02-29 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NotAmazon', '0003_rename_user_emailk_user_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_pass',
            field=models.CharField(max_length=50),
        ),
    ]
