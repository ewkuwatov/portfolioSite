# Generated by Django 4.2.3 on 2023-08-16 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='urls_linkedn',
            new_name='urls_linkedin',
        ),
    ]