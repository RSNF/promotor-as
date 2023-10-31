define narrador = Character("")
define jogador = "Você"
define prof = Character("Prof. Celestina Morais")
define abraao = Character("Abraão")
define aluno1 = Character("Aluno 1")
define aluno2 = Character("Aluno 2")
define turma = Character("Turma")

label historia1:

    scene black with fade

    centered "{size=+16}Caso Abraão: Origem{/size}"

    scene cadeiras:
        xalign 0.5
        yalign 0.5

    play music "sala.mp3"

    # show celestina at left with moveinleft

    show professora sorridente at left with moveinleft:
        zoom 1.6
        yalign 1.2

    narrador "Numa tranquila aula de legislação, a {b}Prof. Celestina Morais{/b} pediu aos alunos que
    tomassem notas sobre o conteúdo apresentado para que fosse criado um relatório." with dissolve

    show jovem sorridente at right with moveinright:
        zoom 1.4
        yalign 1.2

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

    play music "Run Amok.mp3"

    narrador "**Com essa fala de {b}Abraão{/b}, desencadeou uma série de discussões entre os alunos**" with dissolve

    show jovem sorridente at center with moveinright

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

    show professora sorridente

    prof "Ok pessoal, acalmem-se, vamos resolver isso." with dissolve

    play music "sala.mp3"

    show jovem sorridente at right with fade

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

    show professora sorridente

    prof "Pois deveriam estar por dentro das normas para não cometer erros como esses.
    Agindo desse modo, que direito Abraão está ferindo?" with dissolve

    menu:
        "O que você acha?"

        "Invasão de privacidade":
            $ direito_ferido = "Invasão de privacidade"

        "Direitos de \"imagem\"":
            $ direito_ferido = "Direitos de \"imagem\""

    show professora sorridente

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

    hide celestina with moveoutleft

    hide abraao with moveoutright

    scene black with fade

    pause 5.0

    return
