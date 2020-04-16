from pygame import event,display
from gravitation import *

gravitation=Gravitation(2e+30,2e+27,5.5e+26)

while True:
    screen.fill(color.BLACK)
    for event in pygame.event.get():
        Quit.exit(event)
    definition.star(screen,local.star1,local.star2,local.star3)
    gravitation.local_influence()
    gravitation.speed_influence()
    pygame.display.update()
    clock.tick(60)