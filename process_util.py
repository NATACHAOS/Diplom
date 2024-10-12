from PIL import Image

for i in range(1, 3):
    img2 = Image.open('C:\\Users\\Пользователь\\PycharmProjects\\Homeworks\\Module_11_bibl\\foto').copy()
    img2.save(f'foto\\img {i}.png')
