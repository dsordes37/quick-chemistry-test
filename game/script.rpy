

#___________________________________________________________________________________________________
 
label start:
    play music "cook.mp3"
    $som=True
    $ingles=False
    $total=0
    screen p_menu:
        imagemap:
            ground"menu.png"
            hover"menu click.png"
            hotspot(29, 303, 342, 89) clicked Jump("inicio")
            hotspot(29, 391, 342, 89) clicked Jump("configuracoes")
            hotspot(29, 480, 342, 89) clicked Jump("creditos")


    screen config:
        imagemap:
            ground"config.png"
            hover"config click.png"
            hotspot(80, 336, 296, 79) clicked Jump("configuracoes")
            hotspot(70, 427, 296, 79) clicked Jump("lingua")
            hotspot(474, 340, 296, 79) clicked Jump("som_ativo")
            hotspot(472, 426, 296, 79) clicked Jump("som_desativo")
            hotspot(274, 514, 296, 79) clicked Jump("startmenu")

#GAME 1==================================================================================================================
    screen game1_1:
        imagemap:
            ground"game1_p1a"
            hover"game1_p1a_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p1")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p1")#B
            hotspot(354, 282, 574, 84) clicked Jump("certo1_p1")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p1")#D
    screen game1_1b:
        imagemap:
            ground"game1_p1b"
            hover"game1_p1b_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p1")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p1")#B
            hotspot(354, 282, 574, 84) clicked Jump("certo1_p1")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p1")#D
    screen game1_1c:
        imagemap:
            ground"game1_p1c"
            hover"game1_p1c_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p1")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p1")#B
            hotspot(354, 282, 574, 84) clicked Jump("certo1_p1")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p1")#D

    screen game1_2:
        imagemap:
            ground"game1_p2a"
            hover"game1_p2a_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p2")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p2")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p2")#C
            hotspot(354, 375, 574, 84) clicked Jump("certo1_p2")#D
    
    screen game1_2b:
        imagemap:
            ground"game1_p2b"
            hover"game1_p2b_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p2")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p2")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p2")#C
            hotspot(354, 375, 574, 84) clicked Jump("certo1_p2")#D

    screen game1_2c:
        imagemap:
            ground"game1_p2c"
            hover"game1_p2c_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p2")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p2")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p2")#C
            hotspot(354, 375, 574, 84) clicked Jump("certo1_p2")#D

    screen game1_3:
        imagemap:
            ground"game1_p3a"
            hover"game1_p3a_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p3")#A
            hotspot(354, 190, 574, 84) clicked Jump("certo1_p3")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p3")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p3")#D
    
    screen game1_3b:
        imagemap:
            ground"game1_p3b"
            hover"game1_p3b_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p3")#A
            hotspot(354, 190, 574, 84) clicked Jump("certo1_p3")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p3")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p3")#D
    
    screen game1_3c:
        imagemap:
            ground"game1_p3c"
            hover"game1_p3c_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p3")#A
            hotspot(354, 190, 574, 84) clicked Jump("certo1_p3")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p3")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p3")#D



#GAME 2==============================================================================================================================
    screen game2_1:
        imagemap:
            ground"game2_p1a"
            hover"game2_p1a_clic"
            hotspot(379, 184, 306, 31) clicked Jump("certo2_p1")#A
            hotspot(379, 210, 306, 31) clicked Jump("errado2_p1")#B
            hotspot(379, 236, 306, 31) clicked Jump("errado2_p1")#C
            hotspot(379, 263, 306, 31) clicked Jump("errado2_p1")#D

    screen game2_1b:
        imagemap:
            ground"game2_p1b"
            hover"game2_p1b_clic"
            hotspot(379, 184, 306, 31) clicked Jump("certo2_p1")#A
            hotspot(379, 210, 306, 31) clicked Jump("errado2_p1")#B
            hotspot(379, 236, 306, 31) clicked Jump("errado2_p1")#C
            hotspot(379, 263, 306, 31) clicked Jump("errado2_p1")#D

    screen game2_2:
        imagemap:
            ground"game2_p2a"
            hover"game2_p2a_clic"
            hotspot(375, 141, 555, 93) clicked Jump("errado2_p2")
            hotspot(375, 226, 555, 93) clicked Jump("errado2_p2")
            hotspot(375, 322, 555, 93) clicked Jump("errado2_p2")
            hotspot(375, 423, 555, 93) clicked Jump("certo2_p2")

    screen game2_2b:
        imagemap:
            ground"game2_p2b"
            hover"game2_p2b_clic"
            hotspot(375, 141, 555, 93) clicked Jump("errado2_p2")
            hotspot(375, 226, 555, 93) clicked Jump("errado2_p2")
            hotspot(375, 322, 555, 93) clicked Jump("errado2_p2")
            hotspot(375, 423, 555, 93) clicked Jump("certo2_p2")

#GAME 3========================================================================================
    screen game3_1:
        imagemap:
            ground"game3_p1a"
            hover"game3_p1a_clic"
            hotspot(367, 141, 556, 57) clicked Jump("errado3_p1")
            hotspot(367, 204, 556, 57) clicked Jump("errado3_p1")
            hotspot(367, 274, 556, 57) clicked Jump("certo3_p1")
            hotspot(367, 336, 556, 57) clicked Jump("errado3_p1")
    screen game3_1b:
        imagemap:
            ground"game3_p1b"
            hover"game3_p1b_clic"
            hotspot(367, 141, 556, 57) clicked Jump("errado3_p1")
            hotspot(367, 204, 556, 57) clicked Jump("errado3_p1")
            hotspot(367, 274, 556, 57) clicked Jump("certo3_p1")
            hotspot(367, 336, 556, 57) clicked Jump("errado3_p1")
    screen game3_2:
        imagemap:
            ground"game3_p2a"
            hover"game3_p2a_clic"
            hotspot(372, 195, 185, 29) clicked Jump("errado3_p2")
            hotspot(372, 242, 185, 29) clicked Jump("certo3_p2")
            hotspot(372, 286, 185, 29) clicked Jump("errado3_p2")
            hotspot(372, 327, 185, 29) clicked Jump("errado3_p2")         
    screen game3_2b:
        imagemap:
            ground"game3_p2b"
            hover"game3_p2b_clic"
            hotspot(372, 195, 185, 29) clicked Jump("errado3_p2")
            hotspot(372, 242, 185, 29) clicked Jump("certo3_p2")
            hotspot(372, 286, 185, 29) clicked Jump("errado3_p2")
            hotspot(372, 327, 185, 29) clicked Jump("errado3_p2")

#GAME 4========================================================================================================

    screen game4_1:
        imagemap:
            ground"game4_p1a"
            hover"game4_p1a_clic"
            hotspot(376, 145, 512, 53) clicked Jump("errado4_p1")
            hotspot(376, 210, 512, 53) clicked Jump("errado4_p1")
            hotspot(376, 276, 512, 53) clicked Jump("certo4_p1")
            hotspot(376, 329, 512, 53) clicked Jump("errado4_p1")

    screen game4_1b:
        imagemap:
            ground"game4_p1b"
            hover"game4_p1b_clic"
            hotspot(376, 145, 512, 53) clicked Jump("errado4_p1")
            hotspot(376, 210, 512, 53) clicked Jump("errado4_p1")
            hotspot(376, 276, 512, 53) clicked Jump("certo4_p1")
            hotspot(376, 329, 512, 53) clicked Jump("errado4_p1")
    
    screen game4_2:
        imagemap:
            ground"game4_p2a"
            hover"game4_p2a_clic"
            hotspot(376, 148, 512, 53) clicked Jump("errado4_p2")
            hotspot(376, 208, 512, 53) clicked Jump("errado4_p2")
            hotspot(376, 277, 512, 53) clicked Jump("errado4_p2")
            hotspot(376, 364, 512, 53) clicked Jump("certo4_p2")

    screen game4_2b:
        imagemap:
            ground"game4_p2b"
            hover"game4_p2b_clic"
            hotspot(376, 148, 512, 53) clicked Jump("errado4_p2")
            hotspot(376, 208, 512, 53) clicked Jump("errado4_p2")
            hotspot(376, 277, 512, 53) clicked Jump("errado4_p2")
            hotspot(376, 364, 512, 53) clicked Jump("certo4_p2")
    
    #GAME 5============================================================================================================================
    screen game5_1:
        imagemap:
            ground"game5_p1a"
            hover"game5_p1a_clic"
            hotspot(369, 145, 213, 34) clicked Jump("errado5_p1")
            hotspot(369, 187, 213, 34) clicked Jump("errado5_p1")
            hotspot(369, 233, 213, 34) clicked Jump("errado5_p1")
            hotspot(369, 273, 213, 34) clicked Jump("certo5_p1")


    screen game5_1b:
        imagemap:
            ground"game5_p1b"
            hover"game5_p1b_clic"
            hotspot(369, 145, 213, 34) clicked Jump("errado5_p1")
            hotspot(369, 187, 213, 34) clicked Jump("errado5_p1")
            hotspot(369, 233, 213, 34) clicked Jump("errado5_p1")
            hotspot(369, 273, 213, 34) clicked Jump("certo5_p1")
    
    screen game5_2:
        imagemap:
            ground"game5_p2a"
            hover"game5_p2a_clic"
            hotspot(368, 145, 545, 63) clicked Jump("errado5_p2")
            hotspot(368, 211, 545, 63) clicked Jump("certo5_p2")
            hotspot(368, 264, 545, 63) clicked Jump("errado5_p2")
            hotspot(368, 318, 545, 63) clicked Jump("errado5_p2")

    screen game5_2b:
        imagemap:
            ground"game5_p2b"
            hover"game5_p2b_clic"
            hotspot(368, 145, 545, 63) clicked Jump("errado5_p2")
            hotspot(368, 211, 545, 63) clicked Jump("certo5_p2")
            hotspot(368, 264, 545, 63) clicked Jump("errado5_p2")
            hotspot(368, 318, 545, 63) clicked Jump("errado5_p2")

#GAME 6===========================================================================================================================

    screen game6_1:
        imagemap:
            ground"game6_p1a"
            hover"game6_p1a_clic"
            hotspot(366, 127, 545, 63) clicked Jump("errado6_p1")
            hotspot(366, 184, 545, 63) clicked Jump("errado6_p1")
            hotspot(366, 247, 545, 63) clicked Jump("certo6_p1")
            hotspot(366, 315, 545, 63) clicked Jump("errado6_p1")

    screen game6_1b:
        imagemap:
            ground"game6_p1b"
            hover"game6_p1b_clic"
            hotspot(366, 127, 545, 63) clicked Jump("errado6_p1")
            hotspot(366, 184, 545, 63) clicked Jump("errado6_p1")
            hotspot(366, 247, 545, 63) clicked Jump("certo6_p1")
            hotspot(366, 315, 545, 63) clicked Jump("errado6_p1")
    
    screen game6_2:
        imagemap:
            ground"game6_p2a"
            hover"game6_p2a_clic"
            hotspot(379, 164, 348, 49) clicked Jump("certo6_p2")
            hotspot(379, 201, 348, 49) clicked Jump("errado6_p2")
            hotspot(379, 245, 348, 49) clicked Jump("errado6_p2")
            hotspot(379, 284, 348, 49) clicked Jump("errado6_p2")

    screen game6_2b:
        imagemap:
            ground"game6_p2b"
            hover"game6_p2b_clic"
            hotspot(379, 164, 348, 49) clicked Jump("certo6_p2")
            hotspot(379, 201, 348, 49) clicked Jump("errado6_p2")
            hotspot(379, 245, 348, 49) clicked Jump("errado6_p2")
            hotspot(379, 284, 348, 49) clicked Jump("errado6_p2")

#___________________________________________________________________________________________________

label startmenu:
    call screen p_menu

label lingua:
    if not ingles:
        $ingles=True
        call screen settings
    elif ingles:
        $ingles=False
        call screen config

label configuracoes:
    call screen config

label creditos:
    scene credito1
    ""
    call screen p_menu
label som_desativo:
    $som=False
    stop music
    if not ingles:
        call screen config
    elif ingles:
        call screen settings
label som_ativo:
    $som=True
    play music "cook.mp3"
    if not ingles:
        call screen config
    elif ingles:
        call screen settings
#aqui começam os minigames
#================================================================================================================
label certo1_p1:
    scene acertou1
    ""
    if pontos==30:
        call screen game1_2
    elif pontos==20:
        call screen game1_2b
    elif pontos==10:
        call screen game1_2c

label errado1_p1:
    scene errou1
    ""
    $pontos-=10
    if pontos==0:
        $pontos=30
        scene derrota1_1
        ""
        scene derrota1_2
        ""
        call screen game1_1
    elif pontos==20:
        call screen game1_1b
    elif pontos==10:
        call screen game1_1c
label certo1_p2:
    scene acertou1_2
    ""
    scene acertou1_2b
    ""
    scene acertou1_2c
    ""
    if pontos==30:
        call screen game1_3
    elif pontos==20:
        call screen game1_3b
    elif pontos==10:
        call screen game1_3c

label errado1_p2:
    scene errou1_2
    ""
    $pontos-=10
    if pontos==0:
        $pontos=30
        scene derrota1_1
        ""
        scene derrota1_2
        ""
        call screen game1_1
    elif pontos==20:
        call screen game1_2b
    elif pontos==10:
        call screen game1_2c
label certo1_p3:
    scene acertou1_3
    ""
    scene vitoria1
    $total+=pontos
    "{size=40}{font=Kitto.otf}sua pontuação foi %(pontos)d.{/size}{/font}"
    jump lanche
label errado1_p3:
    $pontos-=10
    scene errou1_3
    ""
    if pontos==0:
        $pontos=30
        scene derrota1_1
        ""
        scene derrota1_2
        ""
        call screen game1_1
    elif pontos==20:
        call screen game1_3b
    elif pontos==10:
        call screen game1_3c
#GAME 2========================================================================================================
label certo2_p1:
    scene acertou2_1
    ""
    if pontos==20:
        call screen game2_2
    elif pontos==10:
        call screen game2_2b
label errado2_p1:
    $pontos-=10
    if pontos==0:
        scene derrota2
        ""
        $pontos=20
        call screen game2_1
    elif pontos==10:
        scene errou2_1
        ""
        call screen game2_1b
label certo2_p2:
    scene acertou2_2
    
    ""
    scene vitoria1
    $total+=pontos
    "{size=40}{font=Kitto.otf}sua pontuação foi %(pontos)d.{/size}{/font}"
    call screen game3_1

label errado2_p2:

    $pontos-=10
    if pontos==0:
        scene derrota2
        ""
        $pontos=20
        call screen game2_1
    elif pontos==10:
        scene errou2_2
        ""
        call screen game2_2b
#GAME 3====================================================================================================================
label certo3_p1:
    scene acertou3_1
    ""
    if pontos==20:
        call screen game3_2
    elif pontos==10:
        call screen game3_2b
label errado3_p1:
    $pontos-=10
    if pontos==0:
        scene derrota3
        ""
        $pontos=20
        call screen game3_1
    elif pontos==10:
        scene errou3_2
        ""
        call screen game3_1b
label certo3_p2:
    scene acertou3_2
    
    ""
    scene vitoria1
    $total+=pontos
    "{size=40}{font=Kitto.otf}sua pontuação foi %(pontos)d.{/size}{/font}"
    $pontos=20

    call screen game4_1
label errado3_p2:
    $pontos-=10
    if pontos==0:
        scene derrota3
        ""
        $pontos=20
        call screen game3_1
    elif pontos==10:
        scene errou3_2
        ""
        call screen game3_2b
#GAME 4======================================================================================================================
label certo4_p1:
    scene acertou4_1
    ""
    if pontos==20:
        call screen game4_2
    elif pontos==10:
        call screen game4_2b
label errado4_p1:
    $pontos-=10
    if pontos==0:
        scene derrota4
        ""
        $pontos=20
        call screen game4_1
    elif pontos==10:
        scene errou4_2
        ""
        call screen game4_1b
label certo4_p2:
    scene acertou4_2
    
    ""
    scene vitoria1
    $total+=pontos
    "{size=40}{font=Kitto.otf}sua pontuação foi %(pontos)d.{/size}{/font}"
    jump continua2
label errado4_p2:
    $pontos-=10
    if pontos==0:
        scene derrota4
        ""
        $pontos=20
        call screen game4_1
    elif pontos==10:
        scene errou4_2
        ""
        call screen game4_2b
#GAME 5====================================================================================================================
label certo5_p1:
    scene acertou5_1
    ""
    if pontos==20:
        call screen game5_2
    elif pontos==10:
        call screen game5_2b
label errado5_p1:
    $pontos-=10
    if pontos==0:
        scene derrota5
        ""
        $pontos=20
        call screen game5_1
    elif pontos==10:
        scene errou5_2
        ""
        call screen game5_1b
label certo5_p2:
    scene acertou5_2
    
    ""
    scene vitoria1
    $total+=pontos
    "{size=40}{font=Kitto.otf}sua pontuação foi %(pontos)d.{/size}{/font}"
    call screen game6_1
label errado5_p2:
    $pontos-=10
    if pontos==0:
        scene derrota5
        ""
        $pontos=20
        call screen game5_1
    elif pontos==10:
        scene errou5_2
        ""
        call screen game5_2b

#GAME 6==============================================================================================================
label certo6_p1:
    scene acertou6_1
    ""
    if pontos==20:
        call screen game6_2
    elif pontos==10:
        call screen game6_2b
label errado6_p1:
    $pontos-=10
    if pontos==0:
        scene derrota6
        ""
        $pontos=20
        call screen game6_1
    elif pontos==10:
        scene errou6_2
        ""
        call screen game6_1b
label certo6_p2:
    scene acertou6_2
    
    ""
    scene vitoria1
    $total+=pontos
    "{size=40}{font=Kitto.otf}sua pontuação foi %(pontos)d.{/size}{/font}"
    jump continua3
label errado6_p2:
    $pontos-=10
    if pontos==0:
        scene derrota6
        ""
        $pontos=20
        call screen game6_1
    elif pontos==10:
        scene errou6_2
        ""
        call screen game6_2b


#aqui começa a parte verde #1
#====================================================================================================================================================

label inicio:

    stop music fadeout 1.0
    if som:
        play music "Memo_cute_8_bit_chiptune.mp3"
    scene quarto
    with dissolve
    scene fala00
    ""
    if som:
        play sound "despertador.mp3"
    scene fala01
    ""

    scene celular

    show fala02
    ""

    show fala03
    ""

    scene fala04
    ""

    scene fala05
    ""

    scene fala06
    ""

    scene fala07
    ""

    scene fala08
    ""

    scene fala09
    ""


    scene fala10
    ""

    scene fala11
    ""


#Aqui começa a parte vermelha #2
#=======================================================================================================================================


    scene fala12
    ""

    scene fala13
    ""

    scene fala14
    ""

    scene fala15
    ""


    scene fala16
    ""


    scene fala17
    ""

    scene fala18
    ""

    scene fala19
    ""



#====MINI GAME1====MINI GAME1====MINI GAME1====MINI GAME1====MINI GAME1====MINI GAME1====MINI GAME1====MINI GAME1====
    $pontos=30
    scene pre_game1
    ""
    call screen game1_1

    hide tony9

    jump lanche

label lanche:
    scene pos_game01
    ""
    scene pos_game02
    ""
    scene pos_game03
    ""
    scene pos_game04
    ""
    scene pos_game05
    ""
    scene pos_game06
    ""
    scene pos_game07
    ""
    scene pos_game08
    ""
    scene pos_game09
    ""
    scene pos_game10
    ""
    scene pos_game11
    ""
    scene pos_game12
    ""
    scene pos_game13
    ""
    scene pos_game14
    ""
    scene pos_game15
    ""
    scene pos_game16
    ""
    scene pos_game17
    ""
    scene pos_game18
    ""
    scene pos_game19
    ""
    scene pos_game20
    ""
    scene pos_game21
    if som:
        play sound "sinal-escolar.mp3"
    scene pos_game22
    ""
    scene pos_game23
    ""
    scene pos_game24
    ""
    scene pos_game25
    ""
    scene pos_game26
    ""
    scene pos_game27
    ""
    scene pos_game28
    ""
    scene pos_game29
    ""
    scene pos_game30
    ""
    scene pos_game31
    ""
    scene pos_game32
    ""
    scene pos_game33
    ""
    scene pos_game34
    ""
    scene pos_game35
    ""
    scene pos_game36
    ""
    scene pos_game37
    ""
    scene pos_game38
    ""
    scene pos_game39
    ""
    scene pos_game40
    ""
    scene pos_game41
    ""
    scene pos_game42
    ""
    scene pos_game43
    ""
    scene pos_game44
    ""
    scene pos_game45
    ""

#====MINI GAME2====MINI GAME2====MINI GAME2====MINI GAME2====MINI GAME2====MINI GAME2====MINI GAME2====MINI GAME2====
    $pontos=20
    call screen game2_1
label continua2:
    scene pos_game46
    ""
    scene pos_game47
    ""
    scene pos_game48
    ""
    scene pos_game49
    ""
    scene pos_game50
    ""
    scene pos_game51
    ""
    scene pos_game52
    ""
    scene pos_game53
    ""

#Aqui começa a parte roxa #7
#=============================================================================================================================================
#====MINI GAME3====MINI GAME3====MINI GAME3====MINI GAME3====MINI GAME3====MINI GAME3====MINI GAME3====MINI GAME3====
    $pontos=20
    call screen game5_1
label continua3:

    scene posfinalização1
    call screen pergunta
    screen pergunta:
        imagemap:
            ground"pergunta1"
            hover"pergunta1_clic"
            hotspot(108, 185, 576, 96) clicked Jump("variante1")
            hotspot(108, 280, 576, 96) clicked Jump("variante2")
label variante1:
    scene resposta1
    ""
    jump final
label variante2:
    scene resposta2
    ""
    jump final
label final:
    scene fim
    "{size=40}{font=Kitto.otf}sua pontuação total foi de %(total)d pontos.{/size}{/font}"
    jump start
# PARTE EM INGLÊS
#=======================================================================================================================================

label menuenglish:
    $total=0
    screen touch:
        imagemap:
            ground"menuinicialenglish1.png"
            hover"menuinicialenglishclicked.png"
            hotspot(29, 303, 342, 89) clicked Jump("startenglish")
            hotspot(29, 391, 342, 89) clicked Jump("settings")
            hotspot(29, 480, 342, 89) clicked Jump("credits")

    screen settings:
        imagemap:
            ground"configenglish1.png"
            hover"configenglishclicked.png"
            hotspot(80, 336, 296, 79) clicked Jump("lingua")
            hotspot(70, 427, 296, 79) clicked Jump("settings")
            hotspot(474, 340, 296, 79) clicked Jump("som_ativo")
            hotspot(472, 426, 296, 79) clicked Jump("som_desativo")
            hotspot(274, 514, 296, 79) clicked Jump("menuenglish")
label play:

    call screen touch

label settings:
    call screen settings

label credits:
    scene credito2
    ""
    jump menuenglish

label games:
#GAME 1==================================================================================================================
    screen game1_1i:
        imagemap:
            ground"game1_p1ai"
            hover"game1_p1ai_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p1i")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p1i")#B
            hotspot(354, 282, 574, 84) clicked Jump("certo1_p1i")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p1i")#D
    screen game1_1bi:
        imagemap:
            ground"game1_p1bi"
            hover"game1_p1bi_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p1i")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p1i")#B
            hotspot(354, 282, 574, 84) clicked Jump("certo1_p1i")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p1i")#D
    screen game1_1ci:
        imagemap:
            ground"game1_p1ci"
            hover"game1_p1ci_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p1i")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p1i")#B
            hotspot(354, 282, 574, 84) clicked Jump("certo1_p1i")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p1i")#D

    screen game1_2i:
        imagemap:
            ground"game1_p2ai"
            hover"game1_p2ai_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p2i")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p2i")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p2i")#C
            hotspot(354, 375, 574, 84) clicked Jump("certo1_p2i")#D
    
    screen game1_2bi:
        imagemap:
            ground"game1_p2bi"
            hover"game1_p2bi_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p2i")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p2i")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p2i")#C
            hotspot(354, 375, 574, 84) clicked Jump("certo1_p2i")#D

    screen game1_2ci:
        imagemap:
            ground"game1_p2ci"
            hover"game1_p2ci_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p2i")#A
            hotspot(354, 190, 574, 84) clicked Jump("errado1_p2i")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p2i")#C
            hotspot(354, 375, 574, 84) clicked Jump("certo1_p2i")#D

    screen game1_3i:
        imagemap:
            ground"game1_p3ai"
            hover"game1_p3ai_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p3i")#A
            hotspot(354, 190, 574, 84) clicked Jump("certo1_p3i")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p3i")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p3i")#D
    
    screen game1_3bi:
        imagemap:
            ground"game1_p3bi"
            hover"game1_p3bi_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p3i")#A
            hotspot(354, 190, 574, 84) clicked Jump("certo1_p3i")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p3i")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p3i")#D
    
    screen game1_3ci:
        imagemap:
            ground"game1_p3ci"
            hover"game1_p3ci_clic"
            hotspot(354, 99, 574, 84) clicked Jump("errado1_p3i")#A
            hotspot(354, 190, 574, 84) clicked Jump("certo1_p3i")#B
            hotspot(354, 282, 574, 84) clicked Jump("errado1_p3i")#C
            hotspot(354, 375, 574, 84) clicked Jump("errado1_p3i")#D

#GAME1================================================================================================================
label certo1_p1i:
    scene acertou1i
    ""
    if pontos==30:
        call screen game1_2i
    elif pontos==20:
        call screen game1_2bi
    elif pontos==10:
        call screen game1_2ci

label errado1_p1i:
    scene errou1i
    ""
    $pontos-=10
    if pontos==0:
        $pontos=30
        scene derrota1_1i
        ""
        scene derrota1_2i
        ""
        call screen game1_1i
    elif pontos==20:
        call screen game1_1bi
    elif pontos==10:
        call screen game1_1ci
label certo1_p2i:
    scene acertou1_2i
    ""
    scene acertou1_2bi
    ""
    scene acertou1_2ci
    ""
    if   pontos==30:
        call screen game1_3i
    elif pontos==20:
        call screen game1_3bi
    elif pontos==10:
        call screen game1_3ci

label errado1_p2i:
    scene errou1_2i
    ""
    $pontos-=10
    if pontos==0:
        $pontos=30
        scene derrota1_1i
        ""
        scene derrota1_2i
        ""
        call screen game1_1i
    elif pontos==20:
        call screen game1_2bi
    elif pontos==10:
        call screen game1_2ci
label certo1_p3i:
    scene acertou1_3i
    ""
    scene vitoria1i
    $total+=pontos
    "{size=40}{font=Kitto.otf}your score is %(pontos)d points.{/size}{/font}"
    jump snack
label errado1_p3i:
    $pontos-=10
    scene errou1_3i
    ""
    if pontos==0:
        $pontos=30
        scene derrota1_1i
        ""
        scene derrota1_2i
        ""
        call screen game1_1i
    elif pontos==20:
        call screen game1_3bi
    elif pontos==10:
        call screen game1_3ci


#GAME 2==============================================================================================================================
  
  
    screen game2_1i:
        imagemap:
            ground"game2_p1ai"
            hover"game2_p1ai_clic"
            hotspot(379, 184, 306, 31) clicked Jump("certo2_p1i")#A
            hotspot(379, 210, 306, 31) clicked Jump("errado2_p1i")#B
            hotspot(379, 236, 306, 31) clicked Jump("errado2_p1i")#C
            hotspot(379, 263, 306, 31) clicked Jump("errado2_p1i")#D

    screen game2_1bi:
        imagemap:
            ground"game2_p1bi"
            hover"game2_p1bi_clic"
            hotspot(379, 184, 306, 31) clicked Jump("certo2_p1i")#A
            hotspot(379, 210, 306, 31) clicked Jump("errado2_p1i")#B
            hotspot(379, 236, 306, 31) clicked Jump("errado2_p1i")#C
            hotspot(379, 263, 306, 31) clicked Jump("errado2_p1i")#D

    screen game2_2i:
        imagemap:
            ground"game2_p2ai"
            hover"game2_p2ai_clic"
            hotspot(375, 141, 555, 93) clicked Jump("errado2_p2i")
            hotspot(375, 228, 521, 69) clicked Jump("errado2_p2i")
            hotspot(375, 296, 518, 112) clicked Jump("errado2_p2i")
            hotspot(375, 423, 555, 93) clicked Jump("certo2_p2i")

    screen game2_2bi:
        imagemap:
            ground"game2_p2bi"
            hover"game2_p2bi_clic"
            hotspot(375, 141, 555, 93) clicked Jump("errado2_p2i")
            hotspot(375, 228, 521, 69) clicked Jump("errado2_p2i")
            hotspot(375, 296, 518, 112) clicked Jump("errado2_p2i")
            hotspot(375, 423, 555, 93) clicked Jump("certo2_p2i")


#GAME 2========================================================================================================
label certo2_p1i:
    scene acertou2_1i
    ""
    if pontos==20:
        call screen game2_2i
    elif pontos==10:
        call screen game2_2bi
label errado2_p1i:
    $pontos-=10
    if pontos==0:
        scene derrota2i
        ""
        $pontos=20
        call screen game2_1i
    elif pontos==10:
        scene errou2_1i
        ""
        call screen game2_1bi
label certo2_p2i:
    scene acertou2_2i
    
    ""
    scene vitoria1i
    $total+=pontos
    "{size=40}{font=Kitto.otf}your score is %(pontos)d points.{/size}{/font}"
    call screen game3_1i

label errado2_p2i:

    $pontos-=10
    if pontos==0:
        scene derrota2i
        ""
        $pontos=20
        call screen game2_1i
    elif pontos==10:
        scene errou2_2i
        ""
        call screen game2_2bi

#GAME 3========================================================================================
    screen game3_1i:
        imagemap:
            ground"game3_p1ai"
            hover"game3_p1ai_clic"
            hotspot(363, 150, 531, 76) clicked Jump("errado3_p1i")
            hotspot(363, 219, 531, 76) clicked Jump("errado3_p1i")
            hotspot(363, 294, 585, 74) clicked Jump("certo3_p1i")
            hotspot(363, 356, 585, 74) clicked Jump("errado3_p1i")
    screen game3_1bi:
        imagemap:
            ground"game3_p1bi"
            hover"game3_p1bi_clic"
            hotspot(363, 150, 531, 76) clicked Jump("errado3_p1i")
            hotspot(363, 219, 531, 76) clicked Jump("errado3_p1i")
            hotspot(363, 294, 585, 74) clicked Jump("certo3_p1i")
            hotspot(363, 356, 585, 74) clicked Jump("errado3_p1i")
    screen game3_2i:
        imagemap:
            ground"game3_p2ai"
            hover"game3_p2ai_clic"
            hotspot(373, 284, 185, 29) clicked Jump("errado3_p2i")
            hotspot(373, 326, 185, 29) clicked Jump("certo3_p2i")
            hotspot(373, 375, 178, 38) clicked Jump("errado3_p2i")
            hotspot(373, 417, 178, 38) clicked Jump("errado3_p2i")         
    screen game3_2bi:
        imagemap:
            ground"game3_p2bi"
            hover"game3_p2bi_clic"
            hotspot(373, 284, 185, 29) clicked Jump("errado3_p2i")
            hotspot(373, 326, 185, 29) clicked Jump("certo3_p2i")
            hotspot(373, 375, 178, 38) clicked Jump("errado3_p2i")
            hotspot(373, 417, 178, 38) clicked Jump("errado3_p2i")

#GAME 3====================================================================================================================
label certo3_p1i:
    scene acertou3_1i
    ""
    if pontos==20:
        call screen game3_2i
    elif pontos==10:
        call screen game3_2bi
label errado3_p1i:
    $pontos-=10
    if pontos==0:
        scene derrota3i
        ""
        $pontos=20
        call screen game3_1i
    elif pontos==10:
        scene errou3_2i
        ""
        call screen game3_1bi
label certo3_p2i:
    scene acertou3_2i
    
    ""
    scene vitoria1i
    $total+=pontos
    "{size=40}{font=Kitto.otf}your score is %(pontos)d points.{/size}{/font}"
    call screen game4_1i
label errado3_p2i:
    $pontos-=10
    if pontos==0:
        scene derrota3i
        ""
        $pontos=20
        call screen game3_1i
    elif pontos==10:
        scene errou3_2i
        ""
        call screen game3_2bi

#GAME 4========================================================================================================

    screen game4_1i:
        imagemap:
            ground"game4_p1ai"
            hover"game4_p1ai_clic"
            hotspot(364, 159, 553, 64) clicked Jump("errado4_p1i")
            hotspot(364, 220, 553, 64) clicked Jump("errado4_p1i")
            hotspot(364, 295, 553, 64) clicked Jump("certo4_p1i")
            hotspot(364, 352, 553, 64) clicked Jump("errado4_p1i")

    screen game4_1bi:
        imagemap:
            ground"game4_p1bi"
            hover"game4_p1bi_clic"
            hotspot(364, 159, 553, 64) clicked Jump("errado4_p1i")
            hotspot(364, 220, 553, 64) clicked Jump("errado4_p1i")
            hotspot(364, 295, 553, 64) clicked Jump("certo4_p1i")
            hotspot(364, 352, 553, 64) clicked Jump("errado4_p1i")
    
    screen game4_2i:
        imagemap:
            ground"game4_p2ai"
            hover"game4_p2ai_clic"
            hotspot(367, 157, 552, 64) clicked Jump("errado4_p2i")
            hotspot(367, 222, 552, 64) clicked Jump("errado4_p2i")
            hotspot(367, 291, 552, 64) clicked Jump("errado4_p2i")
            hotspot(367, 360, 552, 64) clicked Jump("certo4_p2i")

    screen game4_2bi:
        imagemap:
            ground"game4_p2bi"
            hover"game4_p2bi_clic"
            hotspot(367, 157, 552, 64) clicked Jump("errado4_p2i")
            hotspot(367, 222, 552, 64) clicked Jump("errado4_p2i")
            hotspot(367, 291, 552, 64) clicked Jump("errado4_p2i")
            hotspot(367, 360, 552, 64) clicked Jump("certo4_p2i")

#GAME 5============================================================================================================================
    screen game5_1i:
        imagemap:
            ground"game5_p1ai"
            hover"game5_p1ai_clic"
            hotspot(377, 156, 201, 44) clicked Jump("errado5_p1i")
            hotspot(377, 200, 201, 44) clicked Jump("errado5_p1i")
            hotspot(377, 249, 201, 44) clicked Jump("errado5_p1i")
            hotspot(377, 292, 201, 44) clicked Jump("certo5_p1i")


    screen game5_1bi:
        imagemap:
            ground"game5_p1bi"
            hover"game5_p1bi_clic"
            hotspot(377, 156, 201, 44) clicked Jump("errado5_p1i")
            hotspot(377, 200, 201, 44) clicked Jump("errado5_p1i")
            hotspot(377, 249, 201, 44) clicked Jump("errado5_p1i")
            hotspot(377, 292, 201, 44) clicked Jump("certo5_p1i")
    
    screen game5_2i:
        imagemap:
            ground"game5_p2ai"
            hover"game5_p2ai_clic"
            hotspot(369, 152, 550, 75) clicked Jump("errado5_p2i")
            hotspot(369, 222, 550, 75) clicked Jump("certo5_p2i")
            hotspot(369, 291, 550, 75) clicked Jump("errado5_p2i")
            hotspot(369, 358, 550, 75) clicked Jump("errado5_p2i")

    screen game5_2bi:
        imagemap:
            ground"game5_p2bi"
            hover"game5_p2bi_clic"
            hotspot(369, 152, 550, 75) clicked Jump("errado5_p2i")
            hotspot(369, 222, 550, 75) clicked Jump("certo5_p2i")
            hotspot(369, 291, 550, 75) clicked Jump("errado5_p2i")
            hotspot(369, 358, 550, 75) clicked Jump("errado5_p2i")
#GAME 5====================================================================================================================
label certo5_p1i:
    scene acertou5_1i
    ""
    if pontos==20:
        call screen game5_2i
    elif pontos==10:
        call screen game5_2bi
label errado5_p1i:
    $pontos-=10
    if pontos==0:
        scene derrota5i
        ""
        $pontos=20
        call screen game5_1i
    elif pontos==10:
        scene errou5_2i
        ""
        call screen game5_1bi
label certo5_p2i:
    scene acertou5_2i
    ""
    scene vitoria1i
    $total+=pontos
    "{size=40}{font=Kitto.otf}your score is %(pontos)d points.{/size}{/font}"
    call screen game6_1i
label errado5_p2i:
    $pontos-=10
    if pontos==0:
        scene derrota5i
        ""
        $pontos=20
        call screen game5_1i
    elif pontos==10:
        scene errou5_2i
        ""
        call screen game5_2bi
label certo4_p1i:
    scene acertou4_1i
    ""
    if pontos==20:
        call screen game4_2i
    elif pontos==10:
        call screen game4_2bi
label errado4_p1i:
    $pontos-=10
    if pontos==0:
        scene derrota4i
        ""
        $pontos=20
        call screen game4_1i
    elif pontos==10:
        scene errou4_2i
        ""
        call screen game4_1bi
label certo4_p2i:
    scene acertou4_2i
    
    ""
    scene vitoria1i
    $total+=pontos
    "{size=40}{font=Kitto.otf}your score is %(pontos)d points.{/size}{/font}"
    jump continua2i
label errado4_p2i:
    $pontos-=10
    if pontos==0:
        scene derrota4i
        ""
        $pontos=20
        call screen game4_1i
    elif pontos==10:
        scene errou4_2i
        ""
        call screen game4_2bi
#GAME 6===========================================================================================================================

    screen game6_1i:
        imagemap:
            ground"game6_p1ai"
            hover"game6_p1ai_clic"
            hotspot(186, 134, 548, 57) clicked Jump("errado6_p1i")
            hotspot(186, 190, 548, 57) clicked Jump("errado6_p1i")
            hotspot(186, 250, 548, 57) clicked Jump("certo6_p1i")
            hotspot(186, 307, 548, 57) clicked Jump("errado6_p1i")

    screen game6_1bi:
        imagemap:
            ground"game6_p1bi"
            hover"game6_p1bi_clic"
            hotspot(186, 134, 548, 57) clicked Jump("errado6_p1i")
            hotspot(186, 190, 548, 57) clicked Jump("errado6_p1i")
            hotspot(186, 250, 548, 57) clicked Jump("certo6_p1i")
            hotspot(186, 307, 548, 57) clicked Jump("errado6_p1i")
    
    screen game6_2i:
        imagemap:
            ground"game6_p2ai"
            hover"game6_p2ai_clic"
            hotspot(379, 164, 348, 49) clicked Jump("certo6_p2i")
            hotspot(379, 201, 348, 49) clicked Jump("errado6_p2i")
            hotspot(379, 245, 348, 49) clicked Jump("errado6_p2i")
            hotspot(364, 333, 171, 47) clicked Jump("errado6_p2i")

    screen game6_2bi:
        imagemap:
            ground"game6_p2bi"
            hover"game6_p2bi_clic"
            hotspot(379, 164, 348, 49) clicked Jump("certo6_p2i")
            hotspot(379, 201, 348, 49) clicked Jump("errado6_p2i")
            hotspot(379, 245, 348, 49) clicked Jump("errado6_p2i")
            hotspot(364, 333, 171, 47) clicked Jump("errado6_p2i")

#GAME 6==============================================================================================================
label certo6_p1i:
    scene acertou6_1i
    ""
    if pontos==20:
        call screen game6_2i
    elif pontos==10:
        call screen game6_2bi
label errado6_p1i:
    $pontos-=10
    if pontos==0:
        scene derrota6i
        ""
        $pontos=20
        call screen game6_1i
    elif pontos==10:
        scene errou6_2i
        ""
        call screen game6_1bi
label certo6_p2i:
    scene acertou6_2i
    
    ""
    scene vitoria1i
    $total+=pontos
    "{size=40}{font=Kitto.otf}your score is %(pontos)d points.{/size}{/font}"
    jump continua3i
label errado6_p2i:
    $pontos-=10
    if pontos==0:
        scene derrota6i
        ""
        $pontos=20
        call screen game6_1i
    elif pontos==10:
        scene errou6_2i
        ""
        call screen game6_2bi


label startenglish:
    screen pergunta1i:
        imagemap:
            ground"perguntai"
            hover"perguntai_clic"
            hotspot(108, 185, 576, 96) clicked Jump("variante1i")
            hotspot(108, 280, 576, 96) clicked Jump("variante1i")
    stop music fadeout 1.0
    if som:
        play music "Memo_cute_8_bit_chiptune.mp3"
    scene quarto
    with dissolve
    scene fala00i
    ""
    if som:
        play sound "despertador.mp3"
    scene fala01i
    ""

    scene celular

    show fala02i
    ""

    show fala03i
    ""

    scene fala04i
    ""

    scene fala05i
    ""

    scene fala06i
    ""

    scene fala07i
    ""

    scene fala08i
    ""

    scene fala09i
    ""


    scene fala10i
    ""

    scene fala11i
    ""


#Aqui começa a parte vermelha #2
#=======================================================================================================================================


    scene fala12i
    ""

    scene fala13i
    ""

    scene fala14i
    ""

    scene fala15i
    ""


    scene fala16i
    ""


    scene fala17i
    ""

    scene fala18i
    ""

    scene fala19i
    ""
    $pontos=30
    call screen game1_1i

    jump snack

label snack:
    scene scene01
    ""
    scene scene02
    ""
    scene scene03
    ""
    scene scene04
    ""
    scene scene05
    ""
    scene scene06
    ""
    scene scene07
    ""
    scene scene08
    ""
    scene scene09
    ""
    scene scene10
    ""
    scene scene11
    ""
    scene scene12
    ""
    scene scene13
    ""
    scene scene14
    ""
    scene scene15
    ""
    scene scene16
    ""
    scene scene17
    ""
    scene scene18
    ""
    scene scene19
    ""
    scene scene20
    ""
    scene scene21
    ""
    scene scene22
    if som:
        play sound "sinal-escolar.mp3"
    ""
    scene scene23
    ""
    scene scene24
    ""
    scene scene25
    ""
    scene scene26
    ""
    scene scene27
    ""
    scene scene28
    ""
    scene scene29
    ""
    scene scene30
    ""
    scene scene31
    ""
    scene scene32
    ""
    scene scene33
    ""
    scene scene34
    ""
    scene scene35
    ""
    scene scene36
    ""
    scene scene37
    ""
    scene scene38
    ""
    scene scene39
    ""
    scene scene40
    ""
    scene scene41
    ""
    scene scene42
    ""
    scene scene43
    ""
    scene scene44
    ""
    scene scene45
    ""
    $pontos=20
    call screen game2_1i
    scene pos_prova2
    ""
    label continua2i:
        scene posi1
        ""
        scene posi2
        ""
        scene posi3
        ""
        scene posi4
        ""
        scene posi5
        ""
        scene posi6
        ""
        scene posi7
        ""
        scene posi8
        ""

        call screen game5_1i
    label continua3i:
        scene posfimi
        ""
        call screen pergunta1i

        
label variante1i:
    scene resposta1i
    ""
    jump finali
label variante2i:
    scene resposta2i
    ""
    jump finali
label finali:
    scene fim
    "{size=40}{font=Kitto.otf}your total score is %(total)d points.{/size}{/font}"
    jump menuenglish
        





  

# Aqui começa a parte laranja #4
#========================================================================================================================================

