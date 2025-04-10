from flask import Flask, request, jsonify
from src.text_processing import process_text

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    analysis_type = data.get('analysis_type', 'summary')
    result = process_text(text, analysis_type)
    print(result)
    return jsonify({'analysis': result}), 200

if __name__ == '__main__':
    app.run()
