INSERT INTO produto (
    nome,
    descricao,
    preco,
    quantidade_estoque,
    categoria
)
VALUES (
    :nome,
    :descricao,
    :preco,
    :quantidade_estoque,
    :categoria
)
RETURNING *;
