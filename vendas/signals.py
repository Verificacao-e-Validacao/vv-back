from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import ItemVenda

@receiver(pre_save, sender=ItemVenda)
def verificar_estoque_antes_venda(sender, instance, **kwargs):

    produto = instance.produto
    quantidade_estoque = produto.total_estoque
    estoque_produto = produto.movimentacoes_estoque.all()
    quantidade_venda = instance.quantidade

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
        raise ValueError(f"Estoque insuficiente para {produto.nome}. Disponível: {quantidade_estoque}, Solicitado: {instance.quantidade}")


def handle_venda_changes(instance, **kwargs):
    venda = instance.venda
    valor_total_venda = 0
    for item in venda.itens.all():
        valor_total_venda += (item.valor_unitario * item.quantidade)

    venda.valor_total = valor_total_venda
    venda.save()

@receiver(post_save, sender=ItemVenda)
def define_valor_total_post_save(sender, instance, **kwargs):
    handle_venda_changes(instance, **kwargs)

@receiver(post_delete, sender=ItemVenda)
def define_valor_total_post_delete(sender, instance, **kwargs):
    handle_venda_changes(instance, **kwargs)