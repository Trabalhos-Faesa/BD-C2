DELETE
FROM produto
WHERE id_produto = :id_produto
RETURNING *;
