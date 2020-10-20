from datetime import date
from habitats.wetlands import Wetlands
from habitats import wetlands
from habitats.snakepit import SnakePit
from habitats.pettingzoo import PettingZoo
from slithering.models import Lizard, Snake, Leech, Worm, Cobra
from swimming.models import Clownfish, Swordfish, Koi, Eel, Whale
from walking.models import Flamingo, Monkey, Tiger, Chimp, Panda



Mister = Flamingo("Mister", "Pink", "Morning", "Grass")
Kyle = Monkey("Kyle", "Big", "Evening", "Bugs")
Flamey = Tiger("Flamey", "Striped", "Night", "Rabbit")
Tollman = Chimp("Tollman", "Small", "Midday", "Bugs")
Jerry = Panda("Jerry", "Red", "Morning", "Bamboo")

Jack = Clownfish("Jack", "Clown", "Morning", "Alge")
Lenny = Swordfish("Lenny", "Swordfish", "Evening", "Mino")
Joey = Koi("Joey", "Japanese", "Night", "Fish food")
Super = Eel("Super", "Eletric", "Midday", "???")
Moe = Whale("Moe", "Orca", "Morning", "Small Fish")

Tony = Lizard("Tony", "Dragon", "Morning", "Flies")
Jason = Snake("Jason", "Garden", "Evening", "Dirt")
Coleman = Leech("Coleman", "Leech", "Night", "blood")
Lorrie = Worm("Lorrie", "Earthworm", "Midday", "Dirt")
King = Cobra("King", "King Cobra", "Morning", "Bugs")

print(f'{Mister.name} the {Mister.species} is available to pet during the {Mister.shift} shift.') 
Mister.feed()
print(Mister)
Tollman.feed()
Tony.feed()

varmint_village = PettingZoo("Varmint Village")

varmint_village.animals.append(Mister)
varmint_village.animals.append(Kyle)
varmint_village.animals.append(Flamey)
varmint_village.animals.append(Tollman)
varmint_village.animals.append(Jerry)

print(varmint_village.animals)

for animal in varmint_village.animals:
    print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

snake_pit = SnakePit("Snake Pit")

snake_pit.animals.append(Tony)
snake_pit.animals.append(Jason)
snake_pit.animals.append(Coleman)
snake_pit.animals.append(Lorrie)
snake_pit.animals.append(King)

print(snake_pit.animals)

for animal in snake_pit.animals:
    print(f'You can find {animal.name} the {animal.species} in the {snake_pit.attraction_name}')

wetlands = Wetlands("Wetlands")

wetlands.animals.append(Jack)
wetlands.animals.append(Lenny)
wetlands.animals.append(Joey)
wetlands.animals.append(Super)
wetlands.animals.append(Moe)

print(snake_pit.animals)

for animal in wetlands.animals:
    print(f'You can find {animal.name} the {animal.species} in the {wetlands.attraction_name}')