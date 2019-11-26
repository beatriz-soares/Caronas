# Meu Carona

Sistema desenvolvido para a disciplina Projeto e Desenvolvimento de Software do DCA na UFRN.

## O Sistema

O Sistema serve para cadastrar e procurar caronas ao longo de uma rota ou de pontos numa determinada região.
O usuário pode realizar cadastro tanto como passageiro (desejando solicitar carona) quanto motorista (desejando oferecer carona).

## Implementação e Ferramenta

O Sistema foi desenvolvido utilizando o framework Django feito em Python, voltado para aplicaçoes Web. 
Utiliza como SGBD o SQLite3 e o Mapeamento objeto-relacional do Django. Além de utilizar sessões, forms e outros utilitários do framework.

## Funcionamento e Fluxo

Inicialmente o usuário irá fazer um cadastro no sistema, podendo optar por ser Motorista, Passageiro ou ambos. Apos preencher o
formulario ja possui sua conta para fazer login no sistema.

Ao realizar login no sistema, caso o usuário tenha optado por ter ambos os perfis, tanto de motorista quanto de passageiro, terá qe optar
por qual deseja prosseguir na sessão. Caso seja motorista, poderá ofertar uma carona indicando os pontos e a sua rota ao longo do trajeto.
Caso seja passageiro, pode solicitar uma carona também ao longo do trajeto ou da rota.
