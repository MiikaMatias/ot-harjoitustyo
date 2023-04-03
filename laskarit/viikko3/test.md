## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat User ja Todo, jotka kuvaavat käyttäjiä ja käyttäjien tehtäviä:

```mermaid
 classDiagram
      Ruutu ..> Pelilauta
      Pelaaja ..> Noppa
      Pelaaja ..> Pelinappula
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
```
