"""
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
"""

import requests
import json 

url = 'http://localhost:11434/api/generate'
myobj = {
    "model": "tinyllama",
    "prompt": "Why is the sky blue?",
    "stream": False
}

x = requests.post(url, json = myobj)
x = json.loads(x.text)

print (x["response"])
