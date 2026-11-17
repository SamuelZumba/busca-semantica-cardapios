"""Modo lexical local; embeddings de verdade ao instalar dependência extra e definir USE_EMBEDDINGS=1."""
import os,re,math
from functools import lru_cache
from fastapi import FastAPI
from pydantic import BaseModel,Field
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
app=FastAPI(title='Busca de Cardápio - dados sintéticos')
PRATOS=[
 {'nome':'Wrap Picante','descricao':'wrap leve com frango grelhado, pimenta e alface','preco':24.5,'ingredientes':['frango','pimenta','alface']},
 {'nome':'Salada da Horta','descricao':'salada fresca, leve, rúcula e tomate','preco':23.,'ingredientes':['rúcula','tomate']},
 {'nome':'Bowl de Açaí','descricao':'doce gelado com banana granola e açaí','preco':29.9,'ingredientes':['açaí','banana','granola']},
 {'nome':'Sanduíche Quente','descricao':'pão, queijo derretido e tomate assado','preco':26.,'ingredientes':['pão','queijo','tomate']}]
TEXT=[p['nome']+' '+p['descricao'] for p in PRATOS]
vectorizer=TfidfVectorizer(strip_accents='unicode',ngram_range=(1,2));X=vectorizer.fit_transform(TEXT)
class Busca(BaseModel): texto:str=Field(min_length=2,max_length=200); limite:int=Field(3,ge=1,le=4)
class Extracao(BaseModel): texto:str=Field(min_length=3,max_length=3000)
@lru_cache
def model():
 from sentence_transformers import SentenceTransformer
 return SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
@app.get('/health')
def health(): return {'ok':True,'embeddings_ativados':os.getenv('USE_EMBEDDINGS')=='1'}
@app.post('/buscar')
def buscar(q:Busca):
 if os.getenv('USE_EMBEDDINGS')=='1':
  m=model(); vectors=m.encode(TEXT+[q.texto],normalize_embeddings=True);scores=vectors[:-1]@vectors[-1];modo='embeddings'
 else:
  scores=cosine_similarity(vectorizer.transform([q.texto]),X)[0];modo='tfidf-lexical'
 order=sorted(range(len(PRATOS)),key=lambda i:float(scores[i]),reverse=True)[:q.limite]
 return {'modo':modo,'resultados':[dict(PRATOS[i],score=round(float(scores[i]),4)) for i in order]}
@app.post('/extrair')
def extrair(q:Extracao):
 """Extrai formato 'Prato: R$ 12,99 - ingrediente, ingrediente'. Não confundir com extração LLM."""
 results=[]
 for line in q.texto.splitlines():
  m=re.match(r'^\s*([^:]+):\s*R\$\s*(\d+(?:[.,]\d{1,2})?)\s*[-–]\s*(.*)\s*$',line,re.I)
  if m: results.append({'nome':m.group(1).strip(),'preco':float(m.group(2).replace(',','.')),'ingredientes':[s.strip() for s in m.group(3).split(',') if s.strip()]})
 return {'itens':results,'modo':'regex-estruturado'}
