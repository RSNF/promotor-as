define narrador = Character("")
define jogador = "Você"
define prof = Character("Prof. Celestina Morais")
define abraao = Character("Abraão")
define aluno1 = Character("Aluno 1")
define aluno2 = Character("Aluno 2")
define turma = Character("Turma")

define joao = Character("João")
define paulo = Character("Paulo")
define vanessa = Character("Vanessa")

image profImg = "/images/professora.png"

image abraaoImg = "/images/jovem.png"

image joaoImg = "/images/joao.png"
image pauloImg = "/images/paulo.png"
image vanessaImg = "/images/vanessa.png"


label historia1:

    scene black with fade

    centered "{size=+16}História 1{/size}"

    
    scene quarto:
        zoom 2.0
        xalign 0.5
        yalign 0.5

    narrador "João Macedo é um jovem de 26 anos, e trabalha como vendedor de carros, na empresa Disgol Veículos. 
    Natural de Ilhéus- Ba, ele trabalha há 5 anos no mesmo lugar" with dissolve

   
    narrador "Recentemente ele começou a passar por alguns problemas financeiros, 
    decorrentes de uma inundação que lhe fez perder vários móveis da sua casa e lhe forçou a recomprar vários deles pelo seu 
    cartão de crédito." with dissolve

    narrador "**Certo dia, durante seu horário de almoço em um restaurante próximo ao trabalho, João recebe uma mensagem em um grupo de conhecidos no WhatsApp**" with dissolve
    play sound "toqueSap.mp3"
    show celular:
        xalign 0.5
        yalign 0.5

    narrador "WhatsApp: O governo está oferecendo um saque especial do Fundo de Garantia por Tempo de Serviço (FGTS) para trabalhadores com mais de 2 anos de carteira assinada. Acesse o link para verificar se o seu FGTS já está disponível: https://www.ba.gov.br/servico/3620-1." with dissolve

    narrador "João clica no link e é redirecionado para um site que se assemelha muito a uma página oficial do governo. Sem suspeitar de nada, ele preenche o formulário com seus dados pessoais, ansioso para descobrir se terá direito ao saque do FGTS..." with dissolve

    narrador "No entanto, a mensagem na tela informa que ele não tem direito ao saque especial. João fecha o site e resolve deixar o assunto para lá. " with dissolve
    hide celular
    narrador "**Algumas semanas depois**" with dissolve

    narrador "João resolve fazer a compra de um sofá novo para sua casa, 
    parcelado em doze vezes no cartão de crédito. Contudo, 
    ele recebe uma mensagem por e-mail informando que o pagamento não foi aprovado" with dissolve

    narrador "Com isso, João acessa o app do banco e descobre que está sem limite para compras e resolve analisar suas faturas. 
    A partir disso, João percebe que foram feitas várias compras online pelo seu cartão de crédito." with dissolve

    narrador "Alarmado, ele liga para seu banco imediatamente..." with dissolve

    
        
        
    show pauloImg at right with moveinright:
        zoom 1.4
        yalign -0.1
   
    paulo "Boa tarde! Em que posso lhe ajudar?" with dissolve
   
    show joaoImg at left with moveinleft:
        zoom 1.4
        yalign -0.1

    joao "Boa tarde, percebi que foram feitas várias compras no meu cartão de crédito que eu não reconheço. Eu gostaria de pedir o reembolso delas." with dissolve

    
    paulo "Aqui é Paulo. Poderia me informar a agência da sua conta com o dígito verificador e o número da sua conta." with dissolve

    joao "Agencia: 1234-5  e Conta: 08456-9." with dissolve

    paulo "Paulo: Em que período ocorreu às compras?" with dissolve

    joao "Entre os dias 15 e 17 de março de 2023" with dissolve

    paulo "Certo João, foi gerado um número de protocolo, poderia estar anotando, por favor?" with dissolve

    joao "Pode falar." with dissolve

    paulo "9517538422680. Sua ocorrência foi efetuada, faremos o possível para ajudá-lo. Vamos analisar suas faturas e lhe retornaremos assim que possível." with dissolve
    
    scene black with fade

    centered "*Tempos depois*
    João recebe um retorno do banco, porém com uma desanimadora resposta. “Depois de analisar as faturas de João, o banco conclui que não será possível estornar as compras não autorizadas. Pois as compras feitas em seu cartão foram efetuadas em sites que já costumava utilizar. Não possui evidências suficientes de que o cartão foi clonado.”
    Sem saber o que fazer, João pede ajuda a uma amiga, Vanessa. Uma advogada recém formada, que trabalha em um pequeno escritório de advocacia na cidade.
    " with dissolve

    scene quarto:
        zoom 2.0
        xalign 0.5
        yalign 0.5

    show joaoImg at left with moveinleft:
        zoom 1.4
        yalign -0.1

    joao "Vanessa, eu não sei o que fazer. As coisas já estavam difíceis antes e agora eu descubro que foram feitas várias compras no meu cartão de crédito que eu simplesmente não fiz e meu banco não quer fazer o cancelamento." with dissolve

    show vanessaImg at right with moveinright:
        zoom 1.4
        yalign -0.1


    vanessa "O banco tem obrigação de estornar o dinheiro, se for comprovado que não foram feitas pelo cliente." with dissolve

    vanessa "Mas você já fez um boletim de ocorrência?" with dissolve

    menu:
        "O que você acha?"

        "Não":
            vanessa "Então, após fazer isso, vamos tentar contato com as lojas em que foram feitas as compras para ver se ainda é possível solicitar o estorno e cancelar a compra." with dissolve

        "Sim":
            vanessa "Então, agora vamos tentar contato com as lojas em que foram feitas as compras para ver se ainda é possível solicitar o estorno e cancelar a compra." with dissolve

    joao "Certo!" with dissolve

    narrador "Após fazer o boletim de ocorrência e verificar com as lojas se era possível cancelar as compras, algumas lojas informaram que o prazo para solicitar o cancelamento já havia encerrado, e tiveram outras  em que não foi possível entrar em contato." with dissolve

    vanessa "A partir disso, nós podemos entrar em contato com o Banco Central e fazer uma denuncia contra a Natur, gerenciadora do seu cartão de crédito, por eles não terem cancelado suas compras, mesmo após você dizer que não reconhece elas. Isso porque elas foram feitas em valores anormais, entre meia noite e três da manhã e com um pequeno intervalo de tempo entre elas. Por si só isso já seria suficiente para seu banco ao menos bloquear as compras realizadas nesse horário." with dissolve

    menu:
        "Isso porque:"

        "A norma jurídica brasileira já estabeleceu jurisprudência de que os bancos têm a responsabilidade de bloquear compras suspeitas de seus clientes. E caso isso não seja feito, eles têm a obrigação de estornarem o valor das compras.":
            vanessa "Correto" with dissolve

        "É um direito público e de ampla jurisprudência de que bancos devem cancelar compras anormais de seus clientes e contatarem eles via ligação telefônica":
            vanessa "Incorreto" with dissolve

        "É um direito objetivo seu entrar em contato com o banco e provar que as compras não foram feitas por você, com isso eles têm a obrigação de estornar os valores.":
            vanessa "Incorreto" with dissolve

    vanessa "Também seria importante descobrir quem foi a pessoa que fez essas compras com seu cartão. Quem lhe passou o link?" with dissolve

    joao "O meu colega, Henrique. Ele encaminhou o link pelo WhatsApp." with dissolve

    vanessa "Acho que infelizmente nesse caso não vai ter muito o que você possa fazer. O fato de seu colega Henrique ter repassado o link suspeito e ter adquirido produtos caros recentemente, levanta suspeitas de seu possível envolvimento nesse golpe. Vamos prosseguir da seguinte maneira: Primeiramente, você deve:" with dissolve
    
    menu:
        "Isso porque?"

        "Registrar uma queixa policial relatando o golpe virtual e mencionando que Henrique enviou o link suspeito.":
            vanessa "Correto" with dissolve

        "Cancelar seu cartão e não fazer qualquer contato com seu banco ou às autoridades":
            vanessa "Incorreto" with dissolve

    scene black with fade

    narrador "João decide realizar uma queixa na delegacia, denunciando que foi vítima de phishing." with dissolve

    narrador "Com o boletim de ocorrência em mãos, João faz uma denúncia ao Bacen contra a gerenciadora do seu cartão de crédito.  O gerente do seu banco lhe liga:" with dissolve

    narrador "*A ideia aqui é iniciar uma discussão entre João e o gerente de banco*" with dissolve

    scene quarto:
        zoom 2.0
        xalign 0.5
        yalign 0.5

    show pauloImg at right with moveinright:
        zoom 1.4
        yalign -0.1

    paulo "Boa tarde, João. Recebemos uma notificação do Bacen a respeito de não termos estornado suas compras. Como já havíamos conversado, isso não será possível uma vez que não há nada que comprove que não foram realizadas por você. " with dissolve

    show joaoImg at left with moveinleft:
        zoom 1.4
        yalign -0.1
    joao "Em apenas um dia eu tive um prejuízo de mais de 4 mil reais e corro o risco de ver meu nome negativado pelo Serasa. Conforme vocês puderam ver pelo boletim de ocorrência que fiz, eu fui vítima de um crime virtual chamado phishing, para o roubo de meus dados bancários." with dissolve

    

    menu:
        "Pergunta:"

        "A prática de phishing existe na lei de crimes cibernéticos, porém o roubo de dados pessoais não é crime no Brasil.":
            narrador "Incorreto" with dissolve

        "Cancelar seu cartão e não fazer qualquer contato com seu banco ou às autoridades":
            narrador "Correto" with dissolve

    scene black with fade

    narrador "O gerente do banco resiste à ideia de indenizar João." with dissolve

    show pauloImg at right with moveinright:
        zoom 1.4
        yalign -0.1

    paulo "Entendemos o transtorno pela sua situação, João. Mas não podemos fazer nada, uma vez que as compras foram feitas com seus dados." with dissolve
    
    narrador "*Com a recusa do Banco em realizar o estorno das compras. João é aconselhado pela sua amiga Vanessa a fazer uma nova denúncia ao Banco Central." with dissolve

    scene quarto:
        zoom 2.0
        xalign 0.5
        yalign 0.5 

    show vanessaImg at right with moveinright:
        zoom 1.4
        yalign -0.1

    vanessa "A lei  Lei nº 4.595, de 31 de dezembro de 1964, conhecida como a Lei do Sistema Financeiro Nacional estabelece que o BC tem o poder de penalizar os bancos caso eles agem de forma a lesar seus clientes." with dissolve

    narrador "Um processo entre o Banco Natur e o João é considerado uma ação de direito público ou privado?" with dissolve

    menu:
        "O que você acha?"

        "Público, por se tratar de uma relação jurídica entre um grande banco privado e uma pessoa física":
            narrador "Incorreto" with dissolve

        "Privado, pelo fato de ser uma relação contratual entre partes não estatais, envolvendo os interesses privados do cliente e do banco. ":
            narrador "Correto" with dissolve

    scene cidade
        

    centered "*Seguindo o conselho de sua amiga, João realiza uma nova e detalhada denúncia contra a Natur ao Bacen, 
    detalhando horários das compras, o boletim de ocorrência e os protocolos de atendimento com seu banco. 
    Recebendo a cópia de um e-mail endereçado ao seu banco."

##################################
########### Parte 2 ###############
##################################

label historia2:

    scene black with fade

    centered "{size=+16}Caso Abraão: Origem{/size}"

    scene cadeiras:
        xalign 0.5
        yalign 0.5



    # show celestina at left with moveinleft

    show profImg at left with moveinleft:
        zoom 1.2
        yalign -0.5
    

    narrador "Numa tranquila aula de legislação, a {b}Prof. Celestina Morais{/b} pediu aos alunos que
    tomassem notas sobre o conteúdo apresentado para que fosse criado um relatório." with dissolve

    show jovem at right with moveinright:
        zoom 1.2
        yalign -0.5

    narrador "{b}Abraão{/b}, sempre buscava praticidade, com auxílio da tecnologia,
    e decidiu gravar um áudio da aula para ouvir mais tarde e elaborar seu relatório." with dissolve

    narrador "Contudo, essa escolha foi feita sem o consentimento de seus colegas." with dissolve

    # w=5.0, esperar 5 segundos para prosseguir
    narrador "**No último horário da aula**{w=5.0}" with fade

    prof "Agora quero que vocês apresentem o relatório que foi criado ao longo da aula
    apresentando o ponto de vista de vocês em relação a nossa discussão." with dissolve

    prof "Vi que todos anotaram sobre a aula, menos você {b}Abraão.{/b}" with dissolve

    abraao "Professora, o relatório era para ser apresentado agora? Não é para a próxima aula?" with dissolve

    prof "Não, estou pedindo o relatório agora para identificar os
    pontos de vista que cada aluno adquiriu ao longo da aula." with dissolve

    prof "Como você vai falar sobre as discussões sem ter anotado o que considerou mais importante?" with dissolve

    abraao "Eu havia gravado a aula para escutar depois e fazer o relatório para a próxima aula." with dissolve

    play sound "ping exclamation.mp3"

    narrador "**Com essa fala de {b}Abraão{/b}, desencadeou uma série de discussões entre os alunos**" with dissolve

    show jovem at right with moveinright:
        zoom 1.2
        yalign -0.5

    narrador "{b}Abraão{/b} se assusta com a reação de seus colegas." with dissolve

    play sound "slap.mp3"

    aluno1 "Você pediu autorização para gravar a aula? Sabe que isso é violação de privacidade?{fast}" with dissolve

    abraao "Mas...{nw}"

    play sound "slap.mp3"

    aluno2 "Não permiti que eu fosse gravada. A senhora deixou, prof?{fast}" with dissolve

    menu:
        "O que você acha?"

        "Não ligo muito.":
            jogador "Não vejo problema dele estar gravando." with dissolve

        "Não gostei.":
            jogador "Não quero que minha gravação seja exposta. Exclua agora!" with dissolve

    narrador "Os murmúrios e desconforto entre os alunos logo se transformaram em uma discussão fervorosa na sala de aula." with dissolve

    narrador "A questão central: Seria a ação de {b}Abraão{/b} considerada um crime?
    Alguns colegas sentiram que sua privacidade fora invadida." with dissolve

    show profImg at left with moveinleft:
        zoom 1.2
        yalign -0.5

    prof "Ok pessoal, acalmem-se, vamos resolver isso." with dissolve

    show jovem at right with moveinright:
        zoom 1.2
        yalign -0.5

    turma "..." with dissolve

    prof "Então vamos lá, começando por {b}Abraão{/b}, porque você decidiu gravar a aula sendo que pedi que todos fizessem anotações?" with dissolve

    abraao "Por questões de praticidade eu decidi gravar a aula para depois, com calma,
    fazer o relatório do que foi dito e revisar os assuntos da aula." with dissolve

    prof "É permitido gravar sem autorização das pessoas?" with dissolve

    menu:
        "O que você acha?"

        "Sim, é permitido.":
            $ prof_resposta = "Não"

            jogador "É permitido gravar sem autorização!" with dissolve

        "Não é permitido.":
            $ prof_resposta = "Exatamente"

            jogador "Com certeza não é permitido!" with dissolve

    prof "[prof_resposta], é errado e pode gerar sanções legais a depender da finalidade para o qual a mídia seja utilizada." with dissolve

    prof "As universidades possuem regras que podem gerar uma ação disciplinar.
    Você leram o código disciplinar do aluno? Está tudo escrito lá." with dissolve

    turma "Não." with dissolve

    show profImg at left with moveinleft:
        zoom 1.2
        yalign -0.5

    prof "Pois deveriam estar por dentro das normas para não cometer erros como esses.
    Agindo desse modo, que direito Abraão está ferindo?" with dissolve

    menu:
        "O que você acha?"

        "Invasão de privacidade":
            $ direito_ferido = "Invasão de privacidade"

        "Direitos de \"imagem\"":
            $ direito_ferido = "Direitos de \"imagem\""

    show profImg at left with moveinleft:
        zoom 1.2
        yalign -0.5

    prof "Exatamente. Ele está ferindo o direito de [direito_ferido] Que pode ser visto no Código Penal." with dissolve

    prof "Muito bem, agora que esclarecemos a questão da gravação, vamos explorar a questão do compartilhamento de mídia sem consentimento." with dissolve

    prof "{b}Abraão{/b}, você já compartilhou essa gravação com alguém?" with dissolve

    abraao "Não, professora, eu só pretendia usá-la para meu próprio estudo." with dissolve

    prof "Ótimo. Agora, vamos discutir as implicações do compartilhamento não autorizado de mídia." with dissolve

    prof "Qual é a diferença entre gravar uma aula para uso pessoal e compartilhá-la com outras pessoas sem permissão?" with dissolve

    menu:
        "O que você acha?"

        "Se for para uso pessoal não tem problema.":
            jogador "Gravar para uso pessoal é legítimo, compartilhar sem permissão viola a privacidade." with dissolve

            $ prof_resposta = "Correto"

        "Nenhuma?":
            jogador "Não há diferença, ambas são ações ilegais." with dissolve

            $ prof_resposta = "Incorreto"

    prof "[prof_resposta]. Gravar para uso pessoal é uma ação que geralmente é aceitável{w=0.5},
    mas compartilhar sem permissão viola a privacidade das pessoas e pode ser ilegal em muitos casos." with dissolve

    aluno1 "Mas, se eu precisasse de uma gravação para comprovar um crime ou coisa do tipo,
    as pessoas não poderiam saber, como eu faria isso?" with dissolve

    prof "O que vocês acham turma?" with dissolve

    menu:
        "O que você acha?"

        "Pode.":
            jogador "Pode, já que é para comprovar alguma forma de corrupção." with dissolve

        "Não pode.":
            jogador "Não, pois um crime não pode justificar outro." with dissolve

    prof "As duas estão corretas. Em algumas situações, a lei permite o uso de evidências, como gravações,
    para comprovar crimes ou ações ilegais, como a corrupção. No entanto, existem diretrizes específicas para isso." with dissolve

    prof "Pois, embora em certos casos a lei permita o uso de evidências para comprovar crimes,
    isso não justifica cometer um crime para provar outro." with dissolve

    prof "A ética e o respeito às leis devem ser mantidos, e existem procedimentos legais a serem seguidos
    para garantir que a evidência seja admissível em um tribunal." with dissolve

    prof "Portanto, cometer um crime para provar outro é geralmente inaceitável." with dissolve

    prof "Quais são os princípios éticos envolvidos no compartilhamento de mídia?
    Você acha que é importante considerar esses princípios ao tomar decisões sobre compartilhar informações?" with dissolve

    menu:
        "O que você acha?"

        "São importantes!":
            jogador "Privacidade, consentimento e respeito, e sim esses princípios são importantes." with dissolve

            $ prof_resposta = "Correto"

        "São nada!":
            jogador "Não tem nenhum, os princípios éticos não são importantes." with dissolve

            $ prof_resposta = "Incorreto"

    prof "[prof_resposta]. Princípios éticos como privacidade,
    consentimento e respeito são fundamentais ao tomar decisões sobre compartilhar informações." with dissolve

    prof "É importante considerar esses princípios para garantir relacionamentos saudáveis e respeitosos,
    ignorar esses princípios pode resultar em violações de privacidade e questões legais." with dissolve

    prof "É crucial considerar a ética em nossas ações." with dissolve

    play sound "sino.mp3"

    narrador "**Fim da aula**{w=5.0}" with dissolve

    prof "...{w=1.0} mais alguma dúvida?" with dissolve

    turma "Não." with dissolve

    prof "Exatamente, de acordo com lei/artigo/código(inserir) é errado o que ele fez.
    {b}Abraão{/b} cometeu um erro ao gravar a aula sem o consentimento dos colegas e da professora." with dissolve

    prof "Isso levanta questões sobre privacidade e a legalidade de sua ação.
    Ele não teve intenções maliciosas ao gravar a aula,
    mas isso não o isenta da responsabilidade de seguir as regras e leis relacionadas à privacidade e à gravação de áudio." with dissolve

    prof "Vamos usar isso como conscientização sobre a importância do respeito à privacidade e a necessidade de seguir as regras.
    Isso pode servir como uma lição valiosa sobre ética, leis e respeito mútuo na era digital." with dissolve

    hide profImg with moveoutleft

    hide abraaoImg with moveoutright

    scene black with fade

    pause 5.0

    return
