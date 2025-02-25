import paho.mqtt.client as mqtt
import json
import random

# Configurações do MQTT
BROKER = "localhost" 
PORT = 1883
TOPIC = "rfid/registro"

# Criar um cliente MQTT
client = mqtt.Client()
client.connect(BROKER, PORT)

# Gerar um RFID aleatório
def gerar_rfid():
    return f"RFID-{random.randint(1000, 9999)}"

# Simular envio de um novo bem
def enviar_mensagem(acao, rfid, nome, status="ativo"):
    dados_rfid = {
        "acao": acao,
        "rfid": rfid,
        "nome": nome,
        "categoria_id": 1,
        "status": status
    }
    client.publish(TOPIC, json.dumps(dados_rfid))
    print(f"📤 Enviado: {dados_rfid}")

# Simular ações
rfid_teste = gerar_rfid()

print("\n📌 Enviando Registro de Novo Bem...")
enviar_mensagem("registrar", rfid_teste, "Notebook Dell")

print("\n📌 Atualizando Bem Existente...")
enviar_mensagem("atualizar", rfid_teste, "Notebook Dell Pro", "manutencao")

print("\n📌 Removendo Bem...")
enviar_mensagem("remover", rfid_teste, "Notebook Dell Pro")

client.disconnect()
