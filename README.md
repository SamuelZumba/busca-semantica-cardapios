> **STATUS: EM DESENVOLVIMENTO.** O código aqui é um protótipo/baseline e NÃO uma aplicação web finalizada. Não apresente como implementação de IA treinada, agente LLM ou integração real sem validação adicional.

# Busca Semântica de Cardápios

> **Status:** MVP educacional; dados fictícios. Nenhuma integração oficial com iFood. Resultados e deploys precisam de verificação antes de divulgação.

## Problema e oportunidade
Recuperação de pratos com embeddings opcionais, índice local e extração estruturada de cardápios fictícios.

## Solução e arquitetura
Consulte o código em Python para o fluxo: **entrada validada → lógica/serviço → resposta auditável**. A implementação usa exemplos sintéticos para demonstrar capacidade técnica sem expor dados de terceiros.

## Tecnologias
Python 3.12; consulte `requirements.txt`. Tópicos recomendados: `python embeddings sentence-transformers search api`.

## Instalação
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

## Como rodar / demonstração
As instruções específicas estão no final deste README ou nos comentários do arquivo `app.py`/`main.py`. Não há URL pública nesta entrega. Para usar modelos externos, configure `.env` **somente localmente**, sem versionar. Não copie dados reais de restaurantes ou usuários.

## Resultados e avaliação
- Resultado técnico: rodar testes, salvar capturas e medir latência/qualidade.
- Métrica de negócio: `[X% / X minutos / X horas a preencher após experimento]`.
- Reprodutibilidade: execute com dados sintéticos e anote parâmetros, data, tamanho de amostra.

## Segurança e limites
Sem credenciais no repositório, nem decisões reais de cupons ou acesso a pedidos. O modo local simplificado deve ser apresentado como tal. Saídas de IA necessitam validação humana antes de publicação comercial.

## Próximos passos
- Medir métricas e latência; documentar experimentos e capturas.
- Configurar CI, publicar demo isolada e registrar endereço real.
- Quando aplicável, ligar API LLM com limites de custo e avaliação de prompts.

## Licença
Escolher uma licença somente após validar titularidade e dependências; não foi imposta uma licença automática.

### Executar
`uvicorn app:app --reload --port 8002` → `/docs`. Por padrão usa TF-IDF **lexical**. Para usar **embeddings reais**, instale `pip install -r requirements-embeddings.txt` e ative `USE_EMBEDDINGS=1` (primeiro uso baixa modelo público e requer internet). A extração é regex e só reconhece linhas no formato indicado; não é LLM.


## Resumo verificado e prévias locais

Ranking local TF-IDF + similaridade de cossenos e extração de itens por expressão regular. Embeddings reais são opcionais e não foram executados aqui.

**Comando principal:** `python -m uvicorn app:app --reload --port 8002` e abra `/docs`

**Validação:** `python -m pytest -q`. Testes automatizados cobrem o comportamento local básico; integrações de terceiros, deploy, custo, performance e segurança de produção exigem testes adicionais.

### Capturas reais
Adicione aqui capturas feitas ao executar este projeto, após remover dados pessoais e segredos. Não há imagens fictícias de interface neste repositório.
