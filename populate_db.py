import os
import django
import random
from datetime import timedelta, datetime

# Configurando o ambiente Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from apps.patrimonio.models import Bem, Categoria
from apps.departamentos.models import Departamento
from apps.fornecedores.models import Fornecedor
from apps.movimentacoes.models import Movimentacao, HistoricoStatus

# Função para criar categorias
def criar_categorias():
    categorias_nomes = ["Computadores", "Móveis", "Veículos", "Equipamentos Médicos"]
    categorias = []
    for nome in categorias_nomes:
        categoria, created = Categoria.objects.get_or_create(nome=nome)
        categorias.append(categoria)
    return categorias

# Função para criar departamentos
def criar_departamentos():
    departamentos_nomes = ["TI", "Recursos Humanos", "Financeiro", "Manutenção"]
    departamentos = []
    for nome in departamentos_nomes:
        departamento, created = Departamento.objects.get_or_create(nome=nome, responsavel=f"Gestor {nome}")
        departamentos.append(departamento)
    return departamentos

# Função para criar fornecedores
def criar_fornecedores():
    fornecedores_nomes = [
        {"nome": "Tech Solutions", "cnpj": "12.345.678/0001-90"},
        {"nome": "Móveis Brasil", "cnpj": "23.456.789/0001-80"},
        {"nome": "Auto Parts", "cnpj": "34.567.890/0001-70"},
    ]
    fornecedores = []
    for fornecedor in fornecedores_nomes:
        obj, created = Fornecedor.objects.get_or_create(
            nome=fornecedor["nome"],
            cnpj=fornecedor["cnpj"],
            telefone=f"({random.randint(10, 99)}) 9{random.randint(1000, 9999)}-{random.randint(1000, 9999)}",
            email=f"contato@{fornecedor['nome'].replace(' ', '').lower()}.com",
        )
        fornecedores.append(obj)
    return fornecedores

# Função para criar bens patrimoniais com valores
def criar_bens(categorias, fornecedores, departamentos):
    bens = []
    status_options = ["ativo", "baixado", "manutencao"]
    
    for i in range(20):  # Criando 20 bens para teste
        bem = Bem.objects.create(
            nome=f"Bem {i+1}",
            identificador_rfid=f"RFID-{1000 + i}",
            categoria=random.choice(categorias),
            fornecedor=random.choice(fornecedores),
            departamento=random.choice(departamentos),
            data_aquisicao=datetime.now() - timedelta(days=random.randint(100, 1000)),
            status=random.choice(status_options),
            valor=round(random.uniform(500, 50000), 2),  # Valor aleatório entre R$ 500 e R$ 50.000
        )
        bens.append(bem)
    return bens


# Função para criar movimentações
def criar_movimentacoes(bens, departamentos):
    movimentacoes = []
    for _ in range(15):  # Criando 15 movimentações
        bem = random.choice(bens)
        origem = random.choice(departamentos)
        destino = random.choice(departamentos)

        while destino == origem:  # Evita que origem e destino sejam o mesmo
            destino = random.choice(departamentos)

        mov = Movimentacao.objects.create(
            bem=bem,
            origem=origem,
            destino=destino,
            descricao=f"Movimentação teste do {bem.nome}",
            data=datetime.now() - timedelta(days=random.randint(1, 30)),
        )
        movimentacoes.append(mov)
    return movimentacoes

# Função para criar histórico de status
def criar_historico_status(bens):
    historico = []
    for _ in range(15):  # Criando 15 registros de histórico
        bem = random.choice(bens)
        status_anterior = random.choice(["ativo", "baixado", "manutencao"])
        status_atual = random.choice(["ativo", "baixado", "manutencao"])

        while status_atual == status_anterior:  # Evita status repetidos
            status_atual = random.choice(["ativo", "baixado", "manutencao"])

        hist = HistoricoStatus.objects.create(
            bem=bem,
            status_anterior=status_anterior,
            status_atual=status_atual,
            alterado_por="Admin Teste",
            data_alteracao=datetime.now() - timedelta(days=random.randint(1, 30)),
        )
        historico.append(hist)
    return historico

# Executando as funções
print("📌 Populando banco de dados...")
categorias = criar_categorias()
departamentos = criar_departamentos()
fornecedores = criar_fornecedores()
bens = criar_bens(categorias, fornecedores, departamentos)
movimentacoes = criar_movimentacoes(bens, departamentos)
historico_status = criar_historico_status(bens)

print("✅ Banco de dados populado com sucesso!")
