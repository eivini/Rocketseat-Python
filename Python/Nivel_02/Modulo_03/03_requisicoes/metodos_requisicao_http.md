## Métodos de requisição HTTP   (request)
[x] Mozilla doc: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods
    
#   • GET   (Apenas retorna dados)
    O método GET solicita a representação de um recurso específico. Requisições utilizando o método GET devem retornar apenas dados.

#   • HEAD
    O método HEAD solicita uma resposta de forma idêntica ao método GET, porém sem conter o corpo da resposta.

#   • POST  (Insere dados a um recurso específico)
    O método POST é utilizado para submeter uma entidade a um recurso específico, frequentemente causando uma mudança no estado do recurso ou efeitos colaterais no servidor.

#   • PUT   (Atualiza dados existente, mas substitui todos as informações atuais ou seja, é obrigado a enviar tudo de novo)
    O método PUT substitui todas as atuais representações do recurso de destino pela carga de dados da requisição.

#   • DELETE    (Remove o dado especifico)
    O método DELETE remove um recurso específico.

#   • CONNECT
    O método CONNECT estabelece um túnel para o servidor identificado pelo recurso de destino.

#   • OPTIONS
    O método OPTIONS é usado para descrever as opções de comunicação com o recurso de destino.

#   • TRACE
    O método TRACE executa um teste de chamada loop-back junto com o caminho para o recurso de destino.

#   • PATCH (Atualiza modificações parciais)
    O método PATCH é utilizado para aplicar modificações parciais em um recurso.

# OBS: HEAD, CONNECT, OPTIONS e TRACE
    não são amplamente utilizados, então não teve explicação ate o momento