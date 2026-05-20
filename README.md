# Flask + Redis + Worker
Você vai ter:

* API Flask
* Redis
* worker processando fila

Exemplo:
usuário envia imagem → worker processa.

cliente
   ↓
Flask API
   ↓
Redis queue
   ↓
Worker