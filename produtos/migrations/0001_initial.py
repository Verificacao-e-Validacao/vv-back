# Generated by Django 3.2.12 on 2024-08-25 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('codigo', models.IntegerField(verbose_name='Código')),
                ('descricao', models.TextField(blank=True, help_text='Descrição do produto', null=True, verbose_name='Descrição')),
                ('peso', models.DecimalField(decimal_places=2, help_text='Peso do produto em quilogramas', max_digits=10)),
                ('valor_compra', models.DecimalField(decimal_places=2, help_text='Valor de compra do produto', max_digits=10)),
                ('valor_venda', models.DecimalField(decimal_places=2, help_text='Valor de venda do produto', max_digits=10)),
                ('quantidade', models.IntegerField(help_text='Quantidade disponível em estoque')),
                ('vencimento', models.DateField(help_text='Data de vencimento do produto')),
                ('detalhes', models.TextField(blank=True, help_text='Detalhes adicionais sobre o produto', null=True)),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
