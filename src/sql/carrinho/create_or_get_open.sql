WITH existing AS (
    SELECT id_carrinho
    FROM carrinho_de_compras
    WHERE id_cliente = :id_cliente AND status = 'aberto'
    LIMIT 1
), created AS (
    INSERT INTO carrinho_de_compras (id_cliente, data_criacao, status)
    SELECT :id_cliente, NOW(), 'aberto'
    WHERE NOT EXISTS (SELECT 1 FROM existing)
    RETURNING id_carrinho
)
SELECT id_carrinho
FROM created
UNION ALL
SELECT id_carrinho
FROM existing
LIMIT 1;