# Generated by Django 2.1.2 on 2018-10-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_4', '0008_remove_teacher_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='teachers',
            field=models.ManyToManyField(related_name='subjects', to='lab_4.Teacher'),
        ),
    ]
