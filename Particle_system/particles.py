import pygame as pg
from random import *

#particle class
class particle:
    def __init__(self, pos, velocity, size, sizeDA, color):
        self.pos = pos
        self.force = [0, 0]
        self.velocity = velocity

        self.size = size
        self.color = color

        self.sizeDA = sizeDA
        self.life_time = self.size 

    def update(self):
        self.velocity[0] += self.force[0]
        self.velocity[1] += self.force[1]
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        if(self.life_time >= 0):
            self.life_time -= self.sizeDA
            self.size = self.life_time

    def is_dead(self):
        return self.life_time <= 3

    def apply_force(self, force):
        self.force = force

    def draw(self, window):
        pg.draw.circle(window, self.color, self.pos, self.size)

#emitter class
class particle_emitter:
    def __init__(self, pos):
        self.pos = pos
        self.force = [0, 0]
        self.velocity = [0, 0]

        self.particles = []

    #emitter
    def emit(self, amount, velocity, size, sizeDA, color):
        for i in range(amount):
            self.particles.append(particle(self.pos.copy(), velocity, size, sizeDA, color))

    def update(self):
        self.velocity[0] += self.force[0]
        self.velocity[1] += self.force[1]
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

        for particle in self.particles:
            particle.update()
            if particle.is_dead():
                self.particles.remove(particle)

    def apply_force(self, force):
        self.force = force
    
    def draw(self, window):
        for particle in self.particles:
            particle.draw(window)

    #particles
    def Papply_force(self, force):
        for particle in self.particles:
            particle.apply_force(force)

    def Pcollide(self, rects, bounciness = 0):
        for particle in self.particles:
            p_rect = pg.Rect(particle.pos[0], particle.pos[1], particle.size, particle.size)

            for rect in rects:
                if p_rect.colliderect(rect):
                    particle.velocity[0] *= -bounciness
                    particle.velocity[1] *= -bounciness