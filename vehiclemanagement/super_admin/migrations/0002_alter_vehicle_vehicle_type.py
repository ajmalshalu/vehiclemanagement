# Generated by Django 4.2.4 on 2023-08-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('Two Wheeler', 'Two Wheeler'), ('Three Wheeler', 'Three Wheeler'), ('Four Wheeler', 'Four Wheeler')], default='Two Wheeler', max_length=50),
        ),
    ]
