from YandexImagesParser.ImageParser import YandexImage

parser = YandexImage()

print(parser.about, parser.version)

for item in parser.search("Дизайн паттерн"):
    print(item.title)
    print(item.url)
    print(item.preview.url)
    print("(", item.size, ")", sep='')
