## Métodos de respostas HTTP   (response)
[x] Mozilla: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status

#   • Respostas Informativas (100 – 199)

#   • Respostas bem-sucedidas (200 – 299)

#   • Mensagens de redirecionamento (300 – 399)

#   • Respostas de erro do cliente (400 – 499)

#   • Respostas de erro do servidor (500 – 599)

##  Respostas informativas

#   • 100 - 199

    [100] Continue
    Essa resposta provisória indica que o cliente deve continuar a solicitação ou ignorar a resposta se a solicitação já estiver concluída.

    [101] Switching Protocols
    Esse código é enviado em resposta a um cabeçalho de solicitação Upgrade do cliente e indica o protocolo para o qual o servidor está mudando.

    [102] Processing (WebDAV)
    Este código indica que o servidor recebeu e está processando a requisição, mas nenhuma resposta está disponível ainda.

    [103] Early Hints Experimental
    Este código de status destina-se principalmente a ser usado com o cabeçalho Link, permitindo que o agente do usuário inicie o pré-carregamento recursos enquanto o servidor prepara uma resposta.

##  Respostas bem-sucedidas

#   • 200 - 299

    [200] OK
    A solicitação foi bem-sucedida. O significado do resultado de "sucesso" depende do método HTTP:

    GET: O recurso foi obtido e transmitido no corpo da mensagem.
    HEAD: Os cabeçalhos de representação são incluídos na resposta sem nenhum corpo de mensagem.
    PUT ou POST: O recurso que descreve o resultado da ação é transmitido no corpo da mensagem.
    TRACE: O corpo da mensagem contém a mensagem de requisição recebida pelo servidor.

    [201] Created
    A requisição foi bem sucedida e um novo recurso foi criado como resultado. Esta é normalmente a resposta enviada após as solicitações POST ou algumas solicitações PUT.

    [202] Accepted
    A solicitação foi recebida, mas ainda não foi atendida. É sem compromisso, pois não há como no HTTP enviar posteriormente uma resposta assíncrona indicando o resultado da solicitação. Destina-se a casos em que outro processo ou servidor manipula a solicitação ou processamento em lote.

    [203] Non-Authoritative Information
    Esse código de resposta significa que os metadados retornados não são exatamente os mesmos que estão disponíveis no servidor de origem, mas são coletados de uma cópia local ou de terceiros. Isso é usado principalmente para espelhos ou backups de outro recurso. Exceto para esse caso específico, a resposta 200 OK é preferida a este status.

    [204] No Content
    Não há conteúdo para enviar para esta solicitação, mas os cabeçalhos podem ser úteis. O agente do usuário pode atualizar seus cabeçalhos em cache para este recurso com os novos.

    [205] Reset Content
    Diz ao agente do usuário para redefinir o documento que enviou esta solicitação.

    [206] Partial Content
    Este código de resposta é usado quando o cabeçalho Range é enviado do cliente para solicitar apenas parte de um recurso.

    [207] Multi-Status (WebDAV)
    Transmite informações sobre vários recursos, para situações em que vários códigos de status podem ser apropriados.

    [208] Already Reported (WebDAV)
    Usado dentro de um elemento de resposta <dav:propstat> para evitar enumerar repetidamente os membros internos de várias ligações para a mesma coleção.

    [226] IM Used (HTTP Delta encoding)
    O servidor atendeu a uma solicitação GET para o recurso e a resposta é uma representação do resultado de uma ou mais manipulações de instância aplicadas à instância atual.

##  Mensagens de redirecionamento

#   • 300 - 399

    [300] Multiple Choices
    A solicitação tem mais de uma resposta possível. O agente do usuário ou usuário deve escolher um deles. (Não há uma maneira padronizada de escolher uma das respostas, mas links HTML para as possibilidades são recomendados para que o usuário possa escolher).

    [301] Moved Permanently
    A URL do recurso solicitado foi alterada permanentemente. A nova URL é fornecida na resposta.

    [302] Found
    Este código de resposta significa que o URI do recurso solicitado foi alterado temporariamente. Outras alterações no URI podem ser feitas no futuro. Portanto, esta mesma URI deve ser utilizada pelo cliente em requisições futuras.

    [303] See Other
    O servidor enviou esta resposta para direcionar o cliente a obter o recurso solicitado em outro URI com uma solicitação GET.

    [304] Not Modified
    É usado para fins de cache. Ele informa ao cliente que a resposta não foi modificada, portanto, o cliente pode continuar a usar a mesma versão em cache da resposta.

    [305] Use Proxy Deprecated
    Definido em uma versão anterior da especificação HTTP para indicar que uma resposta solicitada deve ser acessada por um proxy. Foi descontinuado devido a questões de segurança em relação à configuração em banda de um proxy.

    [306] unused Deprecated
    Esse código de resposta não é mais usado, é apenas reservado. Foi usado em uma versão anterior da especificação HTTP/1.1.

    [307] Temporary Redirect
    O servidor envia esta resposta para direcionar o cliente a obter o recurso solicitado em outra URI com o mesmo método usado na solicitação anterior. Tem a mesma semântica do código de resposta HTTP 302 Found, com a exceção de que o agente do usuário não deve alterar o método HTTP usado: se um POST foi usado na primeira solicitação, um POST deve ser usado no segundo pedido.

    [308] Permanent Redirect
    Isso significa que o recurso agora está permanentemente localizado em outro URI, especificado pelo cabeçalho de resposta HTTP Location:. Isso tem a mesma semântica que o código de resposta HTTP 301 Moved Permanently, com a exceção de que o agente do usuário não deve alterar o método HTTP usado: se um POST foi usado na primeira solicitação, um POST deve ser usado no segundo pedido.

##  Respostas de erro do cliente

#   • 400 - 499

    [400] Bad Request
    O servidor não pode ou não irá processar a solicitação devido a algo que é percebido como um erro do cliente (por exemplo, sintaxe de solicitação malformada, enquadramento de mensagem de solicitação inválida ou roteamento de solicitação enganosa).

    [401] Unauthorized
    Embora o padrão HTTP especifique "unauthorized", semanticamente, essa resposta significa "unauthenticated". Ou seja, o cliente deve se autenticar para obter a resposta solicitada.

    [402] Payment Required Experimental
    Este código de resposta está reservado para uso futuro. O objetivo inicial da criação deste código era usá-lo para sistemas digitais de pagamento, no entanto, este código de status é usado raramente e não existe nenhuma convenção padrão.

    [403] Forbidden
    O cliente não tem direitos de acesso ao conteúdo; ou seja, não é autorizado, portanto o servidor está se recusando a fornecer o recurso solicitado. Ao contrário do 401 Unauthorized, a identidade do cliente é conhecida pelo servidor.

    [404] Not Found
    O servidor não pode encontrar o recurso solicitado. No navegador, isso significa que o URL não é reconhecido. Em uma API, isso também pode significar que o endpoint é válido, mas o próprio recurso não existe. Os servidores também podem enviar esta resposta em vez de 403 Forbidden para ocultar a existência de um recurso de um cliente não autorizado. Este código de resposta é provavelmente o mais conhecido devido à sua ocorrência frequente na web.

    [405] Method Not Allowed
    O método de solicitação é conhecido pelo servidor, mas não é suportado pelo recurso de destino. Por exemplo, uma API pode não permitir chamar DELETE para remover um recurso.

    [406] Not Acceptable
    Esta resposta é enviada quando o servidor web, após realizar negociação de conteúdo orientada pelo servidor, não encontra nenhum conteúdo que esteja em conformidade com os critérios fornecidos por o agente do usuário.

    [407] Proxy Authentication Required
    É semelhante a 401 Unauthorized, mas a autenticação precisa ser feita por um proxy.

    [408] Request Timeout
    Esta resposta é enviada por alguns servidores em uma conexão ociosa, mesmo sem qualquer requisição prévia pelo cliente. Isso significa que o servidor gostaria de desligar esta conexão não utilizada. Essa resposta é muito mais usada, pois alguns navegadores, como Chrome, Firefox 27+ ou IE9, usam mecanismos de pré-conexão HTTP para acelerar a navegação. Observe também que alguns servidores simplesmente encerram a conexão sem enviar esta mensagem.

    [409] Conflict
    Esta resposta será enviada quando uma requisição conflitar com o estado atual do servidor.

    [410] Gone
    Esta resposta é enviada quando o conteúdo solicitado foi excluído permanentemente do servidor, sem endereço de encaminhamento. Espera-se que os clientes removam seus caches e links para o recurso. A especificação HTTP pretende que esse código de status seja usado para "serviços promocionais por tempo limitado". As APIs não devem se sentir compelidas a indicar recursos que foram excluídos com esse código de status.

    [411] Length Required
    O servidor rejeitou a solicitação porque o campo de cabeçalho Content-Length não está definido e o servidor o exige.

    [412] Precondition Failed
    O cliente indicou nos seus cabeçalhos pré-condições que o servidor não atende.

    [413] Payload Too Large
    A entidade requisição é maior do que os limites definidos pelo servidor. O servidor pode fechar a conexão ou retornar um campo de cabeçalho Retry-After.

    [414] URI Too Long
    O URI solicitado pelo cliente é mais longo do que o servidor está disposto a interpretar.

    [415] Unsupported Media Type
    O formato de mídia dos dados requisitados não é suportado pelo servidor, portanto, o servidor está rejeitando a requisição.

    [416] Range Not Satisfiable
    O intervalo especificado pelo campo de cabeçalho Range na solicitação não pode ser atendido. É possível que o intervalo esteja fora do tamanho dos dados do URI de destino.

    [417] Expectation Failed
    Este código de resposta significa que a expectativa indicada pelo campo de cabeçalho de solicitação Expect não pode ser atendida pelo servidor.

    [418] I'm a teapot
    O servidor recusa a tentativa de coar café num bule de chá.

    [421] Misdirected Request
    A requisição foi direcionada a um servidor inapto a produzir a resposta. Pode ser enviado por um servidor que não está configurado para produzir respostas para a combinação de esquema e autoridade inclusas na URI da requisição.

    [422] Unprocessable Content (WebDAV)
    A solicitação foi bem formada, mas não pôde ser atendida devido a erros semânticos.

    [423] Locked (WebDAV)
    O recurso que está sendo acessado está bloqueado.

    [424] Failed Dependency (WebDAV)
    A solicitação falhou devido à falha de uma solicitação anterior.

    [425] Too Early Experimental
    Indica que o servidor não está disposto a correr o risco de processar uma solicitação que pode ser repetida.

    [426] Upgrade Required
    O servidor se recusa a executar a solicitação usando o protocolo atual, mas pode estar disposto a fazê-lo depois que o cliente atualizar para um protocolo diferente. O servidor envia um cabeçalho Upgrade em uma resposta 426 para indicar os protocolos necessários.

    [428] Precondition Required
    O servidor de origem exige que a solicitação seja condicional. Esta resposta destina-se a prevenir o problema de 'atualização perdida', onde um cliente pega (GET) o estado de um recurso, o modifica e o coloca (PUT) de volta no servidor, quando entretanto um terceiro modificou o estado no servidor, levando a um conflito.

    [429] Too Many Requests
    O usuário enviou muitas requisições num dado tempo ("limitação de frequência").

    [431] Request Header Fields Too Large
    O servidor não está disposto a processar a solicitação porque seus campos de cabeçalho são muito grandes. A solicitação pode ser reenviada após reduzir o tamanho dos campos do cabeçalho da solicitação.

    [451] Unavailable For Legal Reasons
    O agente do usuário solicitou um recurso que não pode ser fornecido legalmente, como uma página da Web censurada por um governo.

##  Respostas de erro do servidor
    
#   • 500 - 599

    [500] Internal Server Error
    O servidor encontrou uma situação com a qual não sabe lidar.

    [501] Not Implemented
    O método da requisição não é suportado pelo servidor e não pode ser manipulado. Os únicos métodos que servidores devem suportar (e portanto não devem retornar este código) são GET e HEAD.

    [502] Bad Gateway
    Essa resposta de erro significa que o servidor, enquanto trabalhava como um gateway para obter uma resposta necessária para lidar com a solicitação, obteve uma resposta inválida.

    [503] Service Unavailable
    O servidor não está pronto para manipular a requisição Causas comuns são um servidor em manutenção ou sobrecarregado. Note que junto a esta resposta, uma página amigável explicando o problema deveria ser enviada. Esta resposta deve ser usada para condições temporárias e o cabeçalho HTTP Retry-After deverá, se possível, conter o tempo estimado para recuperação do serviço. O webmaster deve também tomar cuidado com os cabeçalhos relacionados com o cache que são enviados com esta resposta, já que estas respostas de condições temporárias normalmente não deveriam ser postas em cache.

    [504] Gateway Timeout
    Essa resposta de erro é fornecida quando o servidor está atuando como um gateway e não consegue obter uma resposta a tempo.

    [505] HTTP Version Not Supported
    A versão HTTP usada na requisição não é suportada pelo servidor.

    [506] Variant Also Negotiates
    O servidor tem um erro de configuração interna: o recurso variante escolhido está configurado para se envolver em negociação de conteúdo transparente e, portanto, não é um ponto final adequado no processo de negociação.

    [507] Insufficient Storage (WebDAV)
    O método não pôde ser executado no recurso porque o servidor não pode armazenar a representação necessária para concluir a solicitação com êxito.

    [508] Loop Detected (WebDAV)
    O servidor detectou um loop infinito ao processar a solicitação.

    [510] Not Extended
    Extensões adicionais à solicitação são necessárias para que o servidor a atenda.

    [511] Network Authentication Required
    Indica que o cliente precisa se autenticar para obter acesso à rede.