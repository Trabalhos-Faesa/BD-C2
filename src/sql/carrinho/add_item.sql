WITH cart AS (
    SELECT id_carrinho
    FROM carrinho_de_compras
    WHERE id_carrinho = :id_carrinho AND status = 'aberto'
), produto_ok AS (
    SELECT p.id_produto
    FROM produto p
    WHERE p.id_produto = :id_produto
), estoque_ok AS (
    SELECT p.id_produto
    FROM produto p
    WHERE p.id_produto = :id_produto
      AND p.quantidade_estoque >= :quantidade
), upsert AS (
    INSERT INTO itens_do_carrinho (id_carrinho, id_produto, quantidade)
    SELECT :id_carrinho, :id_produto, :quantidade
    WHERE EXISTS (SELECT 1 FROM cart) AND EXISTS (SELECT 1 FROM estoque_ok)
    ON CONFLICT (id_carrinho, id_produto)
    DO UPDATE SET quantidade = itens_do_carrinho.quantidade + EXCLUDED.quantidade
    RETURNING id_carrinho, id_produto, quantidade
), debit AS (
    UPDATE produto p
    SET quantidade_estoque = p.quantidade_estoque - :quantidade
    WHERE p.id_produto = :id_produto AND EXISTS (SELECT 1 FROM upsert)
    RETURNING p.id_produto
)
SELECT u.id_carrinho, u.id_produto, u.quantidade
FROM upsert u;