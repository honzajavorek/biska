#BIS

##Implementace www stránky s přístupovým heslem, její bezpečnost a rychlost, ukázka útoku hrubou silou

V rámci práce vytvoříme testovací webovou stránku, zahrnující uživatelský účet. Budeme se zabývat také hlediskem 
zabezpečení této stránky a rychlostí jejího fungování. Zabezpečení webové stránky otestujeme demonstrací útoku
hrubou silou, kdy se pokusíme náhodně volit hesla a také použitím rainbow tables (tabulek obsahujících hashe,
pomocí nichž je možné nalézt shodu s hashem např. z odcizené databáze a získat tak heslo k účtu).

##Instalace

Abychom mohli rozjet projekt, potřebujeme nainstalovat dva hlavní programy, kterými jsou sqliteman a virtualenv.
Pomocí sqlitemanu můžeme prohlížet obsah odcizené databáze (ze které budeme porovnávat hashe s cílem získat heslo
k uživatelskému účtu). Virtualenv nám vytváří izolované Python prostředí, které nám slouží k nainstalování knihovny
pro běh tohoto projektu (rojekt tedy není nainstalován do systému, ale do tohoto virtuálního prostředí). Příkazem
activate spustíme složku, aby bylo možné do ní instalovat knihovny.
    
    sudo aptitude install sqliteman virtualenv
    cd PycharmProjects/biska
    virtualenv bis
    source bis/bin/activate
    pip install -r requirements.txt
       
## Spuštění webové aplikace s přihlašovacím formulářem

Pro spuštění na adrese `http://localhost:8000/` 

    python app.py syncdb
    python app.py runserver
    
Vytvorime uzivatele
    python app.py createsuperuser --username=admin --email=admin@test.com
    
##MD5
http://cs.wikipedia.org/wiki/Message-Digest_algorithm

    python hackit.py

## Hackovani rainbow tabulka
Program na pouziti i duhove tabulky stazene odsud https://www.freerainbowtables.com. Pouzita jen ta nejmensi pro tyto znaky
a-z0-9 o max delce hesla 8 znaku. 

### Ukazka pouziteho hashe z pokusne DB

./rcracki_mt -h bae60998ffe4923b131e3d6e4c19993e "cesta k adresari s rainbow tabulkama"
   
    statistics
    -------------------------------------------------------
    plaintext found:                          1 of 1(100.00%)
    total disk access time:                   107.14s
    total cryptanalysis time:                 5.20s
    total pre-calculation time:               12.62s
    total chain walk step:                    49985001
    total false alarm:                        5544
    total chain walk step due to false alarm: 20415090

    result
    -------------------------------------------------------
    bae60998ffe4923b131e3d6e4c19993e	bad	hex:626164

###Ukazka dlouhe slovo - jen  pismena

./rcracki_mt -h e8dc4081b13434b45189a720b77b6818 "cesta k adresari s rainbow tabulkama"

    statistics
    -------------------------------------------------------
    plaintext found:                          1 of 1(100.00%)
    total disk access time:                   57.22s
    total cryptanalysis time:                 2.13s
    total pre-calculation time:               12.39s
    total chain walk step:                    49985001
    total false alarm:                        2240
    total chain walk step due to false alarm: 8190237
    
    result
    -------------------------------------------------------
    e8dc4081b13434b45189a720b77b6818	abcdefgh	hex:6162636465666768


###Ukazka kombinovana pismena a cisla

./rcracki_mt -h 11cfd4fab26bbf25df59f59fb8ccd9b1 "cesta k adresari s rainbow tabulkama"

    statistics
    -------------------------------------------------------
    plaintext found:                          1 of 1(100.00%)
    total disk access time:                   190.39s
    total cryptanalysis time:                 7.94s
    total pre-calculation time:               25.68s
    total chain walk step:                    99970002
    total false alarm:                        8075
    total chain walk step due to false alarm: 30700068
    
    result
    -------------------------------------------------------
    11cfd4fab26bbf25df59f59fb8ccd9b1	068877op	hex:3036383837376f70


Nebo to same na webu, bez nutnosti neco stahovat.
http://www.md5crack.com/


## Bruteforce pomoci Hascat

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