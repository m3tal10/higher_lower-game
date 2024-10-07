from art import logo,vs
from game_data import data
import random

print(logo)

  


def generate_random():
  return random.randint(1, len(data)-1)
#Generate a random number
a_index= generate_random()
#make an array to store the values of the current game phase
phase=[data[a_index]]
is_playing= True
right_wrong=""
while is_playing:
  b_index= generate_random()
  phase.append(data[b_index])
  a_data= phase[len(phase)-2]
  b_data= phase[len(phase)-1]
  print(f"Compare A: {a_data['name']}, {a_data['description']}, from {a_data['country']}.")
  print(vs)
  print(f"Against B: {b_data['name']}, {b_data['description']}, from {b_data['country']}.")

  chosen= input("Who has more followers? type 'A' or 'B': ").lower()
  if(chosen=='a'):
    if(a_data['follower_count']<b_data['follower_count']):
      right_wrong="Game over. You're wrong! "
      is_playing=False
    else:
      right_wrong="You're right! "
  else:
    if( b_data['follower_count']<a_data['follower_count']):
      right_wrong="Game over. You're wrong! "
      is_playing=False
    else:
      right_wrong="You're right! "

  print(f"{right_wrong}Current score is: {len(phase)-2}")