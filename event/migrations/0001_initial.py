# Generated by Django 3.2.8 on 2021-10-13 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('html', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=1000)),
                ('last_name', models.CharField(max_length=1000)),
                ('position', models.CharField(max_length=1000)),
                ('uid', models.IntegerField(default=0, unique=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studets', to='event.event')),
            ],
        ),
    ]