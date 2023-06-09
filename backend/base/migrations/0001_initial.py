# Generated by Django 4.2.1 on 2023-05-20 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_personal_user', models.BooleanField(default=False)),
                ('is_business_user', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('otp', models.IntegerField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=30, null=True)),
                ('your_title', models.CharField(blank=True, max_length=30, null=True)),
                ('business_started_in', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('crew_size', models.CharField(blank=True, max_length=30, null=True)),
                ('category', models.CharField(blank=True, choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')], max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('zip', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetroArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')], max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personal_contact_info', to='base.contactinfo')),
                ('metro_area', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personal_metro_area', to='base.metroarea')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='personal_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_company_info', to='base.companyinfo')),
                ('contact_info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_contact_info', to='base.contactinfo')),
                ('metro_area', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business_metro_area', to='base.metroarea')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='business_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
