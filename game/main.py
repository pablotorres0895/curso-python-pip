import random

options = ('piedra', 'papel', 'tijera')


def choose_options():
  user_option = input('Priedra, papel o tijera => ').lower()

  if not user_option in options:
    print('Esa opcion no es valida')
    #continue
    return None, None

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_won_games,
                computer_won_games):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_won_games += 1
    else:
      print('papel gana a piedra')
      print('computer gano!')
      computer_won_games += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano!')
      user_won_games += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_won_games += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_won_games += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_won_games += 1

  return user_won_games, computer_won_games


def check_winner(user_won_games, computer_won_games, rounds):
  if computer_won_games == 2:
    print('*' * 10)
    print(f'El ganador es la computadora en el round# {rounds}')
    print('*' * 10)
    return True
  elif user_won_games == 2:
    print('*' * 10)
    print(f'El ganador es el usuario en el round# {rounds}')
    print('*' * 10)
    return True
  return False


def run_game():
  rounds = 1
  user_won_games = 0
  computer_won_games = 0
  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print(f'User wins: {user_won_games} - Computer wins: {computer_won_games}')
    print('*' * 10)

    rounds += 1

    user_option, computer_option = choose_options()

    user_won_games, computer_won_games = check_rules(user_option,
                                                     computer_option,
                                                     user_won_games,
                                                     computer_won_games)

    if check_winner(user_won_games, computer_won_games, rounds):
      break


run_game()
