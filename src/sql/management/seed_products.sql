INSERT INTO produto (nome, descricao, preco, quantidade_estoque, categoria)
VALUES
  ('Teclado Mecânico', 'Switches azuis', 299.90, 10, 'Periféricos'),
  ('Mouse Gamer', 'RGB 16000 DPI', 199.90, 20, 'Periféricos'),
  ('Monitor 24"', 'IPS 75Hz', 899.00, 5, 'Monitores')
ON CONFLICT DO NOTHING;
