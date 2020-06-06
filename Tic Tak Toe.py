# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 11:07:48 2020

@author: Naman Balaji
   """
   

entries =[' ',' ',' ',' ',' ',' ',' ',' ',' ']
win = ''
player = 'player1'
def draw_board(val):
    print(val[6]+'|'+val[7]+'|'+val[8])
    print('-|-|-')
    print(val[3]+'|'+val[4]+'|'+val[5])
    print('-|-|-')
    print(val[0]+'|'+val[1]+'|'+val[2])
    
    
def player_input():
    p1marker = ''
    p2marker = ''
    while (p1marker != 'X' and p1marker != 'O'):
        p1marker = input("Player1, what do you choose X or O: ")
    if p1marker == 'X':
        p2marker = 'O'
    else:
        p2marker = 'X'
    return [p1marker, p2marker] 

  
def handle_turn(player):

  global marker
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")
  valid = False
  while not valid:

    
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    
    position = int(position) - 1

    
    if entries[position] == " ":
      valid = True
    else:
      print("Position already taken.")

  
  if player =='player1':
      entries[position] = markers[0]
  else:
      entries[position] = markers[1]

  
  draw_board(entries)

def check_winner():
    global win
    global markers
    
    if entries[0]==entries[1]==entries[2]!=" " or entries[3]==entries[4]==entries[5]!=" " or entries[6]==entries[7]==entries[8]!=" ":
       if entries[0]== markers[0] or entries[3]== markers[0] or entries[7]== markers[0]:
           win = 'Player1'
       else:
           win = "Player2"
    elif entries[0]==entries[6]==entries[3]!=" " or entries[4]==entries[1]==entries[7]!=" " or entries[8]==entries[5]==entries[2]!=" ":
        if entries[0]== markers[0] or entries[4]== markers[0] or entries[8]== markers[0]:
           win = 'Player1'
        else:
           win = "Player2"
    elif entries[0]==entries[4]==entries[8]!=" " or entries[6]==entries[4]==entries[2]!=" ":
        if entries[4] == markers[0]:
            win = 'Player1'
        else:
            win = 'Player2'
    else:
         if " " not in entries:
             win = "Tie"
             print("It's a tie")
        

def change_turn():
    global player
    if player == 'player1':
        player = 'player2'
    else:
        player = 'player1'



markers = player_input()
draw_board(entries)

while win =='':
    handle_turn(player)
    check_winner()
    change_turn()
    
if win!='Tie' and win!='':
    print(win+' is the winner')
   
