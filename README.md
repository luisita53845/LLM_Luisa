# LLM_Luisa
Repositorio de prueba para implementar LLM y una aplicación web usando ollama

## 1. Instalación:
Cómo primer paso descargamos [ollama](https://ollama.com/download/linux) de su pagina web y ejecutamos el siguiente comando:

````bash 
$ curl -fsSL https://ollama.com/install.sh | sh
````

## 2. Arrancar el servidor:
Ejecutar el servidor de API REST de ollama con el siguiente comando:

````bash 
$ ollama serve
````

## Descargar un modelo:
Luego de arrancar el servidor, creamos una nueva consola para el siguiente paso.

En la página de ollama descargar un [modelo](https://ollama.com/library) utilizando el siguiente comando:

````bash 
$ ollama pull 'modelo'
````

En este caso usaremos:

````bash 
$ ollama pull tinyllama
````

De igual forma podemos observar los modelos descargados con el siguiente comando:

````bash 
$ ollama list
````

## 4. Realizar un request a la API REST en stream

Para realizar una consulta utilizamos el comando curl como se muestra en el siguiente ejemplo:

````bash 
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}'
````

## 5. Realizar un request a la API REST sin stream

Para realizar una consulta a la API REST sin stream se hace de la siguiente forma:

````bash 
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
````

## 5. Consultar a groq

Estructura básica para realizar una consulta a groq mediante API REST

````bash 
curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${GROQ_API_KEY}" \
  -d '{
         "messages": [
           {
             "role": "user",
             "content": ""
           }
         ],
         "model": "llama3-8b-8192",
         "temperature": 1,
         "max_tokens": 1024,
         "top_p": 1,
         "stream": true,
         "stop": null
       }'
````