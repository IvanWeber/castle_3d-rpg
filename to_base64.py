import base64

with open("sky.jpg", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode("utf-8")
    with open("sky.txt", "w", encoding="utf-8") as out_file:
        out_file.write("data:image/jpeg;base64," + encoded)
