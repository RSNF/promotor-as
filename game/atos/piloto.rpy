define narrador = Character("")
define juiz = Character("Juiz")
define promotor_as = Character("Ryota")
define advogada = Character("Camila")

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
    
    show camila neutra 2 at left
    with dissolve

    narrador "Esta é Camila Oliveira, advogada e, em muitos casos, a oposição do nosso Promotor Ás."

    narrador "Ela também estará atuando nos casos que você enfrentará e, como de costume, será uma oposição de ferro. É bom que você esteja afiado."

    narrador "A advogada dará assistência ao seu cliente e o representará durante o julgamento, combatendo suas acusações e evidências."

    show camila neutra 5 at left

    advogada "Olá, eu sou Camila Oliveira."

    advogada "Assim como o Ryota, sou uma peça importante neste jogo."

    advogada "Enquanto ele busca a acusação, eu estarei aqui para defender os acusados."

    advogada "A justiça é uma balança, e cabe a nós equilibrá-la."

    advogada "Prepare-se, porque nossos caminhos se cruzarão muitas vezes."

    narrador "Pronto! todos os personagens importantes já foram apresentados e introduzidos! É isso tchau!!"

    scene black
    with dissolve

    stop music fadeout 1.0

    pause 3.0

    play sound "ping exclamation.mp3"

    play music "Run Amok.mp3"

    advogada "Espera um pouco aí!!"

    scene tribunal:
        xalign 0.5
        yalign 0.35
    with dissolve

    narrador "hm? o que foi que houv-{nw}"

    advogada "Como assim tchau? e por que a tela estava ficando escura e a música abaixando!? o jogo acabou?"

    narrador "Sim, acontece que o jogo nã-{nw}"

    advogada "O juiz sequer teve fala alguma! O jogo não pode acabar agora!"

    narrador "Calma, Calma aí!"

    narrador "..."

    narrador "Olha meus bens, o jogo não ta completo, então por ora, esse é o fim..."

    narrador "No momento atual é jogo é uma demo, feito para gerar discussões, também para demonstrar o potencial da engine ren'py 
    e de que esse jogo pode ser tornar algo maior!"

    advogada "..."

    stop music fadeout 1.0

    narrador "Então... por enquanto é isso, tchau!"

    hide advogada
    with dissolve

    scene tribunal:
        xalign 0.5
        yalign 0.35
    with dissolve

    pause 5.0

    return
