# Generated by Django 5.0.3 on 2024-06-11 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productfiles_fileread'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='ok', max_length=1000),
            preserve_default=False,
        ),
    ]
