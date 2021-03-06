# Generated by Django 3.0.8 on 2020-07-13 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=75)),
                ('region', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=75)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='region.Country')),
            ],
        ),
    ]
