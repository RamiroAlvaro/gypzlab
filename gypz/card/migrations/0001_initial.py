# Generated by Django 3.1.4 on 2020-12-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('credit', models.FloatField()),
                ('solicitation_status', models.BooleanField(default=False)),
            ],
        ),
    ]