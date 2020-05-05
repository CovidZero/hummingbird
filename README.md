# CÓDIGO FORA DE UTILIZAÇÃO
# hummingbird-covidzero

Essa é uma aplicação criada para fornecer APIs de consulta de dados sobre
COVID-19. Dividimos a aplicação em duas partes, a primeira é uma cron que roda
de tempos em tempos para buscar dados atualizados sobre os casos e registrar em
uma base de dados para consulta e a segunda são as API para consulta dos dados
que são utilizadas pelos Clients.

## Como rodar

 - Para rodar com docker-compose:

```
docker-compose build
docker-compose up
```

## Cron - [Doing]

 - Roda uma busca na base: http://plataforma.saude.gov.br/novocoronavirus/resources/scripts/database.js
 - Registra os dados em um modelo de Report e Cases

## APIS - [ToDo]

