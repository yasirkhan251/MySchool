# Generated by Django 5.0.4 on 2024-05-10 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_student_sats_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(max_length=15),
        ),
    ]