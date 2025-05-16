# Rodando o Servidor
- Crie o virtual enviroment
- Instale os pacotes do requirements.txt
- Na root do projeto (:~/integration-workshop-3$):
```
uvicorn backend.api:app --reload --host 0.0.0.0 --port 8000
```
