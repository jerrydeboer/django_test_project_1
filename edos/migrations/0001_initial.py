# Generated by Django 3.1.4 on 2020-12-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EdosTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dns_server_1', models.CharField(default='8.8.8.8', max_length=128)),
                ('dns_server_2', models.CharField(default='', max_length=128)),
                ('profile_rule_a', models.CharField(max_length=255)),
            ],
        ),
    ]
