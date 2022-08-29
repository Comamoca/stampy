from PIL import Image, ImageFont, ImageDraw
import click
import os
import random
from pathlib import Path


def set_random_color() -> tuple[int, ...]:
    def rand_col(num: int):
        num = random.randint(0, 255)
        return num

    r = 0
    g = 0
    b = 0

    color = [r, g, b]
    color = list(map(rand_col, color))
    return tuple(color)


def divLine(txt: str) -> tuple[str, str]:
    if len(txt) != 4:
        raise ValueError("テキストの長さが不正です。")

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

    try:
        int_list = list(map(int, str_list))

    except ValueError:
        raise ValueError("数値に変換できない要素が渡されました。")
        os.exit(1)

    if len(int_list) != 3:
        raise ValueError("渡された文字列の書式が不正です。")
        os.exit(1)

    return tuple(int_list)


def toRGB(hex_color: str) -> tuple[int, int, int]:
    if hex_color[0] != "#":
        # 16進数では無い
        raise ValueError("引数が16進数ではありません。")

    R = int(hex_color[1:3], 16)
    G = int(hex_color[3:5], 16)
    B = int(hex_color[5:7], 16)

    return (R, G, B)


@click.command()
@click.argument("text")
@click.option("--color", help="set color", default="")
@click.option("--ishex", help="set color to hex", is_flag=True)
# @click.argument("text")
def main(text: str, color: str = "", ishex: bool = False):
    font_path = str(Path().cwd() / Path("./fonts/rounded-x-mplus-1c-bold.ttf"))
    font_size = 100

    if len(color) >= 0:
        tup_color = set_random_color()

    if ishex:
        tup_color = toRGB(color)

    elif len(color) != 0:
        tup_color = to_tuple(color)

    # color = (255, 255, 255)
    # color = (0, 0, 0)
    # blue  = (131, 217, 242)

    text, text2 = divLine(text)

    image = Image.new("RGB", (200, 200), (255, 255, 255))

    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(image)

    draw.text((0, -20), text, font=font, fill=tup_color)
    draw.text((0, font_size - 20), text2, font=font, fill=tup_color)

    image.save("out.png")
