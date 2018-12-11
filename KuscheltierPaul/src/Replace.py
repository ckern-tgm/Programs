
#Replaces time for better wording
def replaceUhrzeit(Uhrzeit):
    # 09:30 -> 9 Uhr 30
    neueZeit = Uhrzeit
    # Erste Zahl überprüfen,wenn 0 dann weg
    if (neueZeit[0] == "0"):
        neueZeit = neueZeit[1:]
    #print(neueZeit)
    neueZeit = neueZeit.replace(":", " Uhr ")
    return neueZeit