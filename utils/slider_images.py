from django.templatetags.static import static
import random

TITLE = {
    1: "Undertale",
    2: "Undertale",
    3: "uncharted",
    4: "Forza Horizon",
    5: "Red Dead Rdemption 2",
    6: "The Legend of Zelda",
    7: "Minecraft",
    8: "Fortnite ",
    9: "Tomb Raider",
}

CONTENT = {
    1: "Undertale es un encantador RPG donde juegas como un niño que cae en el subsuelo, un mundo habitado por monstruos. A diferencia de otros juegos, en Undertale puedes elegir no luchar. En su lugar, puedes hablar con los monstruos y resolver conflictos pacíficamente. Tus decisiones afectan el curso de la historia, llevando a múltiples finales. Con personajes inolvidables, humor ingenioso, y una banda sonora excepcional, Undertale ofrece una experiencia emocionalmente rica y única. Sumérgete en este mundo y descubre cómo tus elecciones pueden marcar la diferencia en una aventura llena de sorpresas y momentos conmovedores. ¡No te lo pierdas!",
    2: "Undertale es un RPG único donde controlas a un niño que cae en un mundo subterráneo lleno de monstruos. A diferencia de otros juegos, puedes optar por no luchar y, en su lugar, resolver conflictos pacíficamente a través del diálogo. Tus decisiones afectan la trama, llevando a diferentes finales. Con personajes memorables, como Sans y Papyrus, y una banda sonora excepcional, Undertale ofrece una historia conmovedora y llena de humor. Explora este fascinante mundo subterráneo, donde cada elección importa, y descubre cómo tus acciones pueden cambiar el destino de sus habitantes. ¡Atrévete a vivir esta aventura incomparable!",
    3: "Uncharted es una serie de acción y aventura que sigue a Nathan Drake, un cazador de tesoros. Viaja a lugares exóticos, enfrenta enemigos mortales y resuelve rompecabezas antiguos. Con una narrativa cinematográfica, intensos combates y paisajes impresionantes, Uncharted ofrece una experiencia épica y emocionante. ¡Embárcate en esta aventura llena de acción!",
    4: "Forza Horizon 5 es un juego de carreras de mundo abierto ambientado en México. Explora paisajes variados, compite en emocionantes carreras y personaliza vehículos en esta experiencia visualmente impresionante y llena de adrenalina.",
    5: "Red Dead Redemption 2 es un épico juego de acción y aventura ambientado en el Salvaje Oeste americano. Explora un vasto mundo abierto, vive como un forajido y participa en emocionantes tiroteos y misiones llenas de decisiones morales.",
    6: "The Legend of Zelda es una icónica serie de videojuegos de aventuras desarrollada por Nintendo. Cada juego sigue a Link, un héroe que debe salvar el reino de Hyrule de las garras de Ganon, enfrentando mazmorras, resolviendo acertijos y explorando vastos paisajes llenos de magia y misterio.",
    7: "Minecraft es un juego de mundo abierto donde los jugadores pueden explorar, construir y sobrevivir en un vasto paisaje generado proceduralmente. Desde construir estructuras simples hasta complejas ciudades, y enfrentarse a peligros como monstruos y explorar cuevas llenas de recursos, Minecraft ofrece una experiencia de juego creativa y única.",
    8: "Fortnite es un popular juego de batalla real donde hasta 100 jugadores compiten para ser el último en pie. Los jugadores pueden construir estructuras defensivas, recolectar recursos y enfrentarse en intensos combates, todo mientras exploran un mundo colorido y en constante evolución.",
    9: "Tomb Raider es una serie de juegos de acción y aventuras que sigue las hazañas de Lara Croft, una arqueóloga y aventurera intrépida. Los juegos combinan exploración de ruinas antiguas, resolución de acertijos, combates emocionantes y narrativas intrigantes, llevando a los jugadores a través de emocionantes aventuras en todo el mundo.",
}

SLIDER = [
    {
        "title": TITLE[1],
        "content": CONTENT[1],
        "image_url": static("assets/img/slider/slide-1.jpg"),
    },
    {
        "title": TITLE[2],
        "content": CONTENT[2],
        "image_url": static("assets/img/slider/slide-2.jpg"),
    },
    {
        "title": TITLE[3],
        "content": CONTENT[3],
        "image_url": static("assets/img/slider/slide-3.jpg"),
    },
    {
        "title": TITLE[4],
        "content": CONTENT[4],
        "image_url": static("assets/img/slider/slide-4.jpg"),
    },
    {
        "title": TITLE[5],
        "content": CONTENT[5],
        "image_url": static("assets/img/slider/slide-5.jpg"),
    },
    {
        "title": TITLE[6],
        "content": CONTENT[6],
        "image_url": static("assets/img/slider/slide-6.jpg"),
    },
    {
        "title": TITLE[7],
        "content": CONTENT[7],
        "image_url": static("assets/img/slider/slide-7.jpg"),
    },
    {
        "title": TITLE[8],
        "content": CONTENT[8],
        "image_url": static("assets/img/slider/slide-8.jpg"),
    },
    {
        "title": TITLE[9],
        "content": CONTENT[9],
        "image_url": static("assets/img/slider/slide-9.jpg"),
    },
]


def random_slider():
    return random.sample(SLIDER, 5)
