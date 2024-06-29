from flask import Flask, request, jsonify, render_template
import openai
import os
from langchain import LLMMathChain
from langchain.llms import OpenAIChat
from langchain.agents import initialize_agent, tool

app = Flask(__name__)

openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("OpenAI API did not exist")

openai.api_key = openai_api_key

llm = OpenAIChat(api_key=openai_api_key, model="gpt-3.5-turbo")
llm_math = LLMMathChain(llm=llm, verbose=True)

@tool
def calculator(query: str) -> str:
    """If you are asked to compute thing use the calculator"""
    return llm_math.run(query)

agent = initialize_agent([calculator], llm, agent="zero-shot-react-description", verbose=True)

class ChatChain:
    def __init__(self):
        self.agent = agent
    
    def run(self, user_input):
        response = self.agent.run(user_input)
        return response 

chain = ChatChain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chain.run(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
