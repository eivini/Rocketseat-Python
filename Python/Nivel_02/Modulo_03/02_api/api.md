## API - Application Programming Interface
+ Como faz quando um sistema quer conversar com outro?

# Palavra chave = interface > porta de entrada / uma forma de estabelecer essa comunicação

# Um sistema rodando que oferece uma API para que outro sistema consiga se conectar

# Ex:
+ Cliente -- request --> API -- passa a request --> API Server      (request == pergunta)
+ Cliente <-- response -- API <-- responde a request -- API Server      (response == resposta)
+ quando o cliente quiser requisitar alguma informação armazedada dentro daquele sistema (API Server)
+ ele vai enviar uma request para a API e a API vai passar a requisição para o servidor
+ depois dessa request o servidor vai responder para a API e a API vai responder para o cliente

# Outro ex:
+ o cliente ta acessando sua conta bancária e depois de acessar, ele quer recuperar o saldo dele, essa informação do saldo está em um sistema externo
+ então ele requisita o saldo dele via API para o servidor e o servidor que roda o sistema por trás vai recuperar essa informação e responder através do response

# O API é como se fosse uma ponte que permite que aplicativos diferentes troquem informações e funcionem juntos

# Para estabelecer uma comunicação temos que ter alguns parâmetros(regras) para que funcione

# Conceito de API REST - Representational State Transfer        (estilo de arquitetura para o desenvolvimento de API's)
+ conjuntode de regras que vai permitir que essa comunicação aconteça de forma fluida
+ essas regras precisam ser respeitadas para que essa comunicação realmente aconteça entre os sistemas
+ a principal ideia por trás do REST é que ele se baseia nos protocolos HTTP/s

## HTTP

    • GET
    • POST
    • PUT
    • DELETE
    • PATCH

## URL

    • /hello_word

## Último conceito de formato de representação
+ Cliente ----- HTTP ----- URL ----- Servidor
    com todos os métodos do http
    • GET
    • POST
    • PUT
    • DELETE
    • PATCH

    URL/hello_word

+ JSON ou XML são formas de devolver a informação para o cliente

## API Rest x API Restful
+ API Rest: é um estilo de arquitetura de desenvolvimento para api's (um conjunto de regras que devemos respeitar)
+ API Restful: se aplica a api's que já foram construidas e respeitam todos os principios do Rest