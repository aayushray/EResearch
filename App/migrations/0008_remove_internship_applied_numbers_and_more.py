# Generated by Django 4.0.3 on 2022-04-05 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_professor_user_alter_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship',
            name='applied_numbers',
        ),
        migrations.AlterField(
            model_name='internship',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]