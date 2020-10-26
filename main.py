from PIL import Image

bodyinput = input("Enter body rgb seperated by commas: ")
faceinput = input("Enter body rgb seperated by commas: ")

bodyinput = bodyinput.split(",")
faceinput = faceinput.split(",")

bodyrgb = []
facergb = []

for x in bodyinput:
    bodyrgb.append(int(x))

for x in faceinput:
    facergb.append(int(x))

# bodyrgb = tuple(bodyrgb)
# facergb = tuple(facergb)


def jeremskin(rgbbody, rgbface):
    body = Image.open("resources/jerembody.png")
    bodyAlpha = body.getchannel("A")
    body = Image.new("RGBA", body.size, (255, 0, 0))
    body.putalpha(bodyAlpha)

    face = Image.open("resources/jeremface.png")
    faceAlpha = face.getchannel("A")
    face = Image.new("RGBA", face.size, (255, 255, 255))
    face.putalpha(faceAlpha)

    body.paste(face, (8, 8), face)

    body.save("output/jeremskin.png")


jeremskin(tuple(bodyrgb), tuple(bodyinput))
