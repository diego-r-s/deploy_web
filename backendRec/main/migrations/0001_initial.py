# Generated by Django 5.0.3 on 2024-06-11 21:48

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('customerName', models.CharField(max_length=100)),
                ('customerCNPJ', models.CharField(max_length=20)),
                ('sellerName', models.CharField(max_length=100)),
                ('sellerCNPJ', models.CharField(max_length=20)),
                ('totalValue', models.DecimalField(decimal_places=2, max_digits=10)),
                ('emissionDate', models.DateTimeField()),
                ('uploadDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=300)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('barCode', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('registrationNumber', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invoiceFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceItemInvoice', to='main.invoice')),
                ('productFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoiceItemProduct', to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categoryFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productCategoryFK', to='main.productcategory'),
        ),
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Pendent'), ('A', 'Approved'), ('R', 'Refused')], max_length=30)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('creationDate', models.DateTimeField(auto_now_add=True)),
                ('approverFK', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='approverWarrantyUser', to=settings.AUTH_USER_MODEL)),
                ('createdByFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdWarrantyUser', to=settings.AUTH_USER_MODEL)),
                ('items', models.ManyToManyField(to='main.invoiceitem')),
            ],
        ),
    ]
