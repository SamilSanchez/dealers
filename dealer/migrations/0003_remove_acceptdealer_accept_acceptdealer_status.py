# Generated by Django 4.1 on 2022-08-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0002_alter_official_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acceptdealer',
            name='accept',
        ),
        migrations.AddField(
            model_name='acceptdealer',
            name='status',
            field=models.CharField(choices=[('in_revision', 'En revision'), ('accept', 'Aprobado'), ('reject', 'Rechazado')], default='in_revision', max_length=11),
        ),
    ]
