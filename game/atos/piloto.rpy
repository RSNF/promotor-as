define narrador = Character("")
define juiz = Character("Juiz")
define promotor_as = Character("Ryota")
define advogada = Character("Advogada")

label piloto:

    narrador "Este é apenas um piloto para uma visual novel."
    narrador "O nome do jogo, como também dos personagens e a história é discutivel e capaz de mundanças."

    play music "Starting Out Waltz Vivace.mp3"

    scene cadeiras:
        xalign 0.5
        yalign 1.0
        linear 15.0 yalign 0.0
    with dissolve

    narrador "Olá, e bem vindo(a) ao Promotor Ás!"

    narrador "Neste jogo você jogará como o \"Promotor Ás\"."

    narrador "Você enfretará vários julgamentos que colocarão seu conhecimento a prova,
    como foco principal serão julgamentos todos relacionados a crimes virtuais, e veremos como se sairá."

    scene tribunal:
        xalign 0.5
        linear 15.0 yalign 1.0
    with dissolve

    narrador "Este é o Tribunal de Justiça Central."

    narrador "Onde muitos casos já foram julgados, muitos culpados dos seus crimes, outros, muitos também, absolvidos."

    narrador "O tribunal é por muitos considerado o paragão da justiça em sí!"

    scene black
    with dissolve

    scene tribunal:
        xalign 0.5
        yalign 0.3
    with dissolve

    show juiz 404

    narrador "O juiz, ele é aquele que remediará as discussões, garantirá a administração dos processos legais, 
    e justo, também será ele que tomará a decisão final declarada ao bater do martelo, apresente o que puder para 
    trazer o juiz para o seu lado!"

    scene cadeiras:
        xalign 1.0
        yalign 0.5

    show ryota confiante at right
    with dissolve

    narrador "Este é Ryota Sakurai."

    narrador "Como também conhecido \"Promotor ás\", por sempre buscar ser eximio nas suas atividades jurídicas."

    narador "Como promotor você investigará os crimes e vai reunir evidências o suficiente para determinar se existe acusação criminal, 
    tendo evidências o suficiente você deve apresentar elas e justificar sua acusação."

    show ryota inseguro

    promotor_as "Mais um dia que começa, mas desafios pela frente."

    promotor_as "Hm, vejo que todos pela frente são de crimes virtuais..."

    show ryota confiante

    promotor_as "Justo o que eu sou o melhor!"

    promotor_as "Talvez hoje seja um ótimo dia!"

    hide ryota confiante
    with dissolve

    scene cadeiras:
        xalign 1.0
        yalign 0.5
        xzoom -1.0
    
    show advogada 404 at left
    with dissolve

    narrador "Já está é ***, advogada e em muitos casos a oposição do nosso Promotor Ás."

    narrador "Ela também estará atuando nos casos que você enfretará, e como de costume dela, será uma oposição de ferro, 
    é bom que você esteja afiado."

    narrador "A advogada vai dar a sua acessória ao seu cliente e vai representar eles durante o julgamento, 
    combatendo suas acusações e evidências."

    scene tribunal:
        xalign 0.5
        yalign 0.35
    with dissolve

    pause 15.0

    return