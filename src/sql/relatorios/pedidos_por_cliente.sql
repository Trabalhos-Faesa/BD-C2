WITH pedidos AS (
    SELECT
        p.id_pedido,
        p.id_cliente,
        p.data_pedido,
        p.status,
        p.id_carrinho,
        p.valorTotal::numeric(10,2) AS valor_total
    FROM pedido p
    WHERE p.id_cliente = $1
    ORDER BY p.data_pedido DESC
), itens AS (
    SELECT
        ic.id_item_carrinho,
        ic.id_carrinho,
        ic.id_produto,
        pr.nome AS nome_produto,
        ic.quantidade,
        ic.preco_unitario::numeric(10,2) AS preco_unitario
    FROM item_carrinho ic
    LEFT JOIN produto pr ON pr.id_produto = ic.id_produto
)
SELECT
    json_build_object(
        'id_pedido', pd.id_pedido,
        'data_pedido', to_char(pd.data_pedido, 'YYYY-MM-DD"T"HH24:MI:SS"Z"'),
        'status', pd.status,
        'id_carrinho', pd.id_carrinho,
        'valor_total', pd.valor_total,
        'itens', (
            SELECT json_agg(json_build_object(
                'id_item_carrinho', it.id_item_carrinho,
                'id_produto', it.id_produto,
                'nome_produto', it.nome_produto,
                'quantidade', it.quantidade,
                'preco_unitario', it.preco_unitario
            ))
            FROM itens it
            WHERE it.id_carrinho = pd.id_carrinho
        )
    ) AS pedido
FROM pedidos pd;
