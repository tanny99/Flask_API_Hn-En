from flask import Flask, jsonify, request
app = Flask(__name__)
from googletrans import Translator

# create a translator object
translator = Translator()

# translate from English to French


# print the translated text
# print(french_translation.text)

@app.route('/api/data', methods=['POST'])
def post_data():
    input_data = request.form.get('input')
    # Code for processing the input data
#     english_text = "Hello, how are you?"
    english_translation = translator.translate(input_data, dest='en')
    result = {"success": True, "data": english_translation.text}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
 
# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/hello')
# def hello():
#     return jsonify({'message': 'Hello, world!'})

# if __name__ == '__main__':
#     app.run()
