# Exemplos de Uso - Login de Cliente

## Endpoint de Login
**POST** `/cliente/login`

### Exemplo de Requisição

```bash
# Com curl
curl -X POST "http://localhost:8000/cliente/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@example.com",
    "senha": "senha123"
  }'
```

```python
# Com Python requests
import requests

response = requests.post(
    "http://localhost:8000/cliente/login",
    json={
        "email": "cliente@example.com",
        "senha": "senha123"
    }
)

if response.status_code == 200:
    data = response.json()
    print(f"Login bem-sucedido! ID: {data['id_cliente']}")
    print(f"Bem-vindo, {data['nome']} {data['sobrenome']}!")
else:
    print("Erro no login:", response.json()["detail"])
```

### Resposta de Sucesso (200)
```json
{
  "id_cliente": 1,
  "email": "cliente@example.com",
  "nome": "João",
  "sobrenome": "Silva",
  "msg": "Login realizado com sucesso!"
}
```

### Resposta de Erro (401)
```json
{
  "detail": "Email ou senha inválidos"
}
```

## Fluxo de Uso

1. **Criar Cliente** (se ainda não existe):
```bash
curl -X POST "http://localhost:8000/cliente/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@example.com",
    "senha": "senha123",
    "nome": "João",
    "sobrenome": "Silva",
    "cpf": "12345678901"
  }'
```

2. **Fazer Login**:
```bash
curl -X POST "http://localhost:8000/cliente/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "cliente@example.com",
    "senha": "senha123"
  }'
```

3. **Usar o id_cliente retornado** para realizar compras no sistema.

## ⚠️ IMPORTANTE - Segurança

A implementação atual compara senhas em texto simples, o que **NÃO é seguro para produção**.

### Para produção, você deve:

1. Instalar biblioteca de hash:
```bash
pip install bcrypt
# ou
pip install passlib[bcrypt]
```

2. Fazer hash da senha ao criar cliente (no `create.sql` ou antes de inserir)
3. Verificar senha usando bcrypt no login

### Exemplo com bcrypt:
```python
import bcrypt

# Ao criar cliente
senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

# No login
if bcrypt.checkpw(credentials.senha.encode('utf-8'), cliente_data['senha'].encode('utf-8')):
    # Login válido
```

## Testar a API

Após iniciar o servidor:
```bash
python -m uvicorn src.main:app --reload
```

Acesse a documentação interativa:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

Lá você pode testar o endpoint de login diretamente pela interface web.
