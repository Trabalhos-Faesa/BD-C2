WITH cart AS (
    SELECT id_carrinho, id_cliente
    FROM carrinho_de_compras
    WHERE id_carrinho = :id_carrinho AND status = 'aberto'
), total AS (
    SELECT SUM(i.quantidade * p.preco) AS valor_total
    FROM itens_do_carrinho i
    JOIN produto p ON p.id_produto = i.id_produto
    WHERE i.id_carrinho = :id_carrinho
), has_items AS (
     SELECT 1 AS ok FROM itens_do_carrinho WHERE id_carrinho = :id_carrinho LIMIT 1
), close_cart AS (
    UPDATE carrinho_de_compras c
    SET status = 'fechado'
     WHERE c.id_carrinho = :id_carrinho AND EXISTS (SELECT 1 FROM cart) AND EXISTS (SELECT 1 FROM has_items)
    RETURNING c.id_carrinho
), pedido AS (
    INSERT INTO pedido (id_cliente, data_pedido, valor_total, status, id_carrinho)
     SELECT c.id_cliente, NOW(), t.valor_total, 'confirmado', c.id_carrinho
     FROM cart c JOIN total t ON TRUE
     WHERE EXISTS (SELECT 1 FROM close_cart) AND t.valor_total IS NOT NULL
    RETURNING id_pedido, id_cliente, data_pedido, valor_total, status, id_carrinho
)
SELECT * FROM pedido;