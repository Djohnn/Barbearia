# Generated by Django 5.0.6 on 2024-07-05 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_users_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='cargo',
            field=models.CharField(choices=[('V', 'Vendedor'), ('G', 'Gerente'), ('C', 'Caixa'), ('CL', 'Cliente'), ('B', 'Barbeiro')], default='CL', max_length=2),
        ),
    ]
