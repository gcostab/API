# Generated by Django 4.2 on 2024-07-31 22:58

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='cadastro',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('codigo', models.CharField(max_length=8, unique=True)),
                ('descricao', models.CharField(max_length=200)),
                ('cargahoraria', models.CharField(max_length=3, unique=True)),
                ('ementa', models.CharField(max_length=50)),
                ('bibliografia', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
