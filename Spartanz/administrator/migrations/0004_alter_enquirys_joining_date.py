# Generated by Django 3.2.5 on 2021-10-28 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_alter_member_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquirys',
            name='joining_date',
            field=models.DateTimeField(),
        ),
    ]
