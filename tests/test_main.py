from stampy import main
from pytest import raises
from click.testing import CliRunner
from random import randint
import random
import pytest


allow_str = "四字熟語"
disallow_str = "にゃんにゃん"

allow_color = "0, 0, 0"
disallow_color = "0, 0, 0, 0"
disallow_color_str = "あ, い, う, え"


def test_divLine():
    txt, txt2 = main.divLine(allow_str)
    assert txt == "熟四"
    assert txt2 == "語字"

    with raises(ValueError) as e:
        main.divLine(disallow_str)

    assert str(e.value) == "テキストの長さが不正です。"

    runner = CliRunner()
    result = runner.invoke(main.main, [allow_str, allow_color])
    assert result.exit_code == 2

    result = runner.invoke(main.main, [allow_str, disallow_color_str])
    assert result.exit_code == 2

    result = runner.invoke(main.main, [allow_str, disallow_color])
    assert result.exit_code == 2


def test_to_tuple():
    allow_tuple = (0, 0, 0)
    assert main.to_tuple(allow_color) == allow_tuple

    with raises(ValueError) as e:
        main.to_tuple(disallow_color_str)

    assert str(e.value) == "数値に変換できない要素が渡されました。"

    with raises(ValueError) as e:
        main.to_tuple(disallow_color)

    assert str(e.value) == "渡された文字列の書式が不正です。"


@pytest.fixture
def set_seed():
    seed = 5454
    return lambda: random.seed(seed)


def test_set_radom_color(set_seed):
    def random_color(num: int):
        set_seed()
        num = randint(0, 255)
        return num

    r = 0
    g = 0
    b = 0

    color = [r, g, b]
    color = list(map(random_color, color))

    assert main.set_random_color() == (202, 137, 239)


def test_toRGB():
    disallow_hex_color = "244747"
    allow_hex_color = "#244747"

    rgb_color = (36, 71, 71)

    with raises(ValueError) as e:
        main.toRGB(disallow_hex_color)

    assert str(e.value) == "引数が16進数ではありません。"

    assert main.toRGB(allow_hex_color) == rgb_color
