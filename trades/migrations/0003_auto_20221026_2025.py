# Generated by Django 3.2.16 on 2022-10-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0002_trade_balance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trade',
            old_name='title',
            new_name='strategy',
        ),
        migrations.AddField(
            model_name='trade',
            name='image_link',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='trade',
            name='notes',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='trade',
            name='profit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trade',
            name='win_loss',
            field=models.CharField(default='Win', max_length=255),
        ),
    ]
