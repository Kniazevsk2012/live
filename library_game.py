def f(kol_pok, *card):
    card_copy = card[0]
    kol_past = 0
    while kol_past < kol_pok:
        past = kol_past % 2
        nex = (past + 1) % 2
        for i in range(len(card_copy[past])):
            for j in range(len(card_copy[past][i])):
                if i > 0 and i < len(card_copy[past]) - 1 and \
                        j > 0 and j < len(card_copy[past][i]) - 1:
                    kol_object = [0, 0, 0, 0]
                    i1 = i - 1
                    while i1 < i + 2:
                        j1 = j - 1
                        while j1 < j + 2:
                            if i1 != i or j1 != j:
                                kol_object[card_copy[past][i1][j1]] += 1
                            j1 += 1
                        i1 += 1
                    if card_copy[past][i][j] > 1:
                        if kol_object[card_copy[past][i][j]] >= 4 or \
                            kol_object[card_copy[past][i][j]] < 2:
                            card_copy[nex][i][j] = 1
                    else:
                        if card_copy[past][i][j] == 1:
                            uk = 2
                            while uk < len(kol_object) and \
                                card_copy[nex][i][j] == 1:
                                if kol_object[uk] == 3:
                                    card_copy[nex][i][j] = uk
                                uk += 1
        kol_past += 1
    return card_copy
