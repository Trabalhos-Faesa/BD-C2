INSERT INTO cliente (
    email,
    senha,
    nome,
    sobrenome,
    cpf,
    cep,
    uf,
    cidade,
    bairro,
    rua,
    numero,
    complemento
)
VALUES (
    :email,
    :senha,
    :nome,
    :sobrenome,
    :cpf,
    :cep,
    :uf,
    :cidade,
    :bairro,
    :rua,
    :numero,
    :complemento
)
RETURNING *;
