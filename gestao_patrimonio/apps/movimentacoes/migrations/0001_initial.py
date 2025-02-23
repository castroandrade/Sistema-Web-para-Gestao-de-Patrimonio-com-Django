# Generated by Django 5.1.6 on 2025-02-21 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamentos', '0001_initial'),
        ('patrimonio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_anterior', models.CharField(max_length=50, verbose_name='Status Anterior')),
                ('status_atual', models.CharField(max_length=50, verbose_name='Status Atual')),
                ('alterado_por', models.CharField(max_length=255, verbose_name='Usuário que Alterou')),
                ('data_alteracao', models.DateTimeField(auto_now_add=True, verbose_name='Data da Alteração')),
                ('bem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.bem', verbose_name='Bem')),
            ],
            options={
                'verbose_name': 'Histórico de Status',
                'verbose_name_plural': 'Histórico de Status',
            },
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsavel', models.CharField(max_length=255, verbose_name='Responsável pela Movimentação')),
                ('data_movimentacao', models.DateTimeField(auto_now_add=True, verbose_name='Data da Movimentação')),
                ('bem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.bem', verbose_name='Bem Movimentado')),
                ('destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destino', to='departamentos.departamento', verbose_name='Departamento de Destino')),
                ('origem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origem', to='departamentos.departamento', verbose_name='Departamento de Origem')),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
            },
        ),
    ]
