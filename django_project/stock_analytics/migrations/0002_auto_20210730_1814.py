# Generated by Django 3.1.7 on 2021-07-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.CharField(max_length=100),
        ),
    ]