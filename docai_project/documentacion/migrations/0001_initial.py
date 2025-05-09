# Generated by Django 5.2 on 2025-04-20 23:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artefacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('REQ', 'Requisitos'), ('CU', 'Casos de Uso'), ('PROT', 'Prototipos'), ('PLAN', 'Plan de Proyecto'), ('DOC', 'Documentación Técnica'), ('REP', 'Reporte de Progreso'), ('MAN', 'Manual de Usuario'), ('MANT', 'Documentación de Mantenimiento')], max_length=10)),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('generado_por_ia', models.BooleanField(default=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluacionCoherencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion_bleu', models.FloatField(blank=True, null=True)),
                ('puntuacion_rouge', models.FloatField(blank=True, null=True)),
                ('puntuacion_manual', models.IntegerField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True)),
                ('evaluado_en', models.DateTimeField(auto_now_add=True)),
                ('artefacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluaciones', to='documentacion.artefacto')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='artefacto',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artefactos', to='documentacion.project'),
        ),
    ]
