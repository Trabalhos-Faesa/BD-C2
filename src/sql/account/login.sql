-- Busca cliente por email e senha para autenticação
SELECT
    id_cliente,
    email,
    senha,
    nome,
    sobrenome,
    cpf
FROM cliente
WHERE email = :email
LIMIT 1;
