from PIL import Image
from multiprocessing import Process


# изменить размер и цвет фото
def resize_image_and_change_color(image_path):
    image = Image.open(image_path)
    image = image.resize((800, 600))
    image = image.convert('L')
    image.save(image_path)


if __name__ == '__main__':

    for i in range(1, 3):
        image_path = f'foto\\img {i}.jpg'
        resize_image_and_change_color(image_path)
        print(f'Файл img {i} обработан: изменён размер и цвет')

    Process(target=resize_image_and_change_color(image_path, )).start()
