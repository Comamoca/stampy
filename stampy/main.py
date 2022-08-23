from PIL import Image, ImageFont, ImageDraw
import click


def divLine(txt: str) -> tuple[str, str]:
    if len(txt) != 4:
        raise ValueError

    line = []
    line2 = []
    for i, c in enumerate(txt):
        if i == 0 or i == 2:
            line.append(c)
        else:
            line2.append(c)

    line.reverse()
    line2.reverse()

    lineTxt = "".join(line)
    lineTxt2 = "".join(line2)

    return (lineTxt, lineTxt2)


def to_tuple(txt: str) -> tuple[int, ...]:
    str_list = txt.split(",")
    int_list = list(map(int, str_list))
    int_tuple = tuple(int_list)

    return int_tuple


@click.command()
@click.argument("text")
@click.option('--color', help='set color', default="0, 0, 0")
# @click.argument("text")
def main(text: str, color: str = "0, 0, 0"):
    font_path = "rounded-x-mplus-1c-bold.ttf"
    font_size = 100

    tup_color = to_tuple(color)

    text, text2 = divLine(text)
    # color = (255, 255, 255)
    # color = (0, 0, 0)
    # blue  = (131, 217, 242)

    # image = Image.open(image_path)
    image = Image.new("RGB", (200, 200), (255, 255, 255))
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(image)
    draw.text((0, -20), text, font=font, fill=tup_color)
    draw.text((0, font_size - 20), text2, font=font, fill=tup_color)
    image.save("out.png")
