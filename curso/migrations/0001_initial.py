# Generated by Django 4.2 on 2024-08-07 21:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplina', '0002_disciplina_delete_cadastro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('disciplina_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='disciplina.disciplina')),
                ('codigo1', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao1', models.CharField(max_length=200)),
            ],
            bases=('disciplina.disciplina',),
        ),
    ]
