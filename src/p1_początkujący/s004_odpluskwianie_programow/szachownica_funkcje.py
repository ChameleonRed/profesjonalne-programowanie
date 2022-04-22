from p1_początkujący.s002_szachownica_funkcje import ramki


def rysuj_górę(rozmiar):
    print(ramki.GORA_LEWO, end='')
    ostatnia_kolumna = rozmiar - 1
    for kolumna in range(rozmiar):
        print(ramki.POZIOM * 2, end='')
        if kolumna != ostatnia_kolumna:
            print(ramki.KRZYŻ_GÓRA, end='')
        else:
            print(ramki.GORA_PRAWO, end='')
    print()


def rysuj_rząd(rozmiar, rząd):
    print(ramki.PION, end='')
    for kolumna in range(rozmiar):
        if (kolumna + rząd) % 2 == 0:
            print('  ', end='')
        else:
            print('**', end='')
        print(ramki.PION, end='')
    print()


def rysuj_separator_rzędu(rozmiar):
    print(ramki.KRZYŻ_LEWO, end='')
    ostatnia_kolumna = rozmiar - 1
    for kolumna in range(rozmiar):
        print(ramki.POZIOM * 2, end='')
        if kolumna != ostatnia_kolumna:
            print(ramki.KRZYŻ, end='')
        else:
            print(ramki.KRZYŻ_PRAWO, end='')
    print()


def rysuj_dół(rozmiar):
    print(ramki.DOL_LEWO, end='')
    ostatnia_kolumna = rozmiar - 1
    for kolumna in range(rozmiar):
        print(ramki.POZIOM * 2, end='')
        if kolumna != ostatnia_kolumna:
            print(ramki.KRZYŻ_DOL, end='')
        else:
            print(ramki.DOL_PRAWO, end='')
    print()


def narysuj_szachownice(rozmiar):
    # rysuj górę
    rysuj_górę(rozmiar=rozmiar)
    # rysuj rzędy
    ostatni_rząd = rozmiar - 1
    for rząd in range(rozmiar):
        # rysuj rząd
        rysuj_rząd(rozmiar=rozmiar, rząd=rząd)
        # rysuj separator, jeśli nie ostatni rząd
        if rząd != ostatni_rząd:
            rysuj_separator_rzędu(rozmiar)
    # rysuj dół
    rysuj_dół(rozmiar=rozmiar)


def funkcja_główna():
    # narysuj szachownice
    narysuj_szachownice(rozmiar=8)


if __name__ == '__main__':
    funkcja_główna()
