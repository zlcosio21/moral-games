import random

CITATIONS = [
    {
        "content": "El acero más fuerte se forja en el fuego más ardiente.",
        "author": "Dutch van der Linde",
    },
    {
        "content": "La vida es una lucha, y la única opción es seguir luchando.",
        "author": "Franklin Clinton",
    },
    {
        "content": "Lo único que importa es la misión. Nadie se queda atrás.",
        "author": "Capitán John Price",
    },
    {
        "content": "Debemos mirar hacia la oscuridad y asumir la responsabilidad. Esa es la única forma de salir de ella.",
        "author": "Adam Jensen",
    },
    {
        "content": "Todos tomamos decisiones, pero al final, nuestras decisiones nos definen.",
        "author": "Andrew Ryan",
    },
    {
        "content": "Sobreviví porque el fuego dentro de mí ardía más brillante que el fuego que me rodeaba..",
        "author": "Joshua Graham",
    },
    {
        "content": "La esperanza es lo que nos hace fuertes. Es por eso que estamos aquí.",
        "author": "Maestro Rahool",
    },
    {
        "content": "La guerra es cuando los jóvenes y estúpidos son engañados por los viejos y amargados para matarse unos a otros.",
        "author": "Niko Bellic",
    },
    {
        "content": "Nada es verdad, todo está permitido.",
        "author": "Ezio Auditore da Firenze",
    },
]


def random_citation():
    return random.choice(CITATIONS)
