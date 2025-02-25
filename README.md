# 🎯 Gestão Patrimonial com Django e MQTT

Este é um **sistema web de gestão de bens patrimoniais** que permite o **rastreamento de ativos por etiquetas RFID** utilizando **Django, MQTT (via Mosquitto) e Chart.js**.

## 📌 Funcionalidades Principais
✅ Cadastro e gerenciamento de bens patrimoniais  
✅ Controle de movimentação de ativos entre setores  
✅ Rastreio por **etiquetas RFID e MQTT**  
✅ Dashboard com gráficos e indicadores  
✅ Sistema de autenticação de usuários  
✅ Testes unitários para garantir a estabilidade do sistema  

---

## 🚀 1️⃣ Tecnologias Utilizadas
- **Python 3.x**
- **Django**
- **Django REST Framework**
- **Bootstrap 5**
- **Chart.js** (Gráficos do dashboard)
- **MQTT (paho-mqtt, Mosquitto)**
- **Banco de Dados: SQLite (ou PostgreSQL/MySQL)**
- **Docker (Opcional)**

---

## 📥 2️⃣ Instalação

### 🔹 1. Clone o Repositório
```sh
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

### 🔹 2. Crie e Ative um Ambiente Virtual
```sh
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 🔹 3. Instale as Dependências
```sh
pip install -r requirements.txt
```

### 🔹 4. Configure o Banco de Dados
```sh
python manage.py migrate
```

### 🔹 5. Crie um Superusuário
```sh
python manage.py createsuperuser
```
📍 **Siga as instruções para criar um usuário administrador.**

### 🔹 6. Inicie o Servidor
```sh
python manage.py runserver
```
📍 **O sistema estará disponível em:** **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

---

## 📡 3️⃣ Configuração do MQTT
### **🔹 1. Instale o Mosquitto MQTT**
No Linux:
```sh
sudo apt update && sudo apt install mosquitto mosquitto-clients
```
No Windows, faça o download do **Mosquitto** [aqui](https://mosquitto.org/download/).

### **🔹 2. Iniciar o Broker MQTT**
```sh
mosquitto -v
```

---

## 🔄 4️⃣ Como Funciona o Registro RFID
### **Subscriber MQTT (`subscribe_rfid.py`)**
O sistema escuta novos **RFIDs enviados via MQTT** e **registra/atualiza** no banco de dados.

**Rodar o subscriber para escutar registros RFID**:
```sh
python subscribe_rfid.py
```

✅ **Ele escuta mensagens no tópico:** `"rfid/registro"`

---

### **Publisher MQTT (`simulate_rfid.py`)**
Simula um **leitor RFID enviando mensagens** para o sistema.

**Rodar a simulação do leitor RFID**:
```sh
python simulate_rfid.py
```

📌 **O Publisher pode enviar ações como:**
```json
{
    "acao": "registrar",
    "rfid": "RFID-1234",
    "nome": "Notebook Dell",
    "categoria_id": 1,
    "status": "ativo"
}
```

📍 **Ações possíveis:**
- `"registrar"` → Cadastra um novo bem se o RFID não existir
- `"atualizar"` → Atualiza status/nome de um bem existente
- `"remover"` → Marca um bem como "baixado"

---

## 🎨 5️⃣ Dashboard e Interface
O sistema possui um **dashboard interativo** com gráficos gerados pelo **Chart.js**:

📌 **Métricas disponíveis:**
✅ **Número total de bens cadastrados**  
✅ **Distribuição dos bens por categoria**  
✅ **Status dos bens (Ativo, Baixado, Manutenção)**  
✅ **Últimas movimentações de bens**  

📍 **Exemplo de dashboard:**
![Dashboard](docs/dashboard-preview.png)

---

## 🧪 6️⃣ Testes Automatizados
Para rodar os **testes unitários**, execute:
```sh
python manage.py test
```

📌 **Os testes cobrem:**
✅ Cadastro e autenticação de usuários  
✅ CRUD de bens patrimoniais  
✅ Movimentações e histórico de status  
✅ Integração com o sistema de etiquetas RFID  

---

## 🛠 7️⃣ Contribuindo
1. **Fork** o projeto  
2. Crie uma **branch**: `git checkout -b minha-feature`  
3. Faça suas alterações e **commit**: `git commit -m 'Adicionando nova feature'`  
4. **Push** para a branch: `git push origin minha-feature`  
5. Abra um **Pull Request** 🚀  

---

📍 **Desenvolvido por:** **José Henrique Castro Andrade** ✨
