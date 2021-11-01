import actions
import pyautogui as pg

actions.open_game()


search_list = [
    "red clay pot",
    "chunk of adderstone",
]


# while True:
for name in search_list:
    if actions.make_search(name):
        actions.send_message_to_discord()
