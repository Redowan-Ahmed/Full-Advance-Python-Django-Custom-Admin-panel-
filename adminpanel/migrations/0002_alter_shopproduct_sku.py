# Generated by Django 4.2.3 on 2023-07-15 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='sku',
            field=models.CharField(blank=True, default='0', max_length=200, unique=True),
        ),
    ]
