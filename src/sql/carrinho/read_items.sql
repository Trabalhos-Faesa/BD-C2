WITH itens AS (
    SELECT i.id_carrinho, i.id_produto, i.quantidade, p.nome AS nome_produto, p.preco,
           (i.quantidade * p.preco) AS subtotal
    FROM itens_do_carrinho i
    JOIN produto p ON p.id_produto = i.id_produto
    WHERE i.id_carrinho = :id_carrinho
)
SELECT *, (SELECT COALESCE(SUM(subtotal), 0) FROM itens) AS total
FROM itens
ORDER BY id_produto;