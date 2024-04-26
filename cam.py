import pygame as pg
from matrixFunctions import *

class Camera:
    def __init__(self, render, position):
        self.render = render
        self.position = np.array([*position, 1.0])
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])
        self.hFov = math.pi / 3
        self.vFov = self.hFov * (render.height / render.width)
        self.nearPlane = 0.1
        self.farPlane = 100
        self.movingSpeed = 0.2
        self.rotationSpeed = 0.005

        self.anglePitch = 0
        self.angleYaw = 0
        self.angleRoll = 0
        
        self.mouse = (0,0)
        
    def control(self):
        self.mouse = pg.mouse.get_rel()
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.position -= self.right * self.movingSpeed
        if key[pg.K_d]:
            self.position += self.right * self.movingSpeed
        if key[pg.K_w]:
            self.position += self.forward * self.movingSpeed
        if key[pg.K_s]:
            self.position -= self.forward * self.movingSpeed
        if key[pg.K_q]:
            self.position += self.up * self.movingSpeed
        if key[pg.K_e]:
            self.position -= self.up * self.movingSpeed

        if(pg.mouse.get_pressed()[0] == True):
            if (self.mouse[0] < 0):
                self.cameraYaw(-self.rotationSpeed*-self.mouse[0])
            if (self.mouse[0] > 0):
                self.cameraYaw(self.rotationSpeed*self.mouse[0])
            if (self.mouse[1] < 0):
                self.cameraPitch(-self.rotationSpeed*-self.mouse[1])
            if (self.mouse[1] > 0):
                self.cameraPitch(self.rotationSpeed*self.mouse[1])
        else:
            if key[pg.K_LEFT]:
                self.cameraYaw(-self.rotationSpeed*2)
            if key[pg.K_RIGHT]:
                self.cameraYaw(self.rotationSpeed*2)
            if key[pg.K_UP]:
                self.cameraPitch(-self.rotationSpeed*2)
            if key[pg.K_DOWN]:
                self.cameraPitch(self.rotationSpeed*2)
            
    def axiiIdentity(self):
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])
            
    def cameraYaw(self, angle):
        self.angleYaw += angle

    def cameraPitch(self, angle):
        self.anglePitch += angle
        
    def cameraUpdateAxii(self):
        #rotate = rotateY(self.angleYaw) @ rotateY(self.anglePitch)
        rotate = rotateX(self.anglePitch) @ rotateY(self.angleYaw)  # this concatenation gives right visual
        self.axiiIdentity()
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate
        
    def translateMatrix(self):
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])

    def rotateMatrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])
        
    def cameraMatrix(self):
        self.cameraUpdateAxii()
        return self.translateMatrix() @ self.rotateMatrix()