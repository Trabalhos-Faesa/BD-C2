UPDATE cliente
SET
  email = :email,
  senha = :senha,
  nome = :nome,
  sobrenome = :sobrenome,
  cpf = :cpf,
  cep = :cep,
  uf = :uf,
  cidade = :cidade,
  bairro = :bairro,
  rua = :rua,
  numero = :numero,
  complemento = :complemento
WHERE id_cliente = :id_cliente
RETURNING *;
