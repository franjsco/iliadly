#!/usr/bin/env python3
##################################################
#                     iliadly                    #
#      https://github.com/franjsco/iliadly       #
#                   @franjsco                    #
##################################################

from requests_html import HTMLSession
from colored import fg, bg, attr

URL_CONTATORI_ILIAD = 'https://www.iliad.it/account/consumi-e-credito'


def preleva_dati():
    # sesione html e get (esecuzione metodo render() per eseguire js)
    session = HTMLSession()
    res = session.get(URL_CONTATORI_ILIAD)
    res.html.render()

    # selettore css dei contatori
    sel_dati = 'div.conso-infos:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'
    sel_chiamate = 'div.conso-infos:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'
    sel_sms = 'div.conso-infos:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)'
    sel_mms = 'div.conso-infos:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)'
    sel_nome_offerta= '.page > h2:nth-child(1) > span:nth-child(1)'
    sel_scadenza_offerta = '.end_offerta'
    sel_credito = 'b.red'

    # ricerca dati mediante selettori e assegnazione valori nel dizionario
    dati = {
        "offerta": res.html.find(sel_nome_offerta, first=True).text.split('\n', 1)[0][7:].strip(),
        "credito": res.html.find(sel_credito, first=True).text.split('\n', 1)[0].strip(),
        "chiamate": res.html.find(sel_chiamate, first=True).text.split('\n', 1)[0][9:].strip(),
        "internet": res.html.find(sel_dati, first=True).text.split('\n', 1)[0].strip(),
        "sms": res.html.find(sel_sms, first=True).text.split('\n', 1)[0].strip(),
        "mms": res.html.find(sel_mms, first=True).text.split('\n', 1)[0].strip(),
        "scadenza": res.html.find(sel_scadenza_offerta, first=True).text[-10:].strip()
    }

    return dati


def stampa_contatori(dati):
    print('%s%s%s          iliadly          %s' % (fg(160), bg(15) ,attr(1), attr(0)))
    print('Offerta:%s%s %s %s' % (fg(1), attr(1), dati["offerta"], attr(0)))
    print('Scadenza:%s%s %s %s' % (fg(1) ,attr(1), dati["scadenza"], attr(0)))
    print('Credito:%s%s %s %s' % (fg(1), attr(1), dati["credito"], attr(0)))
    print('Chiamate:%s%s %s %s' % (fg(1), attr(1), dati["chiamate"], attr(0)))
    print('SMS:%s%s %s %s' % (fg(1) ,attr(1), dati["sms"], attr(0)))
    print('MMS:%s%s %s %s' % (fg(1),attr(1), dati["mms"], attr(0)))
    print('Dati:%s%s %s %s' % (fg(1) ,attr(1), dati["internet"], attr(0)))


def main():
    try:
        dati = preleva_dati()
    except:
        print('%s%siliadly: Errore nel prelevare i dati. Assicurati di essere connesso ad internet con SIM iliad. %s' % (fg(1), bg(0), attr(0)))
        exit(1)

    try:
        stampa_contatori(dati)
    except:
        print('%s%siliadly: Errore nella stampa a video dei contatori. %s' % (fg(1), bg(0), attr(0)))
        exit(1)


if __name__ == "__main__":
    main()
    exit(0)