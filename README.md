# Introduce
---
Implemented RCE vulnerability in LLM integrated web. 
This chatbot helps with calculations.

#Intallation
---
Prerequisites
-Docker
-Docker compose

Steps
1. Clone the Repository
   
```
git https://github.com/WHS-LLM-Integrated-Webhacking/Chatbot_LLMMath

cd Chatbot_LLMMath
```
  
3. Setting environment variables within Docker compose

```
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./templates:/app/templates
    environment:
      FLASK_APP: app
      OPENAI_API_KEY: "your_openai_api_key"
```
