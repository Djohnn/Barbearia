# Generated by Django 5.0.6 on 2024-07-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='codigo_barras',
            field=models.CharField(default='0000000000000', max_length=13, unique=True),
        ),
    ]