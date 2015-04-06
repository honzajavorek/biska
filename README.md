#BIS

##Implementace www stránky s přístupovým heslem, její bezpečnost a rychlost, ukázka útoku hrubou silou

V rámci práce vytvoříme testovací webovou stránku, zahrnující uživatelský účet. Budeme se zabývat také hlediskem 
zabezpečení této stránky a rychlostí jejího fungování. Zabezpečení webové stránky otestujeme demonstrací útoku
hrubou silou, kdy se pokusíme náhodně volit hesla a také použitím rainbow tables (tabulek obsahujících hashe,
pomocí nichž je možné nalézt shodu s hashem např. z odcizené databáze a získat tak heslo k účtu.

##Instalace 
    
    virtualenv bis
    source bis/bin/activate
    pip install -r requirements.txt
    
## Spuštění
Pro spuštění na adrese `http://localhost:8000/`

    python app.py runserver

Vytvorime uzivatele
    python app.py createsuperuser --username=admin --email=admin@test.com
    
##MD5
http://cs.wikipedia.org/wiki/Message-Digest_algorithm

## Hackovani rainbow tabulka

https://www.freerainbowtables.com

./rcracki_mt -h bae60998ffe4923b131e3d6e4c19993e "/media/vlinhart/My Passport/films/AAA/md5_loweralpha-numeric-space#1-8_0"

or faster and easier
http://www.md5crack.com/




    ?l = abcdefghijklmnopqrstuvwxyz
    ?u = ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ?d = 0123456789
    ?s = «space»!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    ?a = ?l?u?d?s
    ?b = 0x00 - 0xff


./hashcat-cli64.bin -m0 -a3 hashes.txt ?l?l?l
#all 3 chars
./hashcat-cli64.bin -m0 -a3 hashes.txt ?a?a?a
./hashcat-cli64.bin -m0 -a3 hashes.txt ?l?d?l?d?l?d?l?d?l?d?l?d?l?d?l?d 
./hashcat-cli64.bin -m0 -a3 hashes.txt ?d?d?d?d?d?d?l?l (123456az)