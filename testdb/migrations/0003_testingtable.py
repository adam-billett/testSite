# Generated by Django 4.2.7 on 2023-11-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0002_rename_password_users_user_pass'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestingTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testVar', models.CharField(max_length=5)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
