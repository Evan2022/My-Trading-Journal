# Generated by Django 3.2.16 on 2022-10-26 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0003_auto_20221026_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='win_loss',
            new_name='win_or_loss',
        ),
    ]
