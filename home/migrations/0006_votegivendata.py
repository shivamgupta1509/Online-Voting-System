# Generated by Django 3.1.7 on 2021-04-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210413_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteGivenData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_name', models.CharField(max_length=122)),
                ('voter_ID', models.CharField(max_length=122)),
            ],
        ),
    ]
