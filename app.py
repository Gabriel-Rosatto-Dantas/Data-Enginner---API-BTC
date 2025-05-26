import requests
from tinydb import TinyDB
from datetime import datetime
from time import sleep


def extrair_preco_btc():
    url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    response = requests.get(url)
    return response.json()

def transformar_preco_btc(dados_json):
    valor = dados_json['data']['amount']
    cripto = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    dados_tratador = {
        'valor': valor,
        'cripto': cripto,
        'moeda': moeda,
        'data': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return dados_tratador

def load(dados_tratados):
    db = TinyDB('db.json')
    db.insert(dados_tratados)
    print("Dados inseridos com sucesso!")
    
    
if __name__ == "__main__":
    while True:
        dados_json = extrair_preco_btc()
        dados_tratados = transformar_preco_btc(dados_json)
        load(dados_tratados)
        sleep(20)
