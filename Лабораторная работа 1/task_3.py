list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

quantity_players = len(list_players) // 2
first_half = list_players[:quantity_players]
print(first_half)

secon_half = list_players[quantity_players:]
print(secon_half)
