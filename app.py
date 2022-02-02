from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='', static_folder='./static')

generator_ = None

@app.before_request
def before_request():
    from merch_generator import generator # Долго ждем, очень долго
    global generator_
    generator_ = generator

@app.route('/')
def hello_world():
    return app.send_static_file('./index.html')

@app.route('/api', methods=['POST'])
def string_input():
    content = request.form
    print(content["query"])
    # запускаем обработку
    # и получаем результат обработки:
    result = generator_.generate(content["query"])
    print(result)
    # result_type = result["type"]
    result_type = {}

    if result_type is not False: # Или возвращаем ошибку и обрабатываем
    # В result должно быть количество сгенерированных изображений либо пути до них
        # result_type["imgs_pathes"]
        imgs_urls = ["http://192.168.0.10:5000/images/1.jpg", "http://192.168.0.10:5000/images/2.jpg"]
        return jsonify({"image_urls": imgs_urls})
    else:
        return jsonify({"error": "error_type"})

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
