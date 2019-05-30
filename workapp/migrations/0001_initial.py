# Generated by Django 2.2 on 2019-05-07 05:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateNotifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('candidate_skills', models.CharField(max_length=200, null=True)),
                ('candidate_location', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Candidate notification',
                'db_table': 'Candidate_notification',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('message', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='JobNotifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('job_skills', models.CharField(max_length=200, null=True)),
                ('job_location', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Job notification',
                'db_table': 'Job_notification',
            },
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('post_name', models.CharField(max_length=100, null=True)),
                ('experience', models.CharField(max_length=200, null=True)),
                ('package', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('skills', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Job Post',
                'db_table': 'Job_Post',
            },
        ),
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathername', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('zipcode', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('qualification', models.CharField(max_length=200, null=True)),
                ('experience', models.CharField(max_length=100, null=True)),
                ('skills', models.CharField(max_length=100, null=True)),
                ('certification', models.CharField(max_length=100, null=True)),
                ('language', models.CharField(max_length=200, null=True)),
                ('photo', models.FileField(blank=True, help_text='Upload only .png, .jpg & .jpeg image extension.', null=True, upload_to='image/userphoto')),
                ('resume', models.FileField(blank=True, help_text='Upload only .txt, .pdf & .word file extension.', null=True, upload_to='image/userresume')),
                ('user', models.OneToOneField(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Registration',
                'db_table': 'user_registration',
            },
        ),
        migrations.CreateModel(
            name='CompanyRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('jobpost', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('website', models.CharField(max_length=200, null=True)),
                ('address', models.TextField(max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Company Registration',
                'db_table': 'company_registration',
            },
        ),
    ]
