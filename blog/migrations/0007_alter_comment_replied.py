# Generated by Django 4.2.3 on 2023-07-16 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_category_options_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='replied',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replied_comment', to='blog.comment'),
        ),
    ]
