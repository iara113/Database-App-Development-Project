# Database-App-Development-Project

[Beatriz Silva, Sérgio Coelho, Tomás Monteiro] DCC/FCUP

Aplicação Python demonstrando o acesso à BD Instituições com atividade em Portugal

#  Referência

- [PyMySQL](https://pymysql.readthedocs.io/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Jinja templates](https://jinja.palletsprojects.com/en/3.0.x/)


# Instalação de dependências

## Python 3 e pip 

Deve ter o Python 3 e o gestor de pacotes pip instalado. Pode
instalar os mesmos em Ubuntu por exemplo usando:

```
sudo apt-get install python3 python3-pip
```

## Bibliotecas Python

```
pip3 install --user Flask==1.1.4 PyMySQL==1.0.2 cryptography==36.0.0
```


# Configuração da BD

Edite o ficheiro `db.py` no que se refere à configuração da sua BD, modificando os parâmetros `DB` (nome da base de dados), `USER` (nome do utilizador) e `PASSWORD` (senha do utilizador).

Teste o acesso executando:

```
python3 test_db_connection.py NOME_DE_UMA_TABELA
```

Se a configuração do acesso à BD estiver correcto, deverá ser listado o conteúdo da tabela `NOME_DE_UMA_TABELA`, por ex. a tabela `Instituicao` da BD Instituições com atividade em Portugal:

```
$ python3 test_db.py Instituicao
SELECT * FROM Instituicao
22 results ...
{'id': 1, 'Nome': 'Academia da Força Aérea', 'Email': 'afa.gabcmd@emfa.pt', 'WebSite': 'http://www.emfa.pt', 'Distrito': 'Lisboa', 'Endereco': 'Granja do Marquês', 'CC': '2715-021', 'Localidade': 'Pêro Pinheiro'}
{'id': 2, 'Nome': 'Academia Militar', 'Email': None, 'WebSite': None, 'Distrito': 'Lisboa', 'Endereco': 'Rua Gomes Freires', 'CC': '1169-203', 'Localidade': 'Leiria'}
{'id': 3, 'Nome': 'Area de Pediatria Cirúrgica', 'Email': 'cirurgicapediatrica@chlc.min-saude.pt', 'WebSite': 'http://www.chlc.min-saude.pt', 'Distrito': 'Lisboa', 'Endereco': 'R.Jacinta Marto', 'CC': '1169-045', 'Localidade': 'Lisboa'}
{'id': 4, 'Nome': 'Area de Pediatria Médica', 'Email': 'servico1@hdestefania.min-saude.pt', 'WebSite': 'http://www.hdestefania.min-saude.pt', 'Distrito': 'Lisboa', 'Endereco': 'R.Jacinta Marto', 'CC': '1169-045', 'Localidade': 'Lisboa'}
{'id': 5, 'Nome': 'Centro de Álgebra', 'Email': 'caul@cii.fc.ul.pt', 'WebSite': 'http://caul.cii.fc.ul.pt', 'Distrito': 'Lisboa', 'Endereco': 'Av.Prof.Gama Pinto 2', 'CC': '1649-003', 'Localidade': 'Lisboa'}
{'id': 6, 'Nome': 'Centro Algoritmi', 'Email': 'secalgoritmi@dei.uminho.pt', 'WebSite': 'http://www.algoritmi.uminho.pt', 'Distrito': 'Braga', 'Endereco': 'Campus de Azurém', 'CC': '4800-050', 'Localidade': 'Guimaraes'}
{'id': 7, 'Nome': 'Centro de Ciência Animal e Veterinária - CECAV', 'Email': 'arnaldos@utad.pt', 'WebSite': 'http://www.utad.pt/pt/investigacao/cecav/index.html', 'Distrito': 'Vila Real', 'Endereco': 'Qta. dos Prados-Apartado 1013', 'CC': '5001-801', 'Localidade': 'Vila Real'}
{'id': 8, 'Nome': 'Centro de Ciências da Terra', 'Email': None, 'WebSite': 'http://www.dct.uminho.pt/cct', 'Distrito': 'Braga', 'Endereco': 'Campus de Gualtar', 'CC': '4710-057', 'Localidade': 'Braga'}
{'id': 9, 'Nome': 'Centro de Investigação e de Tecnologias Agro Ambientais e Biológicas - CITAB', 'Email': 'citab@utad.pt', 'WebSite': 'http://www.citab.utad.pt', 'Distrito': 'Vila Real', 'Endereco': 'Apartado 1013', 'CC': '5001-801', 'Localidade': 'Vila Real'}
{'id': 10, 'Nome': 'Escola Superior de Design', 'Email': None, 'WebSite': None, 'Distrito': 'Lisboa', 'Endereco': 'Av. Dom Carlos I 4', 'CC': '1200-649', 'Localidade': 'Lisboa'}
{'id': 11, 'Nome': 'Escola Superior de Desenvolvimento Social e Comunitário', 'Email': None, 'WebSite': None, 'Distrito': 'Porto', 'Endereco': 'Avenida dos Descobrimentos 333', 'CC': '4400-103', 'Localidade': 'Vila Nova de Gaia'}
{'id': 12, 'Nome': 'Escola Superior de Enfermagem de Coimbra', 'Email': None, 'WebSite': None, 'Distrito': 'Coimbra', 'Endereco': 'Av. Bissaya Barreto', 'CC': '3000-000', 'Localidade': 'Coimbra'}
{'id': 13, 'Nome': 'Escola Superior de Saúde', 'Email': 'secretaria@essua.ua.pt', 'WebSite': 'http://www.ua.pt/essua', 'Distrito': 'Aveiro', 'Endereco': 'Campus Universitário de Santiago', 'CC': '3810-193', 'Localidade': 'Aveiro'}
{'id': 14, 'Nome': 'Lab:USE', 'Email': 'info@labuse.org', 'WebSite': 'http://www.labuse.org', 'Distrito': 'Funchal', 'Endereco': 'Campus da Penteada', 'CC': '9000-390', 'Localidade': 'Madeira'}
{'id': 15, 'Nome': 'Serviço Social', 'Email': 'geral@chpc.min-saude-pt', 'WebSite': 'http://www.chpc.min-saude.pt', 'Distrito': 'Coimbra', 'Endereco': 'Apartado 1', 'CC': '3031-801', 'Localidade': 'Coimbra'}
{'id': 16, 'Nome': 'Reitoria', 'Email': 'gabreitor@unl.pt', 'WebSite': 'http://www.unl.pt', 'Distrito': 'Lisboa', 'Endereco': 'Campus de Campolide', 'CC': '1099-085', 'Localidade': 'Lisboa'}
{'id': 17, 'Nome': 'Requimte', 'Email': 'isa@dq.fct.unl.pt', 'WebSite': 'http://www.requimte.pt/', 'Distrito': 'Setúbal', 'Endereco': 'Qta. da Torre', 'CC': '2829-516', 'Localidade': 'Caparica'}
{'id': 18, 'Nome': 'Museu de Évora', 'Email': 'mevora@imc-ip.pt', 'WebSite': None, 'Distrito': 'Évora', 'Endereco': 'Lg. Conde Vila Flor', 'CC': '7000-804', 'Localidade': 'Évora'}
{'id': 19, 'Nome': 'Serviço de Cardiologia', 'Email': None, 'WebSite': None, 'Distrito': 'Lisboa', 'Endereco': 'Av. Prof. Egas Moniz', 'CC': '1649-035', 'Localidade': 'Lisboa'}
{'id': 20, 'Nome': 'Serviço de Oncologia Médica', 'Email': None, 'WebSite': None, 'Distrito': 'Coimbra', 'Endereco': 'Av. Bissaia Barreto', 'CC': '3001-651', 'Localidade': 'Coimbra'}
{'id': 21, 'Nome': 'Escola de Serviço de Saúde Militar', 'Email': None, 'WebSite': None, 'Distrito': 'Lisboa', 'Endereco': 'R. da Infantaria 16 n30', 'CC': '1269-091', 'Localidade': 'Pêro Pinheiro'}
{'id': 22, 'Nome': 'Escola de Artes', 'Email': 'artes@porto.ucp.pt', 'WebSite': 'http://www.artes.ucp.pt', 'Distrito': 'Porto', 'Endereco': 'R. Diogo Botelho', 'CC': '4169-005', 'Localidade': 'Porto'}
```

# Execução

Inicie a aplicação executando `python3 server.py` e interaja com a mesma
abrindo uma janela no seu browser  com o endereço [__http://localhost:9001/__](http://localhost:9001/) 

```
$ python3 server.py
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
2022-12-28 18:05:42 - INFO -  * Running on http://0.0.0.0:9001/ (Press CTRL+C to quit)
2022-12-28 18:06:20 - INFO - SQL: SELECT COUNT(*) AS instituicoes FROM Instituicao Args: None
2022-12-28 18:06:20 - INFO - SQL: SELECT COUNT(*) AS acolhimentos FROM Instituicao_Acolhimento Args: None
2022-12-28 18:06:20 - INFO - SQL: SELECT COUNT(*) AS dominios FROM Dominio Args: None
2022-12-28 18:06:20 - INFO - SQL: SELECT COUNT(*) AS setores FROM Setor Args: None
2022-12-28 18:06:20 - INFO - SQL: SELECT COUNT(*) AS dirigentes FROM Dirigente Args: None
2022-12-28 18:06:20 - INFO - SQL: SELECT COUNT(*) AS telefones FROM Telefone Args: None
2022-12-28 18:06:20 - INFO - SQL: SELECT COUNT(*) AS faxs FROM Fax Args: None
2022-12-28 18:06:20 - INFO - SQL: SELECT COUNT(*) AS trabalha FROM Trabalha_Segundo Args: None
2022-12-28 18:06:20 - INFO - {'instituicoes': 22, 'acolhimentos': 22, 'dominios': 29, 'setores': 22, 'dirigentes': 22, 'telefones': 19, 'faxs': 18, 'trabalha': 
98}
```



