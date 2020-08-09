# miniature-broccoli
Этот бот парсит очень известный веб ресурс объявлений по недвижимости в Казахстане (создан в целях самообразования)
Его легко запустить в PyCharm или просто в консоле с Питоном не менее 3.8
Не забыть создать conf.yaml файл и там записать следующее:


#!/usr/bin/python3
# -*- coding: utf-8 -*-

---
TOKEN : '' # вставить токен своего бота
ADMIN: ''  # ввести свой пользователь

HOST : 'localhost'
USER : 'root'
PASSWORD : 'password'
DB : 'mysql'
CHARSET : 'utf8mb4'


MENU_0 : # ACTION
  - Выберете что вас интересует?
  - АРЕНДА # https://krisha.kz/arenda/kvartiry/
  - ПРОДАЖА # https://krisha.kz/prodazha/kvartiry/


MENU_1 : # TYPE
  - Какой тип недвижимости?
  - КВАРТИРЫ # https://krisha.kz/arenda/kvartiry/ https://krisha.kz/prodazha/kvartiry/
  - ДОМА # https://krisha.kz/prodazha/doma/
  - КОМНАТЫ # https://krisha.kz/arenda/komnaty/
  - ОФИСЫ
  - ПОМЕЩЕНИЯ
  - ЗДАНИЯ
  - МАГАЗИНЫ И БУТИКИ # https://krisha.kz/arenda/magazina/kyzylorda/
  - ПРОМБАЗЫ, СКЛАДЫ, ЗАВОДЫ
  - ПРОЧАЯ НЕДВИЖИМОСТЬ
  - ВОЗЬМУ В АРЕНДУ


MENU_2:
  - Выберете город?
  - НУР-СУЛТАН
  - АЛМАТЫ
  - КЫЗЫЛОРДА


MENU_3 : # ROOM NUMBER
  - Сколько комнат?
  - любой комнатности
  - 1 комнатная
  - 2 комнатная
  - 3 комнатная
  - 4 комнатная
  - 5 и более комнат

MENU_4: # RENT PERIOD
  - На какой срок?
  - по часам #  4 = hourly #  das[rent:period]=4
  - суточно # 1 = daily
  - помесячно # 2 = monthly
  - поквартально # 3 = quarterly
#
MENU_5:
  - С фото?
  - С фото
  - Нет

MENU_6:
  - От проверенных агенств?
  - От проверенных агенств
  - Нет

MENU_7:
  - От хозяев?
  - От хозяев
  - Нет

MENU_8:
  - Дешевые или дорогие?
  - Дешевые
  - Дорогие
#!/usr/bin/python3
# -*- coding: utf-8 -*-

---
TOKEN : '1134043221:AAEQ5Xsx_BQ7ibsgZ0SNjqK-yGni8esx6R0' # вставить токен своего бота
ADMIN: 'zduissekov'  # ввести свой пользователь

HOST : 'localhost'
USER : 'root'
PASSWORD : 'password'
DB : 'mysql'
CHARSET : 'utf8mb4'


MENU_0 : # ACTION
  - Выберете что вас интересует?
  - АРЕНДА # https://krisha.kz/arenda/kvartiry/
  - ПРОДАЖА # https://krisha.kz/prodazha/kvartiry/


MENU_1 : # TYPE
  - Какой тип недвижимости?
  - КВАРТИРЫ # https://krisha.kz/arenda/kvartiry/ https://krisha.kz/prodazha/kvartiry/
  - ДОМА # https://krisha.kz/prodazha/doma/
  - КОМНАТЫ # https://krisha.kz/arenda/komnaty/
  - ОФИСЫ
  - ПОМЕЩЕНИЯ
  - ЗДАНИЯ
  - МАГАЗИНЫ И БУТИКИ # https://krisha.kz/arenda/magazina/kyzylorda/
  - ПРОМБАЗЫ, СКЛАДЫ, ЗАВОДЫ
  - ПРОЧАЯ НЕДВИЖИМОСТЬ
  - ВОЗЬМУ В АРЕНДУ


MENU_2:
  - Выберете город?
  - НУР-СУЛТАН
  - АЛМАТЫ
  - КЫЗЫЛОРДА


MENU_3 : # ROOM NUMBER
  - Сколько комнат?
  - любой комнатности
  - 1 комнатная
  - 2 комнатная
  - 3 комнатная
  - 4 комнатная
  - 5 и более комнат

MENU_4: # RENT PERIOD
  - На какой срок?
  - по часам #  4 = hourly #  das[rent:period]=4
  - суточно # 1 = daily
  - помесячно # 2 = monthly
  - поквартально # 3 = quarterly
#
MENU_5:#!/usr/bin/python3
# -*- coding: utf-8 -*-

---
TOKEN : '1134043221:AAEQ5Xsx_BQ7ibsgZ0SNjqK-yGni8esx6R0' # вставить токен своего бота
ADMIN: 'zduissekov'  # ввести свой пользователь

HOST : 'localhost'
USER : 'root'
PASSWORD : 'password'
DB : 'mysql'
CHARSET : 'utf8mb4'


MENU_0 : # ACTION
  - Выберете что вас интересует?
  - АРЕНДА # https://krisha.kz/arenda/kvartiry/
  - ПРОДАЖА # https://krisha.kz/prodazha/kvartiry/


MENU_1 : # TYPE
  - Какой тип недвижимости?
  - КВАРТИРЫ # https://krisha.kz/arenda/kvartiry/ https://krisha.kz/prodazha/kvartiry/
  - ДОМА # https://krisha.kz/prodazha/doma/
  - КОМНАТЫ # https://krisha.kz/arenda/komnaty/
  - ОФИСЫ
  - ПОМЕЩЕНИЯ
  - ЗДАНИЯ
  - МАГАЗИНЫ И БУТИКИ # https://krisha.kz/arenda/magazina/kyzylorda/
  - ПРОМБАЗЫ, СКЛАДЫ, ЗАВОДЫ
  - ПРОЧАЯ НЕДВИЖИМОСТЬ
  - ВОЗЬМУ В АРЕНДУ


MENU_2:
  - Выберете город?
  - НУР-СУЛТАН
  - АЛМАТЫ
  - КЫЗЫЛОРДА


MENU_3 : # ROOM NUMBER
  - Сколько комнат?
  - любой комнатности
  - 1 комнатная
  - 2 комнатная
  - 3 комнатная
  - 4 комнатная
  - 5 и более комнат

MENU_4: # RENT PERIOD
  - На какой срок?
  - по часам #  4 = hourly #  das[rent:period]=4
  - суточно # 1 = daily
  - помесячно # 2 = monthly#!/usr/bin/python3
# -*- coding: utf-8 -*-

---
TOKEN : '1134043221:AAEQ5Xsx_BQ7ibsgZ0SNjqK-yGni8esx6R0' # вставить токен своего бота
ADMIN: 'zduissekov'  # ввести свой пользователь

HOST : 'localhost'
USER : 'root'
PASSWORD : 'password'
DB : 'mysql'
CHARSET : 'utf8mb4'


MENU_0 : # ACTION
  - Выберете что вас интересует?
  - АРЕНДА # https://krisha.kz/arenda/kvartiry/
  - ПРОДАЖА # https://krisha.kz/prodazha/kvartiry/


MENU_1 : # TYPE
  - Какой тип недвижимости?
  - КВАРТИРЫ # https://krisha.kz/arenda/kvartiry/ https://krisha.kz/prodazha/kvartiry/
  - ДОМА # https://krisha.kz/prodazha/doma/
  - КОМНАТЫ # https://krisha.kz/arenda/komnaty/
  - ОФИСЫ
  - ПОМЕЩЕНИЯ
  - ЗДАНИЯ
  - МАГАЗИНЫ И БУТИКИ # https://krisha.kz/arenda/magazina/kyzylorda/
  - ПРОМБАЗЫ, СКЛАДЫ, ЗАВОДЫ
  - ПРОЧАЯ НЕДВИЖИМОСТЬ
  - ВОЗЬМУ В АРЕНДУ


MENU_2:
  - Выберете город?
  - НУР-СУЛТАН
  - АЛМАТЫ
  - КЫЗЫЛОРДА


MENU_3 : # ROOM NUMBER
  - Сколько комнат?
  - любой комнатности
  - 1 комнатная
  - 2 комнатная
  - 3 комнатная
  - 4 комнатная
  - 5 и более комнат

MENU_4: # RENT PERIOD
  - На какой срок?
  - по часам #  4 = hourly #  das[rent:period]=4
  - суточно # 1 = daily
  - помесячно # 2 = monthly
  - поквартально # 3 = quarterly
#
MENU_5:
  - С фото?
  - С фото
  - Нет

MENU_6:
  - От проверенных агенств?
  - От проверенных агенств
  - Нет

MENU_7:
  - От хозяев?
  - От хозяев
  - Нет

MENU_8:
  - Дешевые или дорогие?
  - Дешевые
  - Дорогие


#MENU_9:  #ASTANA
#  - astana-almatinskij
#  - astana-esilskij
#  - astana-saryarkinskij
#  - r-n-bajkonur
#
#MENU_10:  #ALMATY
#  - almaty-aujezovskij
#  - almaty-alatauskij
#  - almaty-bostandykskij
#  - almaty-zhetysuskij
#  - almaty-medeuskij
#  - almaty-nauryzbajskiy
#  - almaty-turksibskij


url_dict:  # TRANSLATE TO URL
  'АРЕНДА': 'arenda'
  'ПРОДАЖА': 'prodazha'
  'КВАРТИРЫ': 'kvartiry'
  'ДОМА' : 'doma'
  'НУР-СУЛТАН' : 'nur-sultan'
  'АЛМАТЫ' : 'almaty'
  'КЫЗЫЛОРДА' : 'kyzylorda'

params_dict:
  'по часам' : 'das[rent.period]=4'       #   4 = hourly
  'суточно' : 'das[rent.period]=1'        #   1 = daily
  'помесячно' : 'das[rent.period]=2'      #   2 = monthly
  'поквартально' : 'das[rent.period]=3'   #   3 = quarterly
  '1 комнатная' : 'das[live.rooms]=1'
  '2 комнатная' : 'das[live.rooms]=2'
  '3 комнатная' : 'das[live.rooms]=3'
  '4 комнатная' : 'das[live.rooms]=4'
  '5 и более комнат' : 'das[live.rooms]=5'
  'С фото' : 'das[_sys.hasphoto]=1'  # has a photo?
  'От проверенных агенств' : 'das[checked]=1'  # from th owner
  'Новостройки' : 'das[novostroiki]=1'
  'От хозяев' : 'das[who]=1'  # from th owner
  'Дешевые' : 'sort_by=price-asc'
  'Дорогие' : 'sort_by=price-desc'

#  das[live:square][from]=13
#  das[live:square][to]=31
#  das[price][from]=111
#  das[price][to]=999&

  - поквартально # 3 = quarterly
#
MENU_5:
  - С фото?
  - С фото
  - Нет

MENU_6:
  - От проверенных агенств?
  - От проверенных агенств
  - Нет

MENU_7:
  - От хозяев?
  - От хозяев
  - Нет

MENU_8:
  - Дешевые или дорогие?
  - Дешевые
  - Дорогие


#MENU_9:  #ASTANA
#  - astana-almatinskij
#  - astana-esilskij
#  - astana-saryarkinskij
#  - r-n-bajkonur
#
#MENU_10:  #ALMATY
#  - almaty-aujezovskij
#  - almaty-alatauskij
#  - almaty-bostandykskij
#  - almaty-zhetysuskij
#  - almaty-medeuskij
#  - almaty-nauryzbajskiy
#  - almaty-turksibskij


url_dict:  # TRANSLATE TO URL
  'АРЕНДА': 'arenda'
  'ПРОДАЖА': 'prodazha'
  'КВАРТИРЫ': 'kvartiry'
  'ДОМА' : 'doma'
  'НУР-СУЛТАН' : 'nur-sultan'
  'АЛМАТЫ' : 'almaty'
  'КЫЗЫЛОРДА' : 'kyzylorda'

params_dict:
  'по часам' : 'das[rent.period]=4'       #   4 = hourly
  'суточно' : 'das[rent.period]=1'        #   1 = daily
  'помесячно' : 'das[rent.period]=2'      #   2 = monthly
  'поквартально' : 'das[rent.period]=3'   #   3 = quarterly
  '1 комнатная' : 'das[live.rooms]=1'
  '2 комнатная' : 'das[live.rooms]=2'
  '3 комнатная' : 'das[live.rooms]=3'
  '4 комнатная' : 'das[live.rooms]=4'
  '5 и более комнат' : 'das[live.rooms]=5'
  'С фото' : 'das[_sys.hasphoto]=1'  # has a photo?
  'От проверенных агенств' : 'das[checked]=1'  # from th owner
  'Новостройки' : 'das[novostroiki]=1'
  'От хозяев' : 'das[who]=1'  # from th owner
  'Дешевые' : 'sort_by=price-asc'
  'Дорогие' : 'sort_by=price-desc'

#  das[live:square][from]=13
#  das[live:square][to]=31
#  das[price][from]=111
#  das[price][to]=999&

  - С фото?
  - С фото
  - Нет

MENU_6:
  - От проверенных агенств?
  - От проверенных агенств
  - Нет

MENU_7:
  - От хозяев?
  - От хозяев
  - Нет

MENU_8:
  - Дешевые или дорогие?
  - Дешевые
  - Дорогие


#MENU_9:  #ASTANA
#  - astana-almatinskij
#  - astana-esilskij
#  - astana-saryarkinskij
#  - r-n-bajkonur
#
#MENU_10:  #ALMATY
#  - almaty-aujezovskij
#  - almaty-alatauskij
#  - almaty-bostandykskij
#  - almaty-zhetysuskij
#  - almaty-medeuskij
#  - almaty-nauryzbajskiy
#  - almaty-turksibskij


url_dict:  # TRANSLATE TO URL
  'АРЕНДА': 'arenda'
  'ПРОДАЖА': 'prodazha'
  'КВАРТИРЫ': 'kvartiry'
  'ДОМА' : 'doma'
  'НУР-СУЛТАН' : 'nur-sultan'
  'АЛМАТЫ' : 'almaty'
  'КЫЗЫЛОРДА' : 'kyzylorda'

params_dict:
  'по часам' : 'das[rent.period]=4'       #   4 = hourly
  'суточно' : 'das[rent.period]=1'        #   1 = daily
  'помесячно' : 'das[rent.period]=2'      #   2 = monthly
  'поквартально' : 'das[rent.period]=3'   #   3 = quarterly
  '1 комнатная' : 'das[live.rooms]=1'
  '2 комнатная' : 'das[live.rooms]=2'
  '3 комнатная' : 'das[live.rooms]=3'
  '4 комнатная' : 'das[live.rooms]=4'
  '5 и более комнат' : 'das[live.rooms]=5'
  'С фото' : 'das[_sys.hasphoto]=1'  # has a photo?
  'От проверенных агенств' : 'das[checked]=1'  # from th owner
  'Новостройки' : 'das[novostroiki]=1'
  'От хозяев' : 'das[who]=1'  # from th owner
  'Дешевые' : 'sort_by=price-asc'
  'Дорогие' : 'sort_by=price-desc'

#  das[live:square][from]=13
#  das[live:square][to]=31
#  das[price][from]=111
#  das[price][to]=999&


#MENU_9:  #ASTANA
#  - astana-almatinskij
#  - astana-esilskij
#  - astana-saryarkinskij
#  - r-n-bajkonur
#
#MENU_10:  #ALMATY
#  - almaty-aujezovskij
#  - almaty-alatauskij
#  - almaty-bostandykskij
#  - almaty-zhetysuskij
#  - almaty-medeuskij
#  - almaty-nauryzbajskiy
#  - almaty-turksibskij


url_dict:  # TRANSLATE TO URL
  'АРЕНДА': 'arenda'
  'ПРОДАЖА': 'prodazha'
  'КВАРТИРЫ': 'kvartiry'
  'ДОМА' : 'doma'
  'НУР-СУЛТАН' : 'nur-sultan'
  'АЛМАТЫ' : 'almaty'
  'КЫЗЫЛОРДА' : 'kyzylorda'

params_dict:
  'по часам' : 'das[rent.period]=4'       #   4 = hourly
  'суточно' : 'das[rent.period]=1'        #   1 = daily
  'помесячно' : 'das[rent.period]=2'      #   2 = monthly
  'поквартально' : 'das[rent.period]=3'   #   3 = quarterly
  '1 комнатная' : 'das[live.rooms]=1'
  '2 комнатная' : 'das[live.rooms]=2'
  '3 комнатная' : 'das[live.rooms]=3'
  '4 комнатная' : 'das[live.rooms]=4'
  '5 и более комнат' : 'das[live.rooms]=5'
  'С фото' : 'das[_sys.hasphoto]=1'  # has a photo?
  'От проверенных агенств' : 'das[checked]=1'  # from th owner
  'Новостройки' : 'das[novostroiki]=1'
  'От хозяев' : 'das[who]=1'  # from th owner
  'Дешевые' : 'sort_by=price-asc'
  'Дорогие' : 'sort_by=price-desc'

#  das[live:square][from]=13
#  das[live:square][to]=31
#  das[price][from]=111
#  das[price][to]=999&

