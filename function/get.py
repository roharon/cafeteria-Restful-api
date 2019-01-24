import sqlite3

def formatted_haksik(time, cafeteria):

    con = sqlite3.connect('./DB/haksik_data.db')
    cur = con.cursor()

    querys = 'SELECT ' + time + ' FROM ' + cafeteria
    cur.execute(querys)
    menu_size = len(cur.fetchall())
    cur.execute(querys)

    menu_list = []

    for i in range(0, menu_size):
        menu = cur.fetchone()[0]
        if len(menu) <= 1:
            continue
        else:
            menu_list.append(menu)

    for size in range(0, len(menu_list)):
        menu_list[size] = menu_list[size].split('\n')

        for i in range(0, len(menu_list[size])):
            try:
                menu_list[size].remove('')
                #print(menu_list)
# 어문관 작업중 .  2017-11-06

                for i in range(0,len(menu_list[size])):
                    if '선택식' in menu_list[size][i]:
                        #어문관일때 선택식으로 인한 가격수정
                        menu_list[size][-1] = str(menu_list[size][i-1]).replace('가격 : ', '')
                    else:
                        menu_list[size][-1] = menu_list[size][-1].replace('가격 : ', '')
            except:
                pass
    con.close()

    return menu_list