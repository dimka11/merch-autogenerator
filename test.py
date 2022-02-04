from YandexImagesParser.ImageParser import YandexImage
import requests

parser = YandexImage()

print(parser.about, parser.version)

for i, item in enumerate(parser.search("Дизайн паттерн")):
    print(item.title)
    print(item.url)
    print(item.preview.url)
    img_data = requests.get(item.preview.url).content
    with open(f'downloads/image_name_{i}.jpg', 'wb') as handler:
        handler.write(img_data)
    print("(", item.size, ")", sep='')
