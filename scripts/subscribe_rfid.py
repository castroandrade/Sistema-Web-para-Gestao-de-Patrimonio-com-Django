import os
import django
import paho.mqtt.client as mqtt
import json

# Configurar Django para acessar os models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.config")
django.setup()

from apps.patrimonio.models import Bem, Categoria

# Configurações do MQTT
BROKER = "localhost"  # Altere se necessário
PORT = 1883
TOPIC = "rfid/registro"

# Callback quando uma mensagem chega
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))
        acao = data.get("acao")
        rfid = data.get("rfid")
        nome = data.get("nome", "Item Desconhecido")
        categoria_id = data.get("categoria_id", 1)
        status = data.get("status", "ativo")

        if not rfid:
            print("⚠ Erro: Mensagem sem RFID válido!")
            return

        # Verifica se o bem já existe
        bem = Bem.objects.filter(identificador_rfid=rfid).first()

        if acao == "registrar":
            if bem:
                print(f"⚠ O bem com RFID {rfid} já está cadastrado.")
            else:
                categoria, _ = Categoria.objects.get_or_create(id=categoria_id, defaults={"nome": "Geral"})
                Bem.objects.create(
                    nome=nome,
                    identificador_rfid=rfid,
                    categoria=categoria,
                    status="ativo"
                )
                print(f"✅ Novo bem registrado: {nome} ({rfid})")

        elif acao == "atualizar":
            if bem:
                bem.nome = nome
                bem.status = status
                bem.save()
                print(f"🔄 Bem atualizado: {bem}")
            else:
                print(f"⚠ Nenhum bem encontrado com RFID {rfid} para atualizar.")

        elif acao == "remover":
            if bem:
                bem.status = "baixado"
                bem.save()
                print(f"❌ Bem removido (status 'baixado'): {bem}")
            else:
                print(f"⚠ Nenhum bem encontrado com RFID {rfid} para remover.")

        else:
            print(f"⚠ Ação inválida recebida: {acao}")

    except Exception as e:
        print(f"❌ Erro ao processar mensagem MQTT: {e}")

# Configuração do Cliente MQTT
client = mqtt.Client()
client.on_message = on_message

# Conectar ao broker
client.connect(BROKER, PORT)
client.subscribe(TOPIC)

print(f"📡 Escutando mensagens no tópico: {TOPIC}")
client.loop_forever()
