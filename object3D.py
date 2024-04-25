import pygame as pg
from matrixFunctions import *

class object3D():
    def __init__(self,render):
        self.render = render
        #BOX VERTEX
        # self.vertexes = np.array([(0,0,0,1),(0,1,0,1),(1,1,0,1),(1,0,0,1),
        #                          (0,0,1,1),(0,1,1,1),(1,1,1,1),(1,0,1,1)
        #                        ])
        #BOX FACES
        # self.faces = np.array([(0,1,2,3),(4,5,6,7),(0,4,5,1),(2,3,7,6),(1,2,6,5),(0,3,7,4)])
        #house VERTEXES
        self.vertexes = np.array([(0,0,0,1),(0,1,0,1),(1,1,0,1),(1,0,0,1),
                                  (0,0,1,1),(0,1,1,1),(1,1,1,1),(1,0,1,1), 
                                  (1,1.5,0.5,1),(0,1.5,0.5,1)
                                ])
        #HOUSE FACES
        self.faces = np.array([(0,1,2,3),(4,5,6,7),(0,4,5,1),(2,3,7,6),(1,2,6,5),(0,3,7,4),(9,8,6,5),(9,8,2,1)])
        
    def draw(self):
        self.screenProjection()
        self.movement()
        
    def movement(self):
        self.rotateY(pg.time.get_ticks() % 0.005)
        
    def screenProjection(self):
        vertexes = self.vertexes @ self.render.camera.cameraMatrix()
        vertexes = vertexes @ self.render.projection.projectionMatrix
        vertexes /= vertexes[:, -1].reshape(-1, 1)
        vertexes[(vertexes > 2) | (vertexes < -2)] = 0
        vertexes = vertexes @ self.render.projection.toScreenMatrix
        vertexes = vertexes[:, :2]
        
        for face in self.faces:
            polygon = vertexes[face]
            if not np.any((polygon == self.render.h_width) | (polygon == self.render.h_height)):
                pg.draw.polygon(self.render.screen, pg.Color('orange'), polygon, 3)
                
        for vertex in vertexes:
            if not np.any((vertex == self.render.h_width) | (vertex == self.render.h_height)):
                pg.draw.circle(self.render.screen, pg.Color('white'), vertex, 6)
        
    def translate(self, pos):
        self.vertexes = self.vertexes @ translate(pos)

    def scale(self, scale_to):
        self.vertexes = self.vertexes @ scale(scale_to)

    def rotateX(self, angle):
        self.vertexes = self.vertexes @ rotateX(angle)

    def rotateY(self, angle):
        self.vertexes = self.vertexes @ rotateY(angle)

    def rotateZ(self, angle):
        self.vertexes = self.vertexes @ rotateZ(angle)