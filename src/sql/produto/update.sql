UPDATE produto
SET
    nome = :nome,
    descricao = :descricao,
    preco = :preco,
    quantidade_estoque = :quantidade_estoque,
    categoria = :categoria
WHERE id_produto = :id_produto
RETURNING *;
