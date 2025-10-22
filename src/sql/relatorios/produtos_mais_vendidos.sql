SELECT TOP 50
    p.id_produto,
    p.nome,
    SUM(ic.quantidade) AS total_vendido
FROM item_carrinho ic
JOIN produto p ON p.id_produto = ic.id_produto
JOIN carrinho c ON c.id_carrinho = ic.id_carrinho
JOIN pedido ped ON ped.id_pedido = c.id_pedido
GROUP BY p.id_produto, p.nome
ORDER BY total_vendido DESC;
