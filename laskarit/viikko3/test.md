## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat User ja Todo, jotka kuvaavat käyttäjiä ja käyttäjien tehtäviä:

```mermaid
 classDiagram
      Ruutu ..> Pelilauta
      Noppa "2-8" -- Pelaaja
      Pelinappula ..> Pelaaja
      Pelinappula ..> Ruutu
      Pelaaja ..> Peli
      class Noppa{
      }
      class Pelaaja{
          id
      }
      class Pelilauta{
      }
      class Ruutu{
      }
      class Pelinappula {
      }
      class Peli {
      }
```
