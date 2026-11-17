from fastapi.testclient import TestClient
from app import app
c=TestClient(app)
def test_busca():
 r=c.post('/buscar',json={'texto':'pimenta frango'});assert r.status_code==200;assert r.json()['resultados'][0]['nome']=='Wrap Picante'
def test_extract(): assert c.post('/extrair',json={'texto':'Sopa: R$ 19,90 - cenoura, batata'}).json()['itens'][0]['preco']==19.9
def test_validacao():assert c.post('/buscar',json={'texto':'a'}).status_code==422
