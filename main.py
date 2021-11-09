# Busca de cep usando a API https://viacep.com.br/

import requests
import json

while True:
    try:
        cep = input('Digite o cep (Apenas números): ').strip()
        if len(cep) == 8:
            break
    except:
        print('CEP INVÁLIDO!')

url = f'https://viacep.com.br/ws/{cep}/json/'
viacep = requests.get(url)
viacep = viacep.json()

if 'erro' in viacep:
    print('CEP INVÁLIDO!')
else:
    print('-'*50)
    print('CEP:', viacep['cep'])
    print('Logradouro:', viacep['logradouro'])
    print('Bairro:', viacep['bairro'])
    print('Localidade:', viacep['localidade'], '/', viacep['uf'])
    print('DDD:', viacep['ddd'])
    print('-'*50)
