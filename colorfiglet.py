import os
import random
import shutil
import textwrap
from pyfiglet import Figlet

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

def print_colored(text: str, color: str):
    print(f"{COLORS.get(color, COLORS['reset'])}{text}{COLORS['reset']}")

def print_rainbow(text: str):
    result = ""
    for i, char in enumerate(text):
        color = RAINBOW_COLORS[i % len(RAINBOW_COLORS)]
        result += f"{color}{char}{COLORS['reset']}"
    print(result)

def display_message(msg: str, font_name: str, color_mode: str):
    # Определяем ширину терминала
    term_width = shutil.get_terminal_size().columns or 80

    # Создаём Figlet с учётом максимально допустимой ширины
    f = Figlet(font=font_name, width=term_width)

    # Разбиваем исходный текст на фрагменты, чтобы избежать слишком длинных строк
    wrap_width = max(10, term_width // 8)
    chunks = textwrap.wrap(msg, width=wrap_width)

    # Рендерим и выводим каждый фрагмент
    for chunk in chunks:
        art = f.renderText(chunk)
        if color_mode == "rainbow":
            for line in art.splitlines():
                print_rainbow(line)
        else:
            print_colored(art, color_mode)


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

# Взвешенный выбор шрифта: standard вес 3, остальные — из файла
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

# Чтение сообщений из файла
if os.path.isfile(file):
    with open(file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    # Если выбран шрифт isometric2, ищем сообщение короче 10 символов
    if font_name == "isometric2":
        msg = ""
        while True:
            candidate = random.choice(lines)
            if len(candidate) <=12 :
                msg = candidate
                break
    else:
        msg = random.choice(lines)

    msg = os.path.expandvars(msg)
    display_message(msg, font_name, color_mode)
else:
    print(f"Файл не найден: {file}")
