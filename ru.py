import random
import sys
import time
import os
import subprocess
import platform
import itertools

def clear():
    subprocess.Popen( "cls" if platform.system() == "Windows" else "clear", shell=True)

def ek():
    more = [[] for i in range (kol_ek)]
    for i in range (kol_ek):
        for j in range (kol_ek):
            t = random.randint(0,kol_ek)%4
            more[i].append(vid[t])
    for i in more:
        for j in range (kol_ek):
            print(str(*i[j]).rjust(4), end = '')
        print('\n')
    time.sleep(2)
    print('Начнём игру!\n')
    time.sleep(2)
    delta = False
    while not delta:
        delta = True
        (more,delta) = udal_vsex(more, delta)
        for i in more:
            for j in range (kol_ek):
                print(str(*i[j]).rjust(4), end = '')
            print('\n')
        time.sleep(1)
        if not delta:
            clear()
    if input('Ура, вы победили! Если хотите начать сначала, напишите "Ho"\n') == "Ho":
        ek()
    else:
        clear()
        print('Игра окончена!')


def udal_vsex(more, delta):
    shrimp = [';']
    fish = [chr(968)]
    ban = ['o']
    for i in range (kol_ek):
        for j in range (kol_ek):
            x = (0,-1,+1)
            y = (0,-1,+1)
            sosedi = [[i+a,j+b] for a in x for b in y]
            if more[i][j] == shrimp:
                kol_shrimp = 0
                for t in sosedi:
                    if t[0] >= 0 and t[1] >=0 and t[0] < kol_ek and t[1] < kol_ek:
                        if more[t[0]][t[1]] == shrimp:
                            kol_shrimp+=1
                if kol_shrimp >= 4 or kol_shrimp < 2:
                    delta = False
                    more[i][j] = ban
            if more[i][j] == fish:
                kol_fish = 0
                for t in sosedi:
                    if t[0] >= 0 and t[1] >=0 and t[0] < kol_ek and t[1] < kol_ek:
                        if more[t[0]][t[1]] == fish:
                            kol_fish+=1
                if kol_fish >= 4 or kol_fish < 2:
                    delta = False
                    more[i][j] = ban
            if more[i][j] == ban:
                kol_fish = 0
                kol_shrimp = 0
                for t in sosedi:
                    if t[0] >= 0 and t[1] >=0 and t[0] < kol_ek and t[1] < kol_ek:
                        if more[t[0]][t[1]] == fish:
                            kol_fish+=1
                        if more[t[0]][t[1]] == shrimp:
                            kol_shrimp+=1
                if kol_shrimp == 3:
                    delta = False
                    more[i][j] = shrimp
                elif kol_fish == 3:
                    delta = False
                    more[i][j] = fish
    return (more, delta)
            

shrimp = ';'
fish = chr(968)
rock = chr(5785)
ban = 'o'
vid = [[shrimp], [fish], [rock], [ban]]
print('Размер какого экрана предпочитаете? Введите величину 1 стороны.')
kol_ek = int(input())
ek()



