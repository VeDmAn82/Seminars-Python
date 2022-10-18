def ReadLastRow():
    data = open('text.txt', encoding='utf-8')     # utf-8 кодировка для русского языка
    print(data)
    text = data.readlines()
    print(text[-1])
    data.close()                                  # закрытие потока

# ['РјРѕСЂРѕР· Рё СЃРѕР»РЅС†Рµ\n', 'РґРµРЅСЊ С‡СѓРґРµСЃРЅС‹Р№']     - текст из файла