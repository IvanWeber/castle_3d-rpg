import base64

with open("face-1.png", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode("utf-8")
    with open("face-1.txt", "w", encoding="utf-8") as out_file:
        out_file.write("data:image/jpeg;base64," + encoded)
