import datetime 

def conselhos_da_avo(weather):
    dia_de_hoje = datetime.date.today().day
    for w in weather:
        dia = w['date'].split()[0]
        if (str(dia_de_hoje) == dia):
            if(w.get('temp_min',None) != None and w['temp_min'] < 15):
                print('Leva um casaco!')
            if(w.get('uv',None) != None and w['uv'] > 7):
                print('Sai do sol que faz mal!')

weather = [
    {
        "date": "2 Qui",
        "prev_txt": "Céu nublado por nuvens altas",
        "temp_min": 13, "temp_max": 28, "uv": 8
    },
    {
        "date": "5 Dom",
        "prev_txt": "Céu pouco nublado",
        "temp_min": 11, "temp_max": 27, "uv": 9
    },
    {
        "date": "6 Seg",
        "prev_txt": "Céu limpo",
        "temp_min": 9, "temp_max": 31
    }
]

conselhos_da_avo(weather)