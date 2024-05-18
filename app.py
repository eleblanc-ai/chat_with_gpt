import os
from flask import Flask, request, render_template, Response,jsonify
from openai import OpenAI
import dotenv

app = Flask(__name__)

dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def stream(conversation_history, model_name):
    response = ""
    stream = client.chat.completions.create(
        model=model_name,
        messages=conversation_history,
        stream=True
    )
    for chunk in stream:
        if hasattr(chunk.choices[0].delta, "content"):
            content = chunk.choices[0].delta.content
            if content is not None:
                response += content
                yield content

    conversation_history.append({"role": "assistant", "content": response})
    return response

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/stream-gpt-model', methods=['POST'])
def get_stream():
    request_data = request.get_json()
    user_input = request_data['prompt']
    model_name = request_data['model']
    conversation_history = request_data['conversationHistory']

    conversation_history.append({"role": "user", "content": user_input})
    assistant_response = stream(conversation_history, model_name)

    return Response(assistant_response, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)