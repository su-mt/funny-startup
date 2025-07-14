import os
import random
from pyfiglet import Figlet
from art import tprint

# Цвета ANSI
COLORS = {
    "cyan": "\033[96m",
    "red": "\033[91m",
    "blue": "\033[94m",
    "green": "\033[92m",
    "reset": "\033[0m"
}

RAINBOW_COLORS = [
    "\033[91m",  # красный
    "\033[93m",  # жёлтый
    "\033[92m",  # зелёный
    "\033[96m",  # голубой
    "\033[94m",  # синий
    "\033[95m"   # фиолетовый
]

def print_colored(text, color):
    print(f"{COLORS.get(color, COLORS['reset'])}{text}{COLORS['reset']}")

def print_rainbow(text):
    result = ""
    for i, char in enumerate(text):
        color = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
        result += f"{color}{char}{COLORS['reset']}"
    print(result)

def display_message(msg, font_name, color_mode):
    f = Figlet(font=font_name)
    ascii_art = f.renderText(msg)
    if color_mode == "rainbow":
        for line in ascii_art.splitlines():
            print_rainbow(line)
    else:
        print_colored(ascii_art, color_mode)

# Получение переменных окружения
file_dir = os.environ.get("FUNNY_START_HOME", ".")
fonts_file = os.path.join(file_dir, "fonts.txt")

main_file = os.path.join(file_dir, "start_messages.txt")
ru_file = os.path.join(file_dir, "ru_start_messages.txt")

# Выбор файла с сообщением (русский в 10 раз реже)
message_files = [main_file, ru_file]
weights = [10, 1]
file = random.choices(message_files, weights=weights, k=1)[0]

# Выбор цветового режима
color_modes = ["cyan", "red", "blue", "green", "rainbow"]
color_mode = random.choice(color_modes)

# Взвешенный выбор шрифта
if os.path.basename(file).startswith("ru_"):
    font_name = "moscow"
else:
    use_standard = random.choices(
        ["standard", "from_file"],
        weights=[3, 1],
        k=1
    )[0]

    if use_standard == "standard" or not os.path.isfile(fonts_file):
        font_name = "standard"
    else:
        with open(fonts_file, "r", encoding="utf-8") as f:
            fonts = [line.strip() for line in f if line.strip()]
        font_name = random.choice(fonts)

# Чтение и вывод сообщения
if os.path.isfile(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    msg = random.choice(lines)
    msg = os.path.expandvars(msg)
    display_message(msg, font_name, color_mode)
else:
    print(f"Файл не найден: {file}")
