CASOS DE USO PARA SISTEMA FERROVIÁRIO POTIGUAR

ATOR 1: Cliente

Abrir conta
Fluxo normal:
1 - Cliente informa nome
2 - Cliente informa CPF 
3 - Cliente informa data de nascimento
4 - Cliente informa e-mail 
5 - Sistema abre a conta para o cliente

Extensões:
2a - Se o CPF for inválido, solicitar novo CPF
3a - Se for menor de 16 anos, solicitar nova data de nascimento e informar que a data é inválida
4a - Se o e-mail não for válido, solicitar novo e-mail

Autenticar Usuário
Fluxo normal:
1 - Usuário fornece login e senha

Extensões:
1a - Se login e senha não forem válidos, o Sistema deve informar o erro ao usuário e solicitar as informações novamente

Adicionar saldo
Pré-condição: estar autenticado
Fluxo normal:
1 - Cliente define entre um dos valores pré-definidos de saldo
2 - Cliente define a forma de pagamento (pix, crédito ou débito)
3 - Sistema efetua o pagamento 
4 - Cliente recebe o comprovante de pagamento em PDF
5 - Sistema pergunta se o cliente deseja realizar uma nova recarga

Extensões:
2a - Se opção for PIX, Sistema apresenta QR Code 
2b - Se opção for Cartão de Crédito, o Sistema solicita a inserção dos dados do cartão no aplicativo. Em caso de compra negada, o Sistema deve mostrar ao usuário o motivo.
2c - Se opção for Cartão de Débito, o Sistema solicita a inserção dos dados do cartão no aplicativo. Em caso de compra negada, o Sistema deve mostrar ao usuário o motivo.

Comprar bilhete
Pré-condição: estar autenticado
Fluxo normal:
1 - Cliente acessa no sistema o itinerário, as cadeiras disponíveis e o preço da passagem
2 - Cliente define o itinerário e seleciona cadeiras disponíveis
3 - Sistema verifica se o saldo na conta é suficiente
4 - Sistema reduz o saldo do cliente e realiza a compra 
5 - Cliente recebe o bilhete em PDF

Extensões:
2a - Se no momento que o cliente selecionou o lugar, o mesmo foi adquirido, solicitar que ele escolha outro lugar
3a - Caso o saldo na conta seja insuficiente para a compra do bilhete, o Sistema deve solicitar uma nova recarga
4a - Cliente tem a opção de baixar o bilhete

Gerenciar conta
Pré-condição: estar autenticado
Fluxo normal:
1 - O cliente acessa no sistema a aba do perfil 
2 - O cliente tem a opção de editar as informações pessoais
3 - O cliente tem a opção de excluir sua conta
 
Extensões: 
3a - Se houver saldo na conta, o cliente é avisado pelo Sistema que perderá o saldo se excluir a conta

ATOR 2: Comissário

Autenticar Usuário
Fluxo normal:
1 - Usuário fornece login e senha

Extensões:
1a - Se login e senha não forem válidos, o Sistema deve informar o erro ao usuário e solicitar as informações novamente

Fazer a validação do bilhete do passageiro
Pré-condição: estar autenticado
Fluxo normal:
1 - Passageiro apresenta o bilhete ao comissário
2 - Comissário verifica se é um bilhete válido 

Extensões: 
2a - Caso o bilhete não seja válido, o Sistema emite uma notificação para o comissário

ATOR 3: Gerente

Gerenciar comissários
Fluxo normal:
1 - O gerente concede permissão de comissário a usuário
2 - O gerente remove permissão de comissário a usuário

Gerenciar itinerário
Fluxo normal:
1 - O gerente lista os horários dos itinerários
2 - O gerente define o horário de partida

Gerenciar bilhetes
Fluxo normal:
1 - Gerente edita o valor do bilhete único
2 - Sistema salva novo valor para o bilhete único



