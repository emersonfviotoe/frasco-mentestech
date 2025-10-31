# 🚀 Deploy no Render.com + HostGator

## 1️⃣ Suba este projeto no GitHub

## 2️⃣ No Render.com:
- Crie um novo Web Service
- Conecte ao repositório GitHub
- Ambiente: **Python 3.11**
- O deploy automático será feito com base no `render.yaml`

## 3️⃣ Configure variáveis de ambiente no Render
- FLASK_ENV=production
- SECRET_KEY=uma_chave_segura
- DATABASE_URL=sqlite:///instance/techmind.db

## 4️⃣ Após o deploy, copie o domínio (ex: techmind.onrender.com)

## 5️⃣ No cPanel da HostGator:
- Vá em **Editor de Zona DNS**
- Crie um registro CNAME:
  - Nome: **www**
  - Valor: **techmind.onrender.com**

## 6️⃣ Espere 10–15 minutos e acesse:
👉 [https://www.mentestech.com](https://www.mentestech.com)

---
Usuário admin padrão:
- Email: admin@techmind.com
- Senha: admin123
