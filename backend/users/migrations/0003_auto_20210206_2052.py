# Generated by Django 3.1.5 on 2021-02-06 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210129_0706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='athlete',
            options={'ordering': ('created_at', 'updated_at', 'first_name', 'last_name', 'username', 'password', 'date_of_birth')},
        ),
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ('name', 'username', 'password')},
        ),
        migrations.DeleteModel(
            name='Relative',
        ),
    ]
