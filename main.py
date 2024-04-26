from object3D import *
from cam import *
from project import *
import pygame as pg

class GraphicsRender():
    def __init__(self):
        pg.init()
        infoObject = pg.display.Info()
        self.res = self.width, self.height = infoObject.current_w,infoObject.current_h
        self.h_width, self.h_height = self.width//2, self.height//2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self.createObjects()
        
    def createObjects(self):
        self.camera = Camera(self, [-5,5,-50])
        self.object = self.getObjFile('C:\\Users\\Owner\\3dEngineProject\\3D-Engine\\tank.obj')
        self.projection = Projection(self)
        
        
        '''
        self.camera = Camera(self, [0.5,1,-4])
        self.object = object3D(self)
        self.projection = Projection(self)
        self.object.translate([0.2,0.4,0.2])
        self.axes = Axes(self)
        self.axes.translate([0.7,0.9,0.7])
        self.worldAxes = Axes(self)
        self.worldAxes.movementFlag = False
        self.worldAxes.scale(2.5)
        self.worldAxes.translate([0.0001,0.0001,0.0001])
        '''
        
    def getObjFile(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return object3D(self, vertex, faces)
        
    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
        #self.worldAxes.draw()
        #self.axes.draw()
        self.object.draw()
        
    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            key = pg.key.get_pressed()
            if key[pg.K_ESCAPE]:
                pg.quit()
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.fps)
            
if __name__ == '__main__':
    app = GraphicsRender()
    app.run()