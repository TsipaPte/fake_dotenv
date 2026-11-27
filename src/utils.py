import os
import sys
import secrets

import questionary

import config

def generate_dotenv() -> str:
    fields_to_include_menu = questionary.checkbox("[ШАГ 1] Выберите, какие фальшивые данные сгенерировать:", tuple(config.DOTENV_KEYS.keys()))
    fields_to_include = fields_to_include_menu.ask()

    if (fields_to_include is None) or (len(fields_to_include) == 0):
        sys.exit()

    clear_screen()
    
    is_shuffle = questionary.confirm("[ШАГ 2] Перемешать ключи?")
    shuffle = is_shuffle.ask()

    generator = secrets.SystemRandom()

    if shuffle:
        generator.shuffle(fields_to_include)

    dotenv = ""

    for dotenv_key_name in fields_to_include:
        data = config.DOTENV_KEYS[dotenv_key_name]

        startswith = data["startswith"]
        available_symbols = data["available_symbols"]
        count = data["count"]

        main_part = ""

        for _ in range(count):
            random_symbol = generator.choice(available_symbols)
            main_part += random_symbol

        string_to_include = dotenv_key_name + "=" + startswith + main_part + "\n"

        dotenv += string_to_include

    clear_screen()

    return dotenv

def add_fake_comment() -> str:
    fake_comments_menu = questionary.confirm("[ШАГ 3] Добавить фейковый комментарий в начало файла?")
    fake_comments_answer = fake_comments_menu.ask()
    
    if fake_comments_answer:
        available_presets = questionary.select("[ШАГ 3] Выберите фейковый комментарий:", config.FAKE_COMMENTS, use_shortcuts=True)
        selected_preset = available_presets.ask()

        if selected_preset is None:
            clear_screen()
            return ""
        elif selected_preset == "Свой вариант":
            print("[ШАГ 2] Введите ваш комментарий:")
            selected_preset = input("# ")
            selected_preset = "# " + selected_preset + "\n"

        changed_case = change_case_fake_comment(selected_preset)

        clear_screen()
        return changed_case + "\n"
    else:
        clear_screen()
        return ""

def change_case_fake_comment(comment: str) -> str:
    available_cases = questionary.select("[ШАГ 3.1] Изменить регистр комментария?", config.AVAILABLE_CASES, use_shortcuts=True)
    use_case = available_cases.ask()

    if use_case == "использовать нижний регистр":
        return comment.lower()
    elif use_case == "ИСПОЛЬЗОВАТЬ ВЕРХНИЙ РЕГИСТР":
        return comment.upper()
    elif use_case == "Использовать Регистр, Где Каждое Слово С Большой Буквы":
        return comment.title()
    elif use_case == "Использовать регистр как в предложениях":
        return comment.capitalize()
    elif use_case == "Не менять регистр":
        return comment

    # Если не прошла ни одна проверка, значит пользователь сделал что-то неожиданное,
    # Например нажал CTRL + C или другую неприятность!
    return ""

def clear_screen():
    platform = sys.platform

    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
