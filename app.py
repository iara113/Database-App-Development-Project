import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
from flask import abort, render_template, Flask
import logging
import db

APP = Flask(__name__)

# Start page------------------------------------------------------------------------------------------------------------
@APP.route('/')
def index():
    stats = {}
    x = db.execute('SELECT COUNT(*) AS instituicoes FROM Instituicao').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS acolhimentos FROM Instituicao_Acolhimento').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS dominios FROM Dominio').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS setores FROM Setor').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS dirigentes FROM Dirigente').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS telefones FROM Telefone').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS faxs FROM Fax').fetchone()
    stats.update(x)
    x = db.execute('SELECT COUNT(*) AS trabalha FROM Trabalha_Segundo').fetchone()
    stats.update(x)
    logging.info(stats)
    return render_template('index.html',stats=stats)

# Instituicoes-----------------------------------------------------------------------------------------------------------
@APP.route('/instituicoes/')
def list_instiuicoes():
    instituicoes= db.execute(
      '''
      SELECT id, Nome, Email, WebSite, Distrito, Endereco, CC, Localidade 
      FROM Instituicao
      ORDER BY Nome
      ''').fetchall()
    return render_template('instituicao-list.html', instituicoes=instituicoes)


@APP.route('/instituicoes/<int:id>/')
def get_instituicao(id):
  instituicao = db.execute(
      '''
      SELECT id, Instituicao.Nome AS Instituicao, 
      Instituicao.Email AS Email, 
      Instituicao.WebSite AS Site, 
      Instituicao.Distrito AS Distrito, 
      Instituicao.Endereco AS Endereco, 
      Instituicao.CC AS CC, 
      Instituicao.Localidade AS Localidade,
      Fax.Numero AS Fax, 
      Telefone.Numero AS Telefone,
      Dirigente.Nome AS Dirigente, 
      Instituicao_Acolhimento.Nome AS Acolhimento,
      Setor.Nome AS Setor,
      Trabalha_Segundo.Dominio AS Dominio
      FROM Instituicao 
      JOIN Fax USING(Nome) 
      JOIN Telefone USING(Nome) 
      JOIN Dirigente USING(id) 
      JOIN Instituicao_Acolhimento USING(id)
      JOIN Setor USING(id)
      JOIN Trabalha_Segundo ON(Trabalha_Segundo.Instituicao=Instituicao.Nome)
      WHERE id = %s
      ''', id).fetchone()

  if instituicao is None:
     abort(404, 'Instituicao id {} does not exist.'.format(id))

  return render_template('instituicao.html', 
           instituicao=instituicao)

@APP.route('/instituicoes/search/<expr>/')
def search_instituicao(expr):
  search = { 'expr': expr }
  expr = '%' + expr + '%'
  instituicoes = db.execute(
      ''' 
      SELECT id, Nome
      FROM Instituicao 
      WHERE Nome LIKE %s
      ''', expr).fetchall()
  return render_template('instituicao-search.html',
           search=search,instituicoes=instituicoes)



# Instituicoes Acolhimento-------------------------------------------------------------------------------------------------------------------------
@APP.route('/acolhimentos/')
def list_acolhimento():
    acolhimento = db.execute('''
      SELECT id, Nome 
      FROM Instituicao_Acolhimento
      WHERE Nome IS NOT NULL
      ORDER BY Nome
    ''').fetchall()
    return render_template('acolhimento-list.html', acolhimento=acolhimento)
  
@APP.route('/acolhimentos/<int:id>/')
def acolhimento(id):
  acolhimento = db.execute(
     '''
    SELECT id, Instituicao.Nome AS Instituicao,Instituicao_Acolhimento.Nome AS Acolhimento
    FROM Instituicao JOIN Instituicao_Acolhimento USING(id)
    WHERE id = %s
    ''', id).fetchone()
  return render_template('acolhimento.html', 
           acolhimento=acolhimento)
 
@APP.route('/acolhimentos/search/<expr>/')
def search_acolhimento(expr):
  search = { 'expr': expr }
  expr = '%' + expr + '%'
  acolhimentos = db.execute(
      ''' 
      SELECT id, Nome
      FROM Instituicao_Acolhimento
      WHERE Nome LIKE %s
      ''', expr).fetchall()
  return render_template('acolhimento-search.html',
           search=search,acolhimentos=acolhimentos)
  
  
  
  
  
# Telefone-----------------------------------------------------------------------------------------------------------------------------------------------------------------
@APP.route('/telefones/')
def list_telefone():
    telefone = db.execute('''
      SELECT id, Instituicao.Nome AS Instituicao, Telefone.Numero AS Telefone
      FROM Instituicao JOIN Telefone 
      WHERE Telefone.Numero IS NOT NULL
      ORDER BY Instituicao.Nome
    ''').fetchall()
    return render_template('telefone-list.html', telefone=telefone)
  
@APP.route('/telefones/search/<expr>/')
def search_telefone(expr):
  search = { 'expr': expr }
  expr = '%' + expr + '%'
  telefones = db.execute(
      ''' 
      SELECT Nome, Numero
      FROM Telefone
      WHERE Numero LIKE %s
      ORDER BY Nome,Numero
      ''', expr).fetchall()
  return render_template('telefone-search.html',
           search=search,telefones=telefones)




# Fax-------------------------------------------------------------------------------------------------------------------------------------------------
@APP.route('/faxs/')
def list_fax():
    fax = db.execute('''
       SELECT id, Instituicao.Nome AS Instituicao, Fax.Numero AS Fax
      FROM Instituicao JOIN Fax
      WHERE Fax.Numero IS NOT NULL
      ORDER BY Instituicao.Nome
    ''').fetchall()
    return render_template('fax-list.html', fax=fax)
  
@APP.route('/faxs/search/<expr>/')
def search_faxs(expr):
  search = { 'expr': expr }
  expr = '%' + expr + '%'
  faxs = db.execute(
      ''' 
      SELECT Nome, Numero
      FROM Fax
      WHERE Numero LIKE %s
      ORDER BY Nome, Numero
      ''', expr).fetchall()
  return render_template('fax-search.html',
           search=search,faxs=faxs)
  
  
  

# Dominio------------------------------------------------------------------------------------------------------------------------------------------
@APP.route('/dominios/')
def list_dominio():
    dominio = db.execute('''
      SELECT Nome
      FROM Dominio
      ORDER BY Nome
    ''').fetchall()
    return render_template('dominio-list.html', dominio=dominio)
  
@APP.route('/dominios/search/<expr>/')
def search_dominios(expr):
  search = { 'expr': expr }
  expr = '%' + expr + '%'
  dominios = db.execute(
      ''' 
      SELECT id, Nome, Trabalha_Segundo.Dominio AS Dominio
      FROM Instituicao JOIN Trabalha_Segundo ON (Trabalha_Segundo.Instituicao=Instituicao.Nome)
      WHERE Trabalha_Segundo.Dominio LIKE %s
      ORDER BY Nome
      ''', expr).fetchall()
  return render_template('dominio-search.html',
           search=search,dominios=dominios)
  
  


# Trabalha Segundo----------------------------------------------------------------------------------------------------------------------------------
@APP.route('/trabalhas/')
def list_TrabalhaSegundo():
    trabalhas = db.execute('''
      SELECT Instituicao, Dominio
      FROM Trabalha_Segundo
      ORDER BY Instituicao
    ''').fetchall()
    return render_template('trabalha-list.html', trabalhas=trabalhas)


  
# Dirigente----------------------------------------------------------------------------------------------------------------------------------------
@APP.route('/dirigentes/')
def list_dirigente():
    dirigente = db.execute('''
      SELECT id, Nome
      FROM Dirigente
      WHERE Nome IS NOT NULL
      ORDER BY Nome
    ''').fetchall()
    return render_template('dirigente-list.html', dirigente=dirigente)

@APP.route('/dirigentes/<int:id>/')
def dirigente(id):
  dirigente = db.execute(
    '''
    SELECT id, Instituicao.Nome AS Instituicao,Dirigente.Nome AS Dirigente
    FROM Instituicao JOIN Dirigente USING(id)
    WHERE id = %s
    ''', id).fetchone()

  if dirigente is None:
     abort(404, 'Dirigente id {} does not exist.'.format(id))

  return render_template('dirigente.html', 
           dirigente=dirigente)
  
@APP.route('/dirigentes/search/<expr>/')
def search_dirigentes(expr):
  search = { 'expr': expr }
  expr = '%' + expr + '%'
  dirigentes = db.execute(
    ''' 
    SELECT id, Instituicao.Nome AS Instituicao, Dirigente.Nome AS Dirigente
    FROM Instituicao JOIN Dirigente USING(id)
    WHERE Dirigente.Nome LIKE %s
    ''', expr).fetchall()
  return render_template('dirigente-search.html',
           search=search,dirigentes=dirigentes,)
  
# Setor---------------------------------------------------------------------------------------------------------------------------------------------------
@APP.route('/setores/')
def list_setor():
    setor = db.execute('''
      SELECT id, Instituicao.Nome AS Instituicao, Setor.Nome AS Setor
      FROM Instituicao JOIN Setor
      ORDER BY Setor.Nome
    ''').fetchall()
    return render_template('setor-list.html', setor=setor)

@APP.route('/setores/<int:id>/')
def pesquisa_setor(id):
  setor = db.execute(
    '''
    SELECT id, Instituicao.Nome AS Instituicao,Setor.Nome AS Setor
    FROM Instituicao JOIN Setor USING(id)
    WHERE id = %s
    ''', id).fetchone()

  if setor is None:
     abort(404, 'Setor id {} does not exist.'.format(id))
  return render_template('setor.html', setor=setor)
  
@APP.route('/setores/search/<expr>/')
def search_setor(expr):
  search = { 'expr': expr }
  expr = '%' + expr + '%'
  setores=db.execute(
    '''
    SELECT id, Instituicao.Nome AS Instituicao, Setor.Nome AS Setor
    FROM Setor JOIN Instituicao USING(id)
    WHERE Setor.Nome LIKE %s
    ''', expr).fetchall()
  return render_template('setor-search.html',
           search=search,setores=setores)



