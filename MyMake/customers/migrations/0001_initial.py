# Generated by Django 4.0.4 on 2022-04-13 23:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('total_spend', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
