# Generated by Django 4.2.4 on 2024-12-04 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]