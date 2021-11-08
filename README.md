# Django ERP example
 
<a href="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160643.jpg"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160643.jpg" align="left" height="100" width="100" ></a>
<a href="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160713.jpg"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160713.jpg" align="left" height="100" width="100" ></a>
<a href="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160719.jpg"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160719.jpg" align="left" height="100" width="100" ></a>
<a href="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160725.jpg"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/IMG_20210705_160725.jpg" align="left" height="100" width="100" ></a>
<a href="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/gui.png"><img src="https://github.com/MarcinanBarbarzynca/Radwag-Scale-controller-with-MYSQL-communication/blob/main/images/gui.png" height="100" width="100" ></a>

# What is this?
Its a python app that is used to controll industrial Radwag scale. It use tkinter gui to display mass obtained by serial communication with scale. User is obligated to use controller connected to usb port to "SEND" result to server, "TARE" the scale and "WITHDRAW" the result from server. 

##  Why You need this?
If You want to send results from your scale directly to MySQL database its now possible. 

## Modules used
- pySerial
- Requests
- time

## How to use?
1. Connect scale to USB port wia R232 --> usb dongle... or DIY one
2. Check if Arduino IDE sees your scale. Try to write "normal" communicates to it first. You need to learn how to speak to your Scale. 
3. Adapt my code. 

### Related
- [Remote controller for this scale](https://github.com/MarcinanBarbarzynca/Pilot-do-komputera-Arduino-NANO "Remote controller for this scale")
- [How to read serial from scale](https://github.com/MarcinanBarbarzynca/Read-two-Arduino-serial-with-PYSerial "How to read serial from scale")
- [Scale emulator](https://github.com/MarcinanBarbarzynca/Emulator-wagi-radwag-arduino "Scale emulator")

#### Contact to me :)
Write 10 mails to p_ir@o2.pl


# BUGS! and how to deal with them
- It works slow. 
- Its crashing when it cannot open serial port
- It need some clearence. 

------------

# Co to jest?
To aplikacja pythonowa która pozwala na komunikację między komputerem, pilotem a wagą przemysłową Radwaga. Używa gui wygenerowanego w Tkinterze i wyświetla stan odczytany z portu seryjnego wagi. Użytkownik pomoże sterować procesami przy użyciu trzech przycisków na dodatkowym pilocie: "WYŚLIJ" który wysyła stan wagi do serwera z bazą danych, "TARUJ" który resetuje komunikację z wagą i rozkazuje jej odpowiednimi komendami tak aby przywrócić komunikację z komputerem, "COFNIJ" który cofa ostatnio wysłany wynik do serwera (inaczej wysyła wartość ujemną)

##  Why You need this?
Możesz szybko przesyłać wyniki z wagi do serwera bazodanowego. Możesz budować sobie własne makra przy użyciu mojego kodu. 

## Moduły użyte
- pySerial
- Requests
- time

## Jak używać?
1. Podłącz wagę do USB komputera. Możesz zakupić przejściówki RS232 --> usb lub samodzielnie takie coś wykonać. Ja używam modułów arduino CH340 i dodatków MAX3232
2. Sprawdź czy waga coś nadaje. Aby tego dokonać możesz podłączyć piny RX i TX do przejściówki MAX3232 lub wykorzystać inny sposób np. użyć arduino mega z wieloma portami uart. Następnie wykorzystaj kod pushthru aby podsłuchiwać komunikację między wagą a komputerem. Naucz się rozmawiać ze swoją wagą.
3. Adaptuj się

1. Uruchom list_all_ports0.2_pyserial.py. Ten program skanuje dostępne porty w poszukiwaniu wag i przypisanych do nich pilotów.
2. Zaczekaj aż uruchomi się okienko wagi. Może to potrwać 3*liczba portów com sekund... czyli w przypadku 8 portów com będzie to trwało ok 30 sekund. Czas ten jest można w przyszłości zoptymalizować, ale teraz działa wystarczająco dobrze. 
3. Jeżeli się nie uruchamia to przejdź do procedury naprawiania

- Wyświetlają się okienka z komunikatami o błędach!

## Jak naprawiać?
- Otwórz wybrany program w edytorze python IDE. Uruchom i sprawdź co wypisuje ci konsola pythona. Nie usunąłem jeszcze wiadomości służących do debugowania. 
- Uruchom Arduino IDE i sprawdź co wypisują porty do których jest podpięta waga i pilot. 
- Odpowiednio zmień plik ustawienia.txt. Znajdują się tam pary pilot-waga zapisane z pomocą odpowiedniej sekwencji znaków

## Będzie jeszcze instrukcja instalacji
1. Postaw element na szalce
2. Zaczekaj aż masa się ustabilizuje
3. Naciśnij odpowiedni przycisk: 
 - Wyślij -> wysyła masę z szalki do serwera
 - Cofnij -> wysyła masę do serwera, ale z ujemnym znakiem
 - Taruj -> Wysyła do wagi rozkaz tarowania i pisania bez przerwy w jednostce podstawowej. 

## Powiązane
- [Kontroler, pilot do wagi](https://github.com/MarcinanBarbarzynca/Pilot-do-komputera-Arduino-NANO "Kontroler, pilot do wagi")
- [Jak zbudować komunikator](https://github.com/MarcinanBarbarzynca/Read-two-Arduino-serial-with-PYSerial "Jak zbudować komunikator")
- [Wagi emulator](https://github.com/MarcinanBarbarzynca/Emulator-wagi-radwag-arduino "Wagi emulator")

#### Contact to me :)
Write 10 mails to p_ir@o2.pl


# BUGS! and how to deal with them
- Działa wolno. Wymaga optymalizacji i czyszczenia bufora odczytu i zapisu.
- Wywala się w momencie błędu użytkownika i braku portu com.
- Wymaga jeszcze trochę szlifów w kodzie. Bo wygląda on źle. 
