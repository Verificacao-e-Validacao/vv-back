from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Venda

@receiver(pre_save, sender=Venda)
def verificar_estoque_antes_venda(sender, instance, **kwargs):

    produto = instance.produto
    quantidade_estoque = produto.total_estoque
    estoque_produto = produto.movimentacoes_estoque.all()
    quantidade_venda = instance.quantidade_venda

    for estoque in estoque_produto:
        if estoque.quantidade > quantidade_venda:
            estoque.quantidade -= quantidade_venda
            quantidade_venda = 0
            estoque.save()
            break
        elif estoque.quantidade == quantidade_venda:
            estoque.delete()
            quantidade_venda = 0
            break
        else:
            quantidade_venda -= estoque.quantidade
            estoque.delete()

    if quantidade_venda:
        raise ValueError(f"Estoque insuficiente para {produto.nome}. Disponível: {quantidade_estoque}, Solicitado: {instance.quantidade_venda}")
