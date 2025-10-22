WITH cart AS (
    SELECT id_carrinho
    FROM carrinho_de_compras
    WHERE id_carrinho = :id_carrinho AND status = 'aberto'
), item AS (
    SELECT quantidade
    FROM itens_do_carrinho
    WHERE id_carrinho = :id_carrinho AND id_produto = :id_produto
), delete_item AS (
    DELETE FROM itens_do_carrinho
    WHERE id_carrinho = :id_carrinho AND id_produto = :id_produto AND EXISTS (SELECT 1 FROM cart)
    RETURNING 1
), restock AS (
    UPDATE produto p
    SET quantidade_estoque = p.quantidade_estoque + COALESCE((SELECT quantidade FROM item), 0)
    WHERE p.id_produto = :id_produto AND EXISTS (SELECT 1 FROM delete_item)
    RETURNING p.id_produto
)
SELECT COALESCE((SELECT quantidade FROM item), 0) AS quantidade_estornada;