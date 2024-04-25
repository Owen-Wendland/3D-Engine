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
        self.camera = Camera(self, [0.5,1,-4])
        self.object = object3D(self)
        self.projection = Projection(self)
        self.object.translate([0.2,0.4,0.2])
        self.object.rotateY(-math.pi / 4)
        
    def draw(self):
        self.screen.fill(pg.Color('darkslategray'))
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