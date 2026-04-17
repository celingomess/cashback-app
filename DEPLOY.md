# 🚀 Guia de Deploy na VPS com Docker

## Pré-requisitos na VPS
A VPS precisa ter instalado:
- Docker
- Docker Compose

### Instalar Docker (Ubuntu/Debian)
```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
```

### Instalar Docker Compose
```bash
sudo apt install docker-compose-plugin -y
```

---

## Passo a Passo

### 1. Enviar o projeto para a VPS
**Opção A — Via Git (recomendado):**
```bash
git clone https://github.com/celingomess/cashback-app.git
cd cashback-app
```

**Opção B — Via SCP (enviar pasta local):**
```bash
scp -r ./cashback-app usuario@IP_DA_VPS:/home/usuario/
```

---

### 2. Criar o arquivo `.env` na VPS
Dentro da pasta do projeto, crie o arquivo com as senhas:
```bash
cp .env.example .env
nano .env
```

Edite o `.env` com os valores reais:
```env
DB_PASSWORD=SuaSenhaForte@Aqui
DB_NAME=cashback_db
```

---

### 3. Subir os containers
```bash
docker compose up -d --build
```

O Docker irá:
1. Baixar a imagem do MySQL 8.0
2. Construir a imagem do Flask
3. Criar o banco de dados automaticamente
4. Iniciar ambos os serviços

---

### 4. Verificar se está rodando
```bash
docker compose ps
```

A saída deve mostrar ambos os containers com status `Up (healthy)`.

---

### 5. Acessar a aplicação
Abra no navegador:
```
http://IP_DA_VPS:8086
```

---

## Comandos Úteis

| Ação | Comando |
|---|---|
| Ver logs do app | `docker compose logs app -f` |
| Ver logs do banco | `docker compose logs db -f` |
| Parar os containers | `docker compose down` |
| Reiniciar o app | `docker compose restart app` |
| Reconstruir após mudanças | `docker compose up -d --build` |

---

## (Opcional) Expor na porta 80 com NGINX
Se quiser acessar via `http://IP_DA_VPS` (sem precisar digitar `:5000`), adicione um proxy reverso NGINX:

```bash
sudo apt install nginx -y
```

Crie o arquivo de configuração:
```bash
sudo nano /etc/nginx/sites-available/cashback
```

Cole o conteúdo:
```nginx
server {
    listen 80;
    server_name IP_DA_VPS;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Ative e reinicie:
```bash
sudo ln -s /etc/nginx/sites-available/cashback /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```
