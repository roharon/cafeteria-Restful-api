from bs4 import BeautifulSoup
import datetime, requests


def seo_crawl(cafeteria, date):
    today = datetime.date.today()
    t = ['월', '화', '수', '목', '금', '토', '일']
    r = datetime.datetime.today().weekday()
    days = t[r]

    if date == 'tomorrow':
        today = today + datetime.timedelta(days=1)

    today_d = today.strftime("%Y%m%d")
    today_w = today.strftime("%w")
    ##today_d = "20170615"
    try:
        if cafeteria == 'inmoon':
            req = requests.get(
                'https://wis.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + today_d + '&endDt=' + today_d + '&caf_name=인문관식당&caf_id=h101')
        elif cafeteria == 'gyosoo':
            req = requests.get(
                'https://wis.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + today_d + '&endDt=' + today_d + '&caf_name=교수회관식당&caf_id=h102')
        elif cafeteria == 'sky':
            req = requests.get(
                'https://wis.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + today_d + '&endDt=' + today_d + '&caf_name=스카이라운지&caf_id=h103')
        else:
            raise
            # cafeteria 파라미터가 알맞지 않는 경우 오류 발생시킴.
    except:
        error = "\n서울캠 로딩. 학교 사이트 점검중!\n학식내용을 불러올 수 없습니다."
        return error

    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    my_titles = soup.select(
        'tr'
    )
    data = []
    cafe_menu = []

    for title in my_titles:
        data.append(title.text)

    for i in data:
        if len(data) == 1:

            cafe_menu.append(i)
            return "                "
        else:
            if "\n" in i:

                i = i.replace('\n', ' ').replace('&', ' ').replace('*', ' ').split()

                if '메뉴는' in i[1]:
                    # 교수회관
                    break
                elif '닭강정-' in i[0]:
                    # 인문관
                    break
                elif '※' in i[0]:
                    # 스카이라운지
                    break
                cafe_menu.append(i)

    menu_size = len(cafe_menu)
    menu = \
    {
        "title": [],
        "time": [],
        "food": [],
        "price": [],
        "cal": []
    }
    count = -1
    print(cafe_menu)
    for size in range(1, menu_size):
        time_size = len(cafe_menu[size])
        if today_w == "6":  # 0은 일요일 6은 토요일
            if '인문관' in cafeteria:
                if size in [1, 3, 4]:
                    continue

        menu['food'].append([])
        for what in range(0, time_size):
            if what == 0:
                menu['title'].append(cafe_menu[size][what][:-9])
                menu['time'].append(cafe_menu[size][what][-9:])

            elif what == (time_size - 1):
                menu['price'].append(cafe_menu[size][what])

            elif cafe_menu[size][what].isdigit() == 1:
                # Kcal앞 숫자.
                menu['cal'].append(cafe_menu[size][what] + " Kcal")
            else:
                if 'Kcal' == cafe_menu[size][what]:
                    pass
                else:
                    menu['food'][-1].append(cafe_menu[size][what])

    return menu
"""
    if "인문관" in cafeteria:
        ##인문관 일요일 hfspn 뜨는 오류 수정
        size = len(menu)
        for i in range(0, size):
            if 'hfspn' in menu[i]:
                pass
            if days == "토":
                for i in range(menu['title']):
                    if "1100~1430" in menu['title'][i]:
                        menu['title'][i] = menu[title][i].replace()
                menu['title'] = menu['title'].replace("1100~1430", "1100~1400")
"""


def glo_crawl(cafeteria, date):
    today = datetime.date.today()
    t = ['월', '화', '수', '목', '금', '토', '일']
    r = datetime.datetime.today().weekday()
    days = t[r]

    if date == 'tomorrow':
        today = today + datetime.timedelta(days=1)
        r = datetime.datetime.today().weekday()
        days = t[r]
    elif date == 'test':
        today = today + datetime.timedelta(days=3)
        r = datetime.datetime.today().weekday()
        days = t[r]

    today_d = today.strftime("%Y%m%d")
    end_d = today_d

    today_w = today.strftime("%w")

    today_d = end_d = "20181211"
    try:
        if cafeteria == "hooseng":
            req = requests.get(
                'https://webs.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + today_d + '&endDt=' + end_d + '&caf_name=후생관+학생식당&caf_id=h203')
        elif cafeteria == "umoon":
            req = requests.get(
                'https://webs.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + today_d + '&endDt=' + end_d + '&caf_name=어문관&caf_id=h204')
        elif cafeteria == "hufsdorm":
            req = requests.get(
                'https://webs.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + today_d + '&endDt=' + end_d + '&caf_name=HufsDorm+식당&caf_id=h205')
        elif cafeteria == "faculty_member":
            req = requests.get(
                'https://webs.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + today_d + '&endDt=' + end_d + '&caf_name=후생관+교직원식당&caf_id=h202')
        elif cafeteria == "training_center":
            req = requests.get(
                'https://webs.hufs.ac.kr/jsp/HUFS/cafeteria/viewWeek.jsp?startDt=' + today_d + '&endDt=' + end_d + '&caf_name=국제사회교육원식당&caf_id=h201')
    except:
        error = "\n글로벌캠 로딩. 학교 사이트 점검중!\n학식내용을 불러올 수 없습니다."
        return error

    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    my_titles = soup.select(
        'tr'
    )
    data = []
    cafe_menu = []

    for title in my_titles:
        title.text.replace('일품1', '일품 ')
        title.text.replace('일품2', '일품 ')
        title.text.replace('일품3', '일품 ')
        data.append(title.text)

    for i in data:
        if len(data) == 1:
            cafe_menu.append(i)
            return "         "
        else:
            if "\n" in i:
                if "방학 중" in i:
                    break
                elif '우리 식당은' in i:
                    break
                elif '농협' in i:
                    break
                else:
                    if 'umoon' in cafeteria:
                        if '1430' in i:
                            continue

                    i = i.replace('\n', ' ').replace('&', '').replace('*', '').split()
                    cafe_menu.append(i)

    menu_size = len(cafe_menu)
    count = -1

    menu = \
    {
        "title": [],
        "time": [],
        "food": [],
        "price": [],
        "cal": []
    }

    if cafeteria == "umoon":
        menu_size = len(cafe_menu) - 1

    for size in range(1, menu_size):
        time_size = len(cafe_menu[size])
        ##menu = menu + '\n----------------\n'
        count += 1
        menu['food'].append([])
        for what in range(0, time_size):

            if what == (time_size - 1):
                if cafeteria == "training_center":
                    menu['menu'].append(list(cafe_menu[size][what]))
                elif cafeteria == 'umoon':
                    
                    if size > 1:
                        try:
                            menu['price'].append(cafe_menu[size][what])
                        except:
                            pass
                    else:
                        menu['price'].append(cafe_menu[size][what])
                else:
                    if "QUOT" in cafe_menu[size][what]:
                        break
                        # 후생관 QUOT; 분식가격 나오는 코드 
                    menu['price'].append(cafe_menu[size][what])
            elif what == 0:
                if cafeteria == 'umoon':
                    if '1430' in cafe_menu[size][what]:
                        continue
                    else:
                        if '일품' in cafe_menu[size][what]:
                            menu['title'].append(cafe_menu[size][what])
                        else:
                            try:
                                if '면' in cafe_menu[size][what]:
                                    menu['title'].append(cafe_menu[size][what])
                                else:
                                    menu[count].append(cafe_menu[size][what] + ' : ')
                            except:
                                print("Umoon error-select.")
                                break
                else:
                    try:
                        pass
                    except:
                        print("haksik_pre 기숙사 식당 시간오류")
                    if cafe_menu[size][what] not in ['상기', '※']:
                        menu['title'].append(cafe_menu[size][what][:-9])
                        menu['time'].append(cafe_menu[size][what][-9:])

            else:
                if cafeteria != 'umoon':
                    try:
                        if len(menu['title']) < len(menu['food']):
                            break
                        else:
                            if cafeteria == 'hufsdorm':
                                if '등록된' in cafe_menu[size][what]:
                                    continue
                                # 기숙사식당 스넥 등록된 메뉴 없을때 조치
                            if ('(' or '+' or '/' or 'Kcal') in cafe_menu[size][what]:
                                continue
                            menu['food'][-1].append(cafe_menu[size][what])
                    except:
                        pass
        

    if cafeteria == 'umoon':
        umoon_temp = []
        umoon_select = ''
        umoon_size = int(len(menu))

        for i in range(0, umoon_size):

            if '일품' in menu[i]:
                continue
            else:
                menu[i] = menu[i].replace('\n', '')
                if '' == menu[i]:
                    continue
                elif '자장면' in menu[i]:
                    continue
                elif '\n' in menu[-1]:
                    menu[-1].replace('\n', '')
                else:
                    umoon_temp.append(menu[i])

        for i in range(int(len(umoon_temp) / 2)):
            umoon_select += str(umoon_temp[2 * i]) + '  ' + str(umoon_temp[2 * i + 1]) + '\n'
        try:
            if umoon_temp[-1] not in umoon_select:
                umoon_select += '\n' + umoon_temp[-1]
        except:
            pass
        umoon_select = menu[0] + umoon_select
        menu = [umoon_select]
    
    return menu


if __name__ == "__main__":
    print(glo_crawl('hooseng', 'today'))
    print(seo_crawl('inmoon', 'today'))