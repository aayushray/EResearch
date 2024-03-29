# Generated by Django 4.0.3 on 2022-04-04 09:55

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prof_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_institute', models.CharField(blank=True, default='', max_length=200)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('expertise_area', models.CharField(blank=True, default='', max_length=100)),
                ('active_internships', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Research_Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(blank=True, default='', max_length=100)),
                ('research_statement', models.TextField(blank=True, default='', max_length=700)),
                ('start_date', models.DateField(blank=True, default='')),
                ('end_date', models.DateField(blank=True, default='')),
                ('domain', models.CharField(blank=True, default='', max_length=100)),
                ('prof_name', models.CharField(blank=True, default='', max_length=150)),
                ('stipend', models.CharField(blank=True, default='', max_length=50)),
                ('location', models.CharField(blank=True, default='', max_length=100)),
                ('applied_numbers', models.CharField(blank=True, default='', max_length=50)),
                ('status', models.BooleanField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Student_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank=True, default='', max_length=200)),
                ('age', models.IntegerField(blank=True, default=0, max_length=5)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='1', max_length=20)),
                ('student_institute', models.CharField(blank=True, default='', max_length=200)),
                ('student_email', models.EmailField(blank=True, default='', max_length=254)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('institute_email', models.EmailField(blank=True, default='', max_length=254)),
            ],
        ),
    ]
