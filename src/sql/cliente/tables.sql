CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    cep VARCHAR(10),
    rua VARCHAR(100),
    bairro VARCHAR(60),
    cidade VARCHAR(60),
    numero VARCHAR(10),
    complemento VARCHAR(60),
    telefone VARCHAR(20),
    senha VARCHAR(100) NOT NULL
);
CREATE TABLE produto (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10,2) NOT NULL,
    quantidade_estoque INT NOT NULL,
    categoria VARCHAR(50)
);
CREATE TABLE carrinho_de_compras (
    id_carrinho SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_criacao DATE DEFAULT CURRENT_DATE,
    status VARCHAR(20) DEFAULT 'aberto',
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);
CREATE TABLE itens_do_carrinho (
    id_itens_do_carrinho SERIAL PRIMARY KEY,
    id_carrinho INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL CHECK (quantidade > 0),
    FOREIGN KEY (id_carrinho) REFERENCES carrinho_de_compras (id_carrinho),
    FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);
CREATE TABLE pedido (
    id_pedido SERIAL PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_carrinho INT,
    data_pedido DATE DEFAULT CURRENT_DATE,
    valor_total DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pendente',
    FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
    FOREIGN KEY (id_carrinho) REFERENCES carrinho_de_compras (id_carrinho)
);
CREATE TABLE relatorio (
    id_relatorio SERIAL PRIMARY KEY,
    id_pedido INT NOT NULL,
    data_geracao DATE DEFAULT CURRENT_DATE,
    conteudo TEXT,
    FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido)
);