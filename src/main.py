import questionary
import sys

import click

import config
import utils

def main() -> None:
    print("[WELCOME] Добро пожаловать в мой проект: FakeDotEnv!")
    print("[WELCOME] Вы сможете создать фальшивый .env с случайными данными")
    print("[WELCOME] Это может отвлечь хакер от реальной инфраструктуры (ну и выбесить конечно :D)")

    click.pause("Если Вы готовы начать, то нажмите любую клавишу...")
    utils.clear_screen()

    while True:
        menu = questionary.select("[MENU] Выберите действие:", config.MAIN_MENU_OPTIONS, use_shortcuts=True)
        answer = menu.ask()

        if (answer is None) or (answer == config.EXIT_OPTION):
            sys.exit()

        if answer == "Сгенерировать .env":
            utils.clear_screen()

            # Получение информации
            dotenv_body = utils.generate_dotenv()
            fake_comment = utils.add_fake_comment()

            print(fake_comment + dotenv_body)

if __name__ == "__main__":
    main()
