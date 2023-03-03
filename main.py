import sys
import time
import random
import merge_sorts

number_list = []

def loading_animation():
    animation = "|/-\\"
    idx = 0
    while idx < 20:
        print(animation[idx % len(animation)]+" Loading...", end="\r")
        idx += 1
        time.sleep(0.1)
    print(" Loading")

def get_input(number):
    print('\n')
    for i in range(number) :
        try :
            number_input = int(input("Please input the {} number : ".format(i+1)))
            if number_input == 1999 :
                sys.exit()
            number_list.append(number_input)
        except :
            print("Please only input the number!      TRY AGAIN!")
            return True
    return False


def game_draw(number_list):
    print("""                                   ヘヽ.　　　　/　,ー､ 〉
                            　　　　　＼ ', !-─‐-i　/　/´
                            　　　 　 ／｀ｰ'　　　 L/／｀ヽ､
                            　　 　 /　 ／,　 /|　 ,　 ,　　　 ',
                            　　　ｲ 　/ /-‐/　ｉ　L_ ﾊ ヽ!　 i
                            　　　 ﾚ ﾍ 7ｲ｀ﾄ　 ﾚ'ｧ-ﾄ､!ハ|　 |
            R U SURE U READY?      !,/7 '0'　　 ´0iソ| 　 |　　　
        IF YOU'RE READY             |.从"　　_　　 ,,,, / |./ 　 |
            PRESS R                ﾚ'| i＞.､,,__　_,.イ / 　.i 　|
        IF NOT                       ﾚ'| | / k_７_/ﾚ'ヽ,　ﾊ.　|
            PRESS N                    | |/i 〈|/　 i　,.ﾍ |　i　|
                            　　　　　　.|/ /　ｉ： 　 ﾍ!　　＼　|
                            　　　 　 　 kヽ>､ﾊ 　 _,.ﾍ､ 　 /､!
                            　　　　　　 !'〈//｀Ｔ´', ＼ ｀'7'ｰr'
                            　　　　　　 ﾚ'ヽL__|___i,___,ンﾚ|ノ
                            　　　　　 　　　ﾄ-,/　|___./
                            　　　　　 　　　'ｰ'　　!_,.""")
    ready_input = input("Are you ready? : ")
    return ready_input


if __name__ == '__main__': 
    while True :
        result = get_input(10)
        if result == True :
            number_list = []
            continue
        else :
            break
    print('\n')
    random.shuffle(number_list)
    print("Your number will be :" ,number_list)
    r = game_draw(number_list)
    if r == "R" or r == "r":
        #print("next step!")
        try:
            loading_animation()
        except KeyboardInterrupt:
            sys.exit()
    else :
        print("hahahahah you're weak!    Cya!")
        sys.exit()

    print(" Done!\n")
    countdown = 0
    while countdown < 85:
        if countdown == 0 :
            print("Let's me introduce you about a merge sort!")
        elif countdown == 25 :
             print("So merge sort will spill all the number from list to half, each time with a recursion")
        elif countdown == 55 :
            print("so this is how it work with the number we have\n")
        countdown += 1
        time.sleep(0.1)
    
    print("Result is : ", merge_sorts.half_merge(number_list))


    