import pygame as pg
from Particle_system.particles import *

#initializing pygame
pg.init()

#settinng up the window
fps = 60
clock = pg.time.Clock()
window_size = (640, 640)
window = pg.display.set_mode(window_size)
pg.display.set_caption("Particles")

#emitter
mouse_pos = [pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]]
emitter = particle_emitter(mouse_pos)

#rectangles
collision_rects = [pg.Rect(300, 400, 100, 50), pg.Rect(350, 200, 100, 70), pg.Rect(100, 450, 150, 70)]

#game loop
running = True
while running:

    #emitting the particles
    if pg.mouse.get_pressed()[0]:
        emitter.emit(1, [randrange(-10, 10), randrange(-10, 10)], 12, 0.25, (255, 255, 255))

    #updating
    mouse_pos = [pg.mouse.get_pos()[0], pg.mouse.get_pos()[1]]
    emitter.pos = mouse_pos
    emitter.update()

    #applying gravity to the particles
    emitter.Papply_force([0, 0.2])

    #applying collision to the particles
    emitter.Pcollide(collision_rects, 0.7)

    #drawing
    emitter.draw(window)
    for col_rect in collision_rects:
        pg.draw.rect(window, (150, 100, 50), col_rect)

    #events
    for event in pg.event.get():

        #closing the window
        if event.type == pg.QUIT:
            running = False
            pg.quit()
        
    #updating the window
    clock.tick(fps)
    pg.display.update()
    window.fill((150, 150, 200))
