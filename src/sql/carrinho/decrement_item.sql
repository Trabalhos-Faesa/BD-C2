WITH cart AS (
    SELECT id_carrinho
    FROM carrinho_de_compras
    WHERE id_carrinho = :id_carrinho AND status = 'aberto'
), curr AS (
    SELECT i.id_carrinho, i.id_produto, i.quantidade
    FROM itens_do_carrinho i
    WHERE i.id_carrinho = :id_carrinho AND i.id_produto = :id_produto
), updated AS (
    UPDATE itens_do_carrinho i
    SET quantidade = i.quantidade - :quantidade
    WHERE EXISTS (SELECT 1 FROM cart)
      AND i.id_carrinho = :id_carrinho AND i.id_produto = :id_produto
    RETURNING i.id_carrinho, i.id_produto, i.quantidade
), removed AS (
    DELETE FROM itens_do_carrinho i
    WHERE i.id_carrinho = :id_carrinho AND i.id_produto = :id_produto AND i.quantidade <= 0
    RETURNING :quantidade AS qtd_removida
), restock AS (
    UPDATE produto p
    SET quantidade_estoque = p.quantidade_estoque + :quantidade
    WHERE p.id_produto = :id_produto AND (EXISTS (SELECT 1 FROM updated) OR EXISTS (SELECT 1 FROM removed))
    RETURNING p.id_produto
)
SELECT COALESCE((SELECT quantidade FROM updated LIMIT 1), 0) AS quantidade_atual;