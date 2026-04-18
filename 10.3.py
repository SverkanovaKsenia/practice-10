from PIL import Image, ImageDraw, ImageFont

holidays = {
    "Новый год": "новыйгод.jpeg",
    "8 Марта": "8 марта.jpg",
    "23 Февраля": "др.jpg"
}

print("Праздники:", ", ".join(holidays.keys()))
holiday = input("Какой праздник? ")
name = input("Имя? ")

img = Image.open(holidays[holiday])
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("/Library/Fonts/Arial Bold.ttf", 60)
except:
    font = ImageFont.truetype("arial.ttf", 60)

part1 = name
part2 = ", поздравляю!"

w1, h1 = draw.textbbox((0, 0), part1, font=font)[2:4]
w2, h2 = draw.textbbox((0, 0), part2, font=font)[2:4]

total_w = w1 + w2
x = (img.width - total_w) // 2
y = 50

draw.text((x, y), part1, fill=(255, 0, 0), font=font)

draw.text((x + w1, y), part2, fill=(0, 0, 255), font=font)

img.save("pozdravleniya.png")
print("Сохранено как pozdravleniya.png")
img.show()