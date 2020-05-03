# Coloca el código de tu juego en este archivo.
define gui.about = _("""\
Creado por Susana Sánchez Muñoz, Alekadra Mitiajeva, Andrea Cabrera Torres

CC BY-NC 4.0""")

image goblin ="goblin.png"
image goblin2 ="goblin2.png"
image goblin2 ="goblin2.png"
image porfi ="porfi.png"
image porfi2 ="porfi2.png"
image porfi3 ="porfi3.png"
image porfi4 ="porfi4.png"
image porfi5 ="porfi5.png"
image alicia ="alicia.png"
image alicia2 ="alicia2.png"
image vhs ="vhs.png"
image camarero ="camarero.png"
image descampado ="descampado.jpg"
image tranvia ="tranvia.jpg"
image tranviainterior ="tranviainterior.jpg"
image telepizza ="telepizza.jpg"
image casa ="casa.jpg"
image emocasa ="emocasa.jpg"
image calle ="calle.jpg"
image sordos ="sordos.jpg"
image riendo ="riendo.jpg"
image casafuturo ="casafuturo.jpg"
image farmacia ="farmacia.jpg"
image tobecontinued ="tobecontinued.jpg"
image torre ="torre.jpg"
image trap ="trap.png"
image telepizza-astorga ="telepizza-astorga.jpg"
image fecha ="fecha.jpg"
image fly ="fly.png"

define config.main_menu_music = "die.mp3" 
define g = Character("Goblin")
define p = Character("Porfi")
define c = Character("Camarero")
define s = Character("Grupo de sordos")
define a = Character("Alicia")


# El juego comienza aquí.

label start:
    

    scene descampado
    play music "The X-Files Theme.mp3" fadein 2.0
       
    "DÍA 1 - 22:00 - Goblin y Porfi salen de una cápsula. Se dan cuenta de que
    están en un descampado que les resulta extraño y desconocido."
    
    show porfi at right
    p "¿Estamos muertos?¿Por fin estamos muertos?¿De verdad lo hemos conseguido?"
    show goblin at left
    g "¿Y ahora qué?"

 
menu:
    p "Yo tengo hambre... ¿Vamos a buscar algo?"
    "¿Tú crees que aquí la comida sabrá mejor?":
      jump escena2
      
label escena2:
    stop music fadeout 2.0
    play music "lofim.mp3" fadein 2.0
    scene telepizza
    "Porfi y Goblin pasean por la ciudad mirando asombrados.
Encuentran un restaurante que les llama la atención. Aparece
su camarero de la nada."
    show camarero

    c "¡Nuestros menús son creados con especial amor! ¡Aquí la comida sabe incluso mejor que en el más allá! PICERRIA AMBURUGUESA SIPAI"
menu:
    p "¿Quieres que comamos algo aquí?"
    "Sí, ¡tengo mucha hambre!":
      jump hambre
    "No me da muy buena impresión ese sitio… Quizás deberíamos irnos a dar un paseo.":
     jump no

label hambre:
        play sound "restaurante2.mp3" fadein 2.0
        scene telepizza-astorga
"Entran al restaurante y piden una pizza. Salen de la pizzería horrorizados!"
show goblin2 at left
g "Estaba todo malísimo. Si esto es la vida después de la muerte quiero morir otra vez."
show porfi2 at right
p "Vamos a dar un paseo, a ver si se nos olvida esa pizza horrible"
jump tranvia 

label no:
"No me da muy buena impresión ese sitio… Quizás deberíamos irnos a dar un paseo."
jump tranvia

label tranvia:
        stop sound fadeout 2.0
        scene tranvia
"Empiezan a pasear por la ciudad y ven pasar un tranvía."
g "¡Mira! ¡Un tranvía! ¡Quiero montarme!"
jump interior

label interior:
    stop music fadeout 2.0
    scene tranviainterior
    play sound "tranvia.mp3" fadein 2.0

show porfi3 at right
p "Oye, ¿No se parece mucho a nuestra ciudad?"
show goblin3 at left
g "Ahora que lo dices..."
show porfi3 at right
p "¿No habían empezado las obras hace poco? ¡No entiendo nada! ¡Pero tengo una idea!"

menu:
    p "¿Buscamos nuestra casa?"
    "Sí, creo que es lo mejor.":
      jump escena4
      
label escena4:
    stop sound fadeout 2.0
    play sound "pajaritos.mp3"

    scene casa with fade
    "DÍA 2 - 10:00 - Saito duerme. Goblin sube a la cama de Saito y lo graba."
show goblin2 at left
g "¡Porfi despierta!¡Mira cómo está la casa!"
jump emotransition

label emotransition:
    stop sound fadeout 2.0
    play music "rock.mp3" fadein 2.0
    hide goblin2 at left
    scene emocasa with Dissolve(05.0)
show porfi2 at right
p "¡No me lo creo! Habían cambiado todas nuestras chatarras por unos... ¿Extraños aparatos?"
jump calle 
label calle:
    stop music fadeout 2.0
    play sound "Ciudad.mp3" fadein 2.0
    scene calle
    "DÍA 2 - 13:00 - Han decidido seguir explorando la ciudad, están andando por la calle."
show goblin5 at left
g "Aquí todo el mundo parece normal."
hide goblin5 at left
show porfi5 at right
p "¿Preguntamos a alguien si hay una asociación para emos aquí?"
hide porfi5 at right
show goblin5 at left
g "Sí, mira, vamos a preguntarle a esos, que parecen informados."
hide goblin5 at left
show porfi2 at right
p "hshshshs"
show goblin2 at left
g "hshshshs!! Tu ya tienes 18."
show porfi2 at right
p "¡Tienes razón! ¡Debo hacerlo!"
jump escena5

label escena5:
        scene sordos
"Porfi se acerca al grupo. Ellos dejan de mirarlos y se centran en sus móviles."
show porfi4 at right
p "¡Hola, soy Porfi! Mi amigo Goblin y yo somos nuevos por aquí. ¿Sabéis si hay una asociación para emos cerca?"
s " "
show porfi4 at right
p "¡Oye! ¡¿Podéis escucharme?!"
hide porfi4 at right
s " "
show goblin2 at left
menu:
    p "¡Que estoy aquí! ¡No soy invisible! ¿O lo soy? ¡Goblin! ¡¿Somos fantasmas?!"
    "¡Ahora nada me impide ser yo!":
      jump yo
    "No, debe haber una explicación lógica…":
     jump logica

label yo:
    play sound "riendo.mp3" fadein 2.0
    scene riendo
"Goblin se vuelve loco y baja los pantalones a Porfi. El grupo señala a Porfi y se ríen mientras le hacen fotos."
jump escena6 

label logica:
    scene trap
"Goblin mira y ve el cartel que pone detrás: “Asociación para sordos por el trap”."
jump escena6

label escena6:
        stop sound fadeout 2.0
        play music "lofim.mp3" fadein 2.0
        scene farmacia with fade
"Ambos siguen andando por la ciudad."
show goblin at left
g "Entonces no estamos muertos, y tampoco estamos locos."
show porfi at right
p "Así que, ¿Dónde estamos?"
jump fecha

label fecha:
        play sound "shock.mp3"
        scene fecha
"Porfi y Goblin ven el cartel de una farmacia, con la fecha"

menu:
    
    "¿Estamos en el futuro?"
    "FLASHBACK":
      jump back
    "FLASHFORWARD":
     jump forward

label back:
    stop music fadeout 2.0
    play music "CanFly.mp3" fadein 2.0
    scene torre with fade
    show fly at truecenter

"AÑO 2007 - Saltan desde la azotea de un edificio al vacío..."
p "Adiós, mundo cruel… Al menos nos vamos juntos."
g "¡Viva My Chemical Romance!"

jump forward 

label forward:
    stop music fadeout 2.0
    play music "lofi.mp3" fadein 2.0
    scene casafuturo with fade
"AÑO 2043 - Porfi habando con su hija Alicia"
show porfi2 at right
p "Hija, voy a contarte una historia increíble, la historia de cómo viaje al futuro."
hide porfi2 at right
show alicia at left
a "¡No papá! ¿no tienes otra historia?"
hide alicia at left
show porfi4 at right
p "Si no quieres escuchar la historia, al menos vamos a verla, no?"
hide porfi4 at right
show vhs at top
"Porfi enseña una cinta de video donde esta grabado el documental"
hide vhs at top
show alicia2 at left with Dissolve(02.0)
a "OK BOOMER"

jump escena7
label escena7:
        stop music fadeout 2.0
        play music "die.mp3" fadein 2.0
        scene tobecontinued
"{size=+10}{b}To be continued...{/b}{/size}"
return