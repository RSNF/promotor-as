define narrador = Character("")
define juiz = Character("Juiz")
define promotor_as = Character("Ryota")
define advogada = Character("Advogada")

label piloto:

    narrador "Este é apenas um piloto para uma visual novel."
    narrador "O nome do jogo, assim como dos personagens e a história, é discutível e sujeito a mudanças."

    play music "Starting Out Waltz Vivace.mp3"

    scene cadeiras:
        xalign 0.5
        yalign 1.0
        linear 15.0 yalign 0.0
    with dissolve

    narrador "Olá e bem-vindo(a) ao Promotor Ás!"

    narrador "Neste jogo, você jogará como o \"Promotor Ás\"."

    narrador "Você enfrentará vários julgamentos que colocarão seu conhecimento à prova, com foco principal em julgamentos relacionados a crimes virtuais. Veremos como você se sairá."

    scene tribunal:
        xalign 0.5
        linear 15.0 yalign 1.0
    with dissolve

    narrador "Este é o Tribunal de Justiça Central."

    narrador "Onde muitos casos já foram julgados, muitos culpados dos seus crimes, outros, absolvidos."

    narrador "O tribunal é considerado por muitos como o paradigma da justiça em si!"

    scene black
    with dissolve

    scene tribunal:
        xalign 0.5
        yalign 0.3
    with dissolve

    show juiz 404

    narrador "O juiz é aquele que media as discussões, garante a administração dos processos legais e, por fim, toma a decisão final declarada ao bater do martelo. Apresente o que puder para conquistar o juiz para o seu lado!"

    scene cadeiras:
        xalign 1.0
        yalign 0.5

    show ryota confiante at right
    with dissolve

    narrador "Este é Ryota Sakurai."

    narrador "Também conhecido como \"Promotor Ás\", por sempre buscar ser exímio em suas atividades jurídicas."

    narrador "Como promotor, você investigará os crimes e reunirá evidências suficientes para determinar se existe acusação criminal. Tendo evidências suficientes, você deve apresentá-las e justificar sua acusação."

    show ryota inseguro

    promotor_as "Mais um dia que começa, mais desafios pela frente."

    promotor_as "Hm, vejo que todos os casos de hoje são de crimes virtuais..."

    show ryota confiante

    promotor_as "Justamente no que eu sou o melhor!"

    promotor_as "Talvez hoje seja um ótimo dia!"

    hide ryota confiante
    with dissolve

    scene cadeiras:
        xalign 1.0
        yalign 0.5
        xzoom -1.0
    
    show advogada 404 at left
    with dissolve

    narrador "Esta é ***, advogada e, em muitos casos, a oposição do nosso Promotor Ás."

    narrador "Ela também estará atuando nos casos que você enfrentará e, como de costume, será uma oposição de ferro. É bom que você esteja afiado."

    narrador "A advogada dará assistência ao seu cliente e o representará durante o julgamento, combatendo suas acusações e evidências."

    scene tribunal:
        xalign 0.5
        yalign 0.35
    with dissolve

    pause 15.0

    return
