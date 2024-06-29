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
  
2. Setting environment variables within Docker compose

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

3. Build
```
docker-compose up --build
```

4. Run

```
Access to http://127.0.0.1:5000
```

#Usage
---
When chatbot is running, you can be used to calculate.
![image](https://github.com/WHS-LLM-Integrated-Webhacking/Chatbot_LLMMath/assets/93432485/04a940d7-1a86-4161-8a31-8778590ee484)
