class Pokemon:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

pikachu = Pokemon("Pikachu", "When several of these Pokémon gather, their electricity could build and cause lightning storms.")

pokedex = {
    "Pikachu": pikachu,
    }
