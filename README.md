
# CNAB Parser



## Ideia 💡
Criar um backend para receber e parsear CNAB files, além de mostrar as transações em tela, separadas por estabelecimentos, com saldo total em conta.

## Ferramentas 🛠️
* Python
* Django
* SQLite

## Instalação

Instale jukefood com python

- Crianção do ambiente

```bash
  python -m venv venv            
```

- Ativação do ambiente

```bash
  source venv/bin/activate          
```

- Instalação dos pacotes

```bash
  pip install -r requirements.txt                  
```

- Rodar as migrations

```bash
  python ./manage.py migrate                
```

- Rodar o servidor

```bash
  python ./manage.py runserver               
```

- Acesar o servidor em (rota de importação de arquivo CNAB:

```bash
  http://localhost:8000/            
```

- Rota para visualização dos dados importados:

```bash
  http://localhost:8000/transactions            
```
