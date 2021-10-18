import random
from warnings import filters
p=[]
b=[]
to=0
tob=0
odds = int(10000)
whtch = {0:"player",1:"banker",2:"引き分け"}
def deck_total(a):
    return str(a)[:1]
def odds_process(a):
    return abs(kake) * a
print("＊半角数字以外は入力しないでください＊")
#賭け金の入力
while True:
    while True:
        print("賭け金を入力してください")
        kake = int(input())
        if kake > odds:
            syakkinn = (odds - kake) * -1
            print("現在" + str(syakkinn) + "コインの借金があります")
            print("完済するまでゲームを終われません")
            break
        elif kake == 0:
            print("最低1コイン以上賭けてください")
        else:
            break 
    odds -= kake
    while True:
        basyo = int(input("どこに賭けますか？　0:player 1:banker 2:引き分け"))
        print()
        if basyo == 0 or basyo == 1 or basyo == 2:
            break
        else:
            print("正しい回答を入力してください")
    print(whtch[basyo] + "に" +  str(kake) + "コイン賭けました")

    for i in range(2):
    #プレイヤー１,2枚目
        p_deck = random.randint(1,14)
        if p_deck >= 10:
            p_deck = 0
        p.append(p_deck)
        to += p_deck
        if to > 9:
            goukei1 = deck_total(to)
            to -= to
            to += int(goukei1)
    #バンカー1,2枚目
        ban_deck = random.randint(1,14)
        if ban_deck >= 10:
            ban_deck = 0
        b.append(ban_deck)
        tob += ban_deck
        if tob > 9:
            goukei2 = deck_total(tob)
            tob -= tob
            tob += int(goukei2)
    #ナチュラルwin
    if to >= 8:
        if to == tob:
            pass
    elif tob < to and to >= 8:
        pass
    elif to < tob and tob >= 8:
        pass
    #プレイヤー3枚目
    elif to < 6:
        p_deck = random.randint(1,14)
        if p_deck >= 10:
            p_deck = 0
        p.append(p_deck)
        to += p_deck
    #バンカー3枚目
        if tob <= 2 or tob == 3 and p_deck > 8 or tob == 4 and 2 <= p_deck < 8 or tob == 5 and 4 <= p_deck < 8 or tob == 6 and 6 <= p_deck < 8:
            ban_deck = random.randint(1,14)
            if ban_deck >= 10:
                ban_deck = 0
            b.append(ban_deck)
            tob += ban_deck
    elif tob < 6:
        ban_deck = random.randint(1,14)
        if ban_deck >= 10:
            ban_deck = 0
        b.append(ban_deck)
        tob += ban_deck
    else:
        pass

    
    
    print(str(p) + " : " + str(b))
    print(str(to) + " : " + str(tob))

    #プレイヤー合計
    if to <= 9:
        print("player :" + str(to))
    else:
        goukei1 = deck_total(to)
        print("player :" + str(goukei1))

    #バンカー合計
    if tob <= 9:
        print("banker :" + str(tob))
    else:
        goukei2 = deck_total(tob)
        print("banker :" + str(goukei2))

    #勝敗
    if to > tob and basyo == 0:
        print("playerの勝ち")
        win1 = odds_process(2)
        odds += win1
    elif to > tob:
        print("playerの勝ち")
    elif to < tob and basyo==1:
        print("bankerの勝ち")
        win2 = odds_process(0.95)
        odds += int(win2)
    elif to < tob:
        print("bankerの勝ち")
    elif to == tob and basyo==2:
        print("引き分け")
        win3 = odds_process(9)
        odds += win3
    else:
        print("引き分け")

    #再挑戦の確認&処理
    print("今の手持ちは" + str(odds) + "コインです")
    kakunin = int(input("続けますか？ 0:yes 1:no"))
    print()

    p.clear()
    b.clear()
    to -= to
    tob -= tob
    if odds <= 0 and kakunin >= 1:
        print("借金があるので終われません")
        kake -= kake
    elif kakunin == 0:
        print("ゲームを継続します")
        kake -= kake
    else:
        kasegi = odds - 10000
        print("合計" + str(kasegi) + "コイン増えました")
        print("ゲームを終了します")
        print("お疲れ様でした")
        break