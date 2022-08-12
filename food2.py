import myfood

foodlist = ["짜장면", "짬뽕", "탕수육", "우동", "돈까스"]

# 위 리스트를 출력
myfood.print_list(foodlist)

while True: 
    addfood = input("추가음식입력:")
    print(f"추가음식입력: {addfood}")
    if addfood == "그만":
        break
    foodlist.append(addfood)

myfood.print_list(foodlist)
myfood.print_rand_list(foodlist)
 