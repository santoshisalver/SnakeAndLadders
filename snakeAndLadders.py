# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 22:29:45 2024

@author: santo
"""

from PIL import Image
import random
end=30
def show_board():
    img=Image.open('snake&ladder.jpg')
    img.show() 
def check_ladder(points):
    if points==3:
        print('Ladder')
        return 22
    elif points==5:
        print('Ladder')
        return 8
    elif points==11:
        print("Ladder")
        return 26
    elif points==20:
        print("Ladder")
        return 29
    else:
        return points
def check_snake(points):
    if points==27:
        print("Snake")
        return 1
    elif points==8:
        print("Snake")
        return 5
    elif points==26:
        print("Snake")
        return 11
    elif points==29:
        print("Snake")
        return 20
    else:
        return points
def reached_end(points):
    if points==end:
        return True
    else:
        return False
def play():
    p1_name=input('player one please enter your name: ')
    p2_name=input('player two please enter your name: ')
    pp1=0
    pp2=0
    turn=0
    while(1):
        if turn%2==0:
            print(p1_name,'your turn')
            c=input('Press 1 to continue,0 to quit')
            if c=='0':
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quitting the game,Thanks for playing')
                break
            dice=random.randint(1,6)
            print('Dice showed: ',dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1>end:
                pp1=end
            print(p1_name,'your score: ',pp1)
            if reached_end(pp1):
                print(p1_name,'won')
                break
        else:
            print(p2_name,'your turn')
            c=input('Press 1 to continue,0 to quit')
            if c==0:
                print(p1_name,'scored',pp1)
                print(p2_name,'scored',pp2)
                print('Quitting the game,Thanks for playing')
                break
            dice=random.randint(1,6)
            print('Dice showed: ',dice)
            pp2=pp2+dice
            pp2=check_ladder(pp2)
            pp2=check_snake(pp2)
            if pp2>end:
                pp2=end
            print(p2_name,'your score: ',pp2)
            if reached_end(pp2):
                print(p2_name,'won')
                break
        turn=turn+1
show_board()
play()
            