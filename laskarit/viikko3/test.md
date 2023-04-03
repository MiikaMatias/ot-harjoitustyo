## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat User ja Todo, jotka kuvaavat käyttäjiä ja käyttäjien tehtäviä:

```mermaid
 classDiagram
      class Noppa{
      }
      class Pelaaja{
          id
      }
      class Pelilauta{
        id
      }
```

---
title: Animal example
---
classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }
