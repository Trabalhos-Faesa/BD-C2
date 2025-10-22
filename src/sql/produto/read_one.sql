SELECT id_produto, nome, descricao, preco, quantidade_estoque, categoria, data_criacao
FROM produto
WHERE id_produto = :id_produto;