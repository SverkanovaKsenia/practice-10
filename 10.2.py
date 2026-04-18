from PIL import Image

# Словарь: праздник -> имя файла
holidays = {
    "Новый год": "новыйгод.jpeg",
    "8 Марта": "8 марта.jpg",
    "День рождения": "др.jpg"
}

print("Доступные праздники:")
for h in holidays:
    print(f"  - {h}")

choice = input("К какому празднику нужна открытка? ")
image = Image.open(holidays[choice])
image.show()
