# Generated by Django 3.2.5 on 2021-10-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0009_enquirys_timming'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquirys',
            name='visit_type',
            field=models.CharField(blank=True, choices=[('c', 'Call'), ('d', 'Directly')], max_length=1),
        ),
    ]