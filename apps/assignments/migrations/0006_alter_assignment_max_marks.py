# Generated by Django 3.2.6 on 2021-08-24 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0005_rename_name_assignment_assignment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='max_marks',
            field=models.DecimalField(decimal_places=1, max_digits=19),
        ),
    ]
