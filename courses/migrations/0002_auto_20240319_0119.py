# Generated by Django 3.2.24 on 2024-03-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='id',
        ),
        migrations.AddField(
            model_name='module',
            name='module_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='module',
            name='module_name',
            field=models.CharField(max_length=100),
        ),
    ]
