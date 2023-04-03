## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat User ja Todo, jotka kuvaavat käyttäjiä ja käyttäjien tehtäviä:

```mermaid
 classDiagram
      Todo "*" --> "1" User
      class User{
          username
          password
      }
      class Todo{
          id
          content
          done
      }
```