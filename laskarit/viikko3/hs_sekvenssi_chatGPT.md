## Chatgpt test
Uteliaisuuttani laitoin chatGPT:n tekemään tehtävän. Sinäänsä ikävää koska luulisi että tällaisen tehtävän delegoiminen kielimallille olisi juuri noiden osaamisalueen keskiössä, mutta veikkaan että tarvitaan aikamoista kikkailua että saadaan se tuottamaan oikeanlainen kaavio. 

"""
[ code ]

Teemme sekvenssikaavion mermaid kielellä md tiedostoon. Kirjoita kaavio näiden ohjeiden mukaan:

Kuvaa sekvenssikaaviona koodin main-funktion suorituksen aikaansaama toiminnallisuus.

Muista, että sekvenssikaaviossa tulee tulla ilmi kaikki mainin suorituksen aikaansaamat olioiden luomiset ja metodien kutsut!
"""


```mermaid
sequenceDiagram
    participant Kioski
    participant Matkakortti
    participant HKLLaitehallinto
    participant Lataajalaite
    participant Lukijalaite

    Kioski ->> Matkakortti: osta_matkakortti("Kalle")
    Note over Kioski,Matkakortti: luodaan uusi matkakortti<br/>omistajana "Kalle"<br/>alkusaldolla 0€
    Matkakortti -->> Kioski: uusi_kortti
    Kioski ->> Lataajalaite: lisaa_lataaja(rautatietori)
    Note over Kioski,Lataajalaite: lisätään rautatietori lataajaksi
    Lataajalaite -->> Kioski: 
    Kioski ->> Lukijalaite: lisaa_lukija(ratikka6)
    Note over Kioski,Lukijalaite: lisätään ratikka6 lukijaksi
    Lukijalaite -->> Kioski: 
    Kioski ->> Lukijalaite: lisaa_lukija(bussi244)
    Note over Kioski,Lukijalaite: lisätään bussi244 lukijaksi
    Lukijalaite -->> Kioski: 
    Kioski ->> Lataajalaite: lataa_arvoa(kallen_kortti, 3)
    Note over Kioski,Lataajalaite: lisätään 3€ saldoa Kallen kortille
    Lataajalaite ->> Matkakortti: kasvata_arvoa(3)
    Note over Lataajalaite,Matkakortti: lisätään 3€ kortin saldolle
    Matkakortti -->> Lataajalaite: 
    Kioski ->> Lukijalaite: osta_lippu(kallen_kortti, 0)
    Note over Kioski,Lukijalaite: yritetään ostaa ratikkalippua 1.50€
    Lukijalaite ->> Matkakortti: vahenna_arvoa(1.5)
    Note over Lukijalaite,Matkakortti: vähennetään 1.50€ kortin saldosta
    Matkakortti -->> Lukijalaite: 
    Lukijalaite ->> Kioski: true
    Note over Lukijalaite,Kioski: lippu ostettu onnistuneesti
    Kioski ->> Lukijalaite: osta_lippu(kallen_kortti, 2)
    Note over Kioski,Lukijalaite: yritetään ostaa seutulippua 3.50€
    Lukijalaite ->> Matkakortti: vahenna_arvoa(2.1)
    Note over Lukijalaite,Matkakortti: vähennetään 2.10€ kortin saldosta
    Matkakortti -->> Lukijalaite: 
    Lukijalaite ->> Kioski: true
    Note over Lukijalaite,Kioski: lippu ostettu onnistuneesti
```
