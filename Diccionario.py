meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Una carita como reaccion a algo gracioso",
            "MEME": "Chiste que se puede ver en texto en imagen o en video",
            "CREEPY": "Una manera de decir algo de miedo o Terrorifico",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación"
            "AGGRO": "ponerse agresivo/enojado",
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
            
            
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Perdon no lo hemos encontrado")
