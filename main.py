from PIL import Image, ImageDraw, ImageFont, ImageFilter
from math import ceil

order = []
images = {}
class_ = ""
bg = Image.open("bg.png")
bg = bg.filter(ImageFilter.GaussianBlur(10))

with open("order.txt", "r") as file:
    class_ = file.readline().strip("\n")

    lines = file.readlines()
    for line in lines:
        skill = line.strip("\n").split(",")
        skill[1] = int(skill[1])
        order.append(skill)

        if not skill[0] in images.keys():
            images[skill[0]] = Image.open(f"{skill[0]}.png")

for key,value in images.items():
    images[key] = value.resize((value.width*4, value.height*4), Image.NEAREST)

font_file = "INKFREE.TTF"
FONT_EXTRA_LARGE = ImageFont.truetype(font_file, 120)
FONT_LARGE = ImageFont.truetype(font_file, 80)
FONT_SMALL = ImageFont.truetype(font_file, 40)

rows = ceil((len(order)-8)/9)
image_width = 2000
cycles_x = 8
cycles_y = rows + 1
cycle_offset_x = 220
cycle_offset_y = 175
base_x = 243
base_y = 200
arrow_offset_y = 30
arrow_offset_x = 155
end = False

bg_image = Image.new("RGBA", size = (image_width, base_y*2 + (rows+1)*(128 + 47) - 47), color = (0, 0, 0, 0))
bg_image_draw = ImageDraw.Draw(bg_image, "RGBA")
bg_image_draw.fontmode = "L"
image = Image.new("RGBA", size = (image_width, base_y*2 + (rows+1)*(128 + 47) - 47), color = (0, 0, 0, 0))
image_draw = ImageDraw.Draw(image, "RGBA")
image_draw.fontmode = "L"

bg_image.paste(bg)

class_text = f"{class_} 6th job skill order"
bg_image_draw.text(((image_width - image_draw.textlength(class_text, FONT_EXTRA_LARGE))/2, 40), class_text, fill=(0, 0, 0, 255), stroke_width=6, font=FONT_EXTRA_LARGE)
bg_image_draw.text(((image_width - image_draw.textlength(class_text, FONT_EXTRA_LARGE))/2, 40), class_text, fill=(255, 255, 255, 255), stroke_width=1, font=FONT_EXTRA_LARGE)

image_draw.rounded_rectangle(xy=(5, 200-47, image_width-5, base_y + (rows+1)*(128 + 47)), radius=20, fill=(0, 0, 0, 70))

current_square = 0

for y in range(cycles_y):
    for x in range(cycles_x):
        if current_square >= len(order):
            end=True
            break

        image.alpha_composite(images[order[current_square][0]].convert("RGBA"), (base_x + x * cycle_offset_x, base_y + y * cycle_offset_y))

        text_offset = 0
        skill_level = order[current_square][1]
        if skill_level >= 20:
            text_offset = 10
        elif skill_level >= 10:
            text_offset = 15
        else:
            text_offset = 25

        image_draw.text((base_x + x * cycle_offset_x + text_offset, base_y + y * cycle_offset_y + 80), f"Lv {skill_level}", fill=(0, 0, 0), stroke_width=4, font=FONT_SMALL)
        image_draw.text((base_x + x * cycle_offset_x + text_offset, base_y + y * cycle_offset_y + 80), f"Lv {skill_level}", fill=(255, 255, 255), stroke_width=1, font=FONT_SMALL)

        if not current_square + 1 >= len(order):
            image_draw.text((base_x + x * cycle_offset_x + arrow_offset_x, base_y + arrow_offset_y + y * cycle_offset_y), ">", fill=(0, 0, 0), stroke_width=4, font=FONT_LARGE)
            image_draw.text((base_x + x * cycle_offset_x + arrow_offset_x, base_y + arrow_offset_y + y * cycle_offset_y), ">", fill=(255, 255, 255), stroke_width=1, font=FONT_LARGE)

        current_square += 1
    
    if end: break;
    
    if base_x == 243:
        base_x = 23
        cycles_x += 1

combinded = Image.alpha_composite(bg_image, image)
#combinded.show()
combinded.save("order.png")