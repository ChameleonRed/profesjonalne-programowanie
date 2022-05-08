"""
Gramatyka matematyki.

Około 4,5h projektowanie, programowanie, kodowania, testowanie izabawa.
Potrenowałem pisanie match/case, tokenizację i parsowanie.

start:
    wyrażenie spacje?

wyrażenie:
    | dodawanie (spacje? ('+'|'-') spacje? dodawanie)?

dodawanie:
    | mnożenie (spacje? ('*'|'-') spacje? mnożenie)?

mnożenie:
    | potęgowanie (spacje? ('*'|'-') spacje? potęgowanie)?

potęgowanie:
    | atom (spacje? ('**'|'^') spacje? atom)?

atom:
    | spacje? liczba_całkowita
    | spacje? liczba_zmiennoprzecinkowa
    | spacje? '(' spacje? wyrażenie spacje? ')'
    | spacje? 'log' spacje? '('spacje?  wyrażenie spacje? ',' spacje? wyrażenie spacje? ')'

"""

import dataclasses
import logging
import math
import re
import sys
from collections.abc import Generator


@dataclasses.dataclass
class Token:
    nazwa: str
    wartość: str
    pozycja: int


def obliczeniowy_tokenizator(input: str) -> Generator[Token, None, None]:
    pozycja = 0
    for token in re.finditer(
            r'(?P<int>\d+)'
            r'|(?P<float>(?:\d+\.\d*|\.\d+)(?:[eE][-+]\d+)?|\d+[eE][-+]\d+)'
            r'|(?P<identifier>\w+)'
            r'|(?P<plus>\+)'
            r'|(?P<minus>-)'
            r'|(?P<power>\^|\*\*)'
            r'|(?P<multiply>\*)'
            r'|(?P<divide>/)'
            r'|(?P<begin_parenthesis>\()' 
            r'|(?P<end_parenthesis>\))'
            r'|(?P<equal>==)'
            r'|(?P<coma>,)'
            r'|(?P<space>\s+)'
            r'|(?P<unknown>.+?)',
            input):
        yield Token(nazwa=token.lastgroup, wartość=token.group(0), pozycja=pozycja)
        pozycja += len(token.group(0))


class ObliczeniowyParserBłąd(Exception):
    pass


class ObliczeniowyParser:
    def __init__(self, tokenizator: Generator[Token, None, None]):
        self.tokenizator = tokenizator
        self.stos_stanów = []
        self.stos_tokenów = []
        self.stos = []

    def _weź_token(self):
        logging.debug('_weź_token')
        try:
            if self.stos_tokenów:
                token = self.stos_tokenów.pop()
            else:
                token = next(self.tokenizator)
            logging.debug('token %s', token)
            self.aktualny_token = token
            return token
        except StopIteration:
            logging.debug('Nie ma więcej tokenów.')
            return None

    def _zwróć_token(self, token):
        logging.debug('_zwróć_token')
        self.stos_tokenów.append(token)
        logging.debug('token %s', token)
        logging.debug('stos tokenów %s', self.stos_tokenów)

    def _weź_ze_stosu(self):
        logging.debug('_weź_ze_stosu')
        value = self.stos.pop()
        logging.debug('pobrano %s stos %s', value, self.stos)
        return value

    def _odłóż_na_stos(self, value):
        logging.debug('_odłóż_na_stos')
        self.stos.append(value)
        logging.debug('włożono %s stos %s', value, self.stos)

    def _początek_stanu(self):
        stan = sys._getframe(1).f_code.co_name
        logging.debug('-> %s początek', stan)
        self.stos_stanów.append(stan)
        logging.debug('stos stanów: %s', ' -> '.join(self.stos_stanów))

    def _koniec_stanu(self):
        stan = sys._getframe(1).f_code.co_name
        logging.debug('<- %s koniec', stan)
        self.stos_stanów.pop()
        logging.debug('stos stanów: %s', ' -> '.join(self.stos_stanów))

    def _zrób_przecinek(self):
        self._początek_stanu()
        while True:
            token = self._weź_token()
            match token:
                # ,
                case Token(nazwa='coma'):
                    return
                # spacja
                case Token(nazwa='space'):
                    continue
                # nie wiadomo co
                case _:
                    raise ObliczeniowyParserBłąd(token)

    def zrób_logarytm(self):
        while True:
            token = self._weź_token()
            match token:
                # (
                case Token(nazwa='begin_parenthesis'):
                    self._zrób_wyrażenie()
                    self._zrób_przecinek()
                    self._zrób_wyrażenie()
                    while True:
                        token = self._weź_token()
                        match token:
                            # )
                            case Token(nazwa='end_parenthesis'):
                                b = self._weź_ze_stosu()
                                a = self._weź_ze_stosu()
                                c = math.log(a, b)
                                logging.debug('-' * 60)
                                logging.debug('logarytm log(%s, %s) = %s', a, b, c)
                                logging.debug('-' * 60)
                                self._odłóż_na_stos(c)
                                self._koniec_stanu()
                                return
                            # spacja
                            case Token(nazwa='space'):
                                continue
                            # nie wiadomo co
                            case _:
                                raise ObliczeniowyParserBłąd(token)
                # spacja
                case Token(nazwa='space'):
                    continue

    def _zrób_atom(self):
        self._początek_stanu()
        while True:
            token = self._weź_token()
            match token:
                # spacja
                case Token(nazwa='space'):
                    continue
                # liczba całkowita
                case Token(nazwa='int'):
                    logging.debug('-' * 60)
                    logging.debug('atom = %s', token.wartość)
                    logging.debug('-' * 60)
                    self._odłóż_na_stos(int(token.wartość))
                    self._koniec_stanu()
                    return
                # liczba zmiennoprzecinkowa
                case Token(nazwa='float'):
                    logging.debug('-' * 60)
                    logging.debug('atom = %s', token.wartość)
                    logging.debug('-' * 60)
                    self._odłóż_na_stos(float(token.wartość))
                    self._koniec_stanu()
                    return
                # ( wyrażenie )
                case Token(nazwa='begin_parenthesis'):
                    self._zrób_wyrażenie()
                    while True:
                        token = self._weź_token()
                        match token:
                            # )
                            case Token(nazwa='end_parenthesis'):
                                self._koniec_stanu()
                                return
                            # spacja
                            case Token(nazwa='space'):
                                continue
                            # nie wiadomo co
                            case _:
                                raise ObliczeniowyParserBłąd(token)
                # function ( value, base )
                case Token(nazwa='identifier'):
                    match token.wartość:
                        case 'log':
                            self._zwróć_token(token)
                            self.zrób_logarytm()
                            return
                # koniec
                case None:
                    self._zwróć_token(token)
                    self._koniec_stanu()
                    return
                # nie wiadomo co
                case _:
                    raise ObliczeniowyParserBłąd(token)

    def _zrób_potęgowanie(self):
        self._początek_stanu()
        self._zrób_atom()
        while True:
            token = self._weź_token()
            match token:
                # spacja
                case Token(nazwa='space'):
                    continue
                # *
                case Token(nazwa='power'):
                    self._zrób_atom()
                    b = self._weź_ze_stosu()
                    a = self._weź_ze_stosu()
                    c = a ** b
                    logging.debug('-' * 60)
                    logging.debug('potęgowanie %s ** %s = %s', a, b, c)
                    logging.debug('-' * 60)
                    self._odłóż_na_stos(c)
                    continue
                # koniec
                case None:
                    self._zwróć_token(token)
                    self._koniec_stanu()
                    return
                # coś innego
                case _:
                    self._zwróć_token(token)
                    self._koniec_stanu()
                    return

    def _zrób_mnożenie(self):
        self._początek_stanu()
        self._zrób_potęgowanie()
        while True:
            token = self._weź_token()
            match token:
                # spacja
                case Token(nazwa='space'):
                    continue
                # *
                case Token(nazwa='multiply'):
                    self._zrób_potęgowanie()
                    b = self._weź_ze_stosu()
                    a = self._weź_ze_stosu()
                    c = a * b
                    logging.debug('-' * 60)
                    logging.debug('mnożenie %s * %s = %s', a, b, c)
                    logging.debug('-' * 60)
                    self._odłóż_na_stos(c)
                    continue
                # /
                case Token(nazwa='divide'):
                    self._zrób_potęgowanie()
                    b = self._weź_ze_stosu()
                    a = self._weź_ze_stosu()
                    c = a / b
                    logging.debug('-' * 60)
                    logging.debug('dzielenie %s / %s = %s', a, b, c)
                    logging.debug('-' * 60)
                    self._odłóż_na_stos(c)
                    continue
                # koniec
                case None:
                    self._zwróć_token(token)
                    self._koniec_stanu()
                    return
                # coś innego
                case _:
                    self._zwróć_token(token)
                    self._koniec_stanu()
                    return

    def _zrób_dodawanie(self):
        self._początek_stanu()
        self._zrób_mnożenie()
        while True:
            token = self._weź_token()
            match token:
                # spacja
                case Token(nazwa='space'):
                    continue
                # +
                case Token(nazwa='plus'):
                    self._zrób_mnożenie()
                    b = self._weź_ze_stosu()
                    a = self._weź_ze_stosu()
                    c = a + b
                    logging.debug('-' * 60)
                    logging.debug('dodawanie %s + %s = %s', a, b, c)
                    logging.debug('-' * 60)
                    self._odłóż_na_stos(c)
                    continue
                # -
                case Token(nazwa='minus'):
                    self._zrób_mnożenie()
                    b = self._weź_ze_stosu()
                    a = self._weź_ze_stosu()
                    c = a - b
                    logging.debug('-' * 60)
                    logging.debug('odejmowanie %s - %s = %s', a, b, c)
                    logging.debug('-' * 60)
                    self._odłóż_na_stos(c)
                    continue
                # koniec
                case None:
                    self._zwróć_token(token)
                    self._koniec_stanu()
                    return
                # coś innego
                case _:
                    self._zwróć_token(token)
                    self._koniec_stanu()
                    return

    def _zrób_wyrażenie(self):
        self._początek_stanu()
        logging.debug('zrób_wyrażenie początek')
        while True:
            token = self._weź_token()
            match token:
                # spacja
                case Token(nazwa='space'):
                    continue
                # koniec
                case None:
                    self._koniec_stanu()
                    return None
                # dodawanie
                case _:
                    self._zwróć_token(token)
                    self._zrób_dodawanie()
                    self._koniec_stanu()
                    return

    def parsuj(self) -> int | bool | None:
        self._zrób_wyrażenie()
        return self._weź_ze_stosu()


if __name__ == '__main__':
    format = '%(relativeCreated)5d | %(levelname).1s | %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=format)

    wyrażenie = '2 + 8 * 2 * (3 + 4) + (2 + 3) ^ (2 * 3 - 2) + log(16, 2)'
    logging.debug('-' * 60)
    logging.debug('Tokenizuj: %s.', wyrażenie)
    logging.debug('-' * 60)
    for x in obliczeniowy_tokenizator(wyrażenie):
        logging.debug(x)

    logging.debug('-' * 60)
    logging.debug('Parsuj: %s.', wyrażenie)
    logging.debug('-' * 60)
    parser = ObliczeniowyParser(obliczeniowy_tokenizator(wyrażenie))
    logging.debug('-' * 60)
    logging.debug('Wynik %s', parser.parsuj())
    logging.debug('-' * 60)

