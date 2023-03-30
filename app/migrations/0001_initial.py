# Generated by Django 4.1.7 on 2023-03-30 04:55

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
                ('c_code', models.IntegerField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=100)),
                ('c_population', models.IntegerField()),
                ('c_king', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Capital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_capital', models.CharField(max_length=100)),
                ('c_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
        ),
    ]
