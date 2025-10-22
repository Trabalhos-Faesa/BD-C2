DELETE
FROM cliente
WHERE id_cliente = :id_cliente
RETURNING *;
