from flask import Flask, request, jsonify, send_file
from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='', static_folder='./static')

@app.route('/')
def hello_world():
    return app.send_static_file('./index.html')

@app.route('/api', methods=['POST'])
def string_input():
    content = request.form
    print(content)
    # print(content["query"])
    # запускаем обработку
    # и получаем результат обработки:
    result = {}
    if result is not None: # Или возвращаем ошибку и обрабатываем
    # В result должно быть количество сгенерированных изображений либо пути до них
        return jsonify({"image_urls":["http://192.168.0.10:5000/images/1.jpg", "http://192.168.0.10:5000/images/2.jpg"]})
    else:
        return jsonify({"error": "error_type"})

if __name__ == '__main__':
    # Тут инициализируем March Generator и создаем TextProcessor
    app.run(host= '0.0.0.0',debug=True)