from flask import Flask, request, jsonify, send_file
app = Flask(__name__,  static_url_path='', 
            static_folder='./static')

@app.route('/api/string_input/<uuid>', methods=['GET', 'POST']) # примеры с SO
def string_input(uuid):
    content = request.json
    print(content['text_desc'])
    # запускаем обработку, как нам асинхронно вернуть ответ?
    return jsonify({"uuid":uuid})

@app.route('/get_image') # ?type=1
def get_image():
    if request.args.get('type') == '1':
       filename = '_R252NvcByc.jpg'
    else:
       filename = 'health-image.jpg'
    return send_file(filename, mimetype='image/jpeg') # for download image

@app.route('/get_images_urls', methods=['GET'])
def get_image():
	# Проверяем наличие сгенерированных изображений
    if (True)
    	return jsonify({"error":"error type"})
    else:
    	return jsonify("image_urls":[{"image1": "url1"}, {"image2": "url2"}])

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)


# example requrest:
# POST http://192.168.0.10:5000/api/string_input/1
# [{"key":"Content-Type","name":"Content-Type","value":"application/json","description":"","type":"text"}]
# {"text_desc":"моя строка"}