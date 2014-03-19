#Shubham Srivastava
from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Fog
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import Vec3,Vec4,BitMask32
from pandac.PandaModules import Point3
import random, sys, os, math


nob=0
points=10
noba=0

class MyApp(ShowBase):
    def addTitle(self,text):
        return OnscreenText(text=text, style=1, fg=(1,1,1,1), pos=(0,-0.95), align=TextNode.ACenter, scale = .07)

    def makeStatusLabel(self, i):
        return OnscreenText(style=1, fg=(1,1,0,1), pos=(-1.3 + (i*0.8), -0.95 ), align=TextNode.ALeft, scale = .05, mayChange = 1)

    def __init__(self):
        ShowBase.__init__(self)
        self.keyMap = {"left":0, "right":0, "forward":0, "cam-left":0, "cam-right":0}
        base.win.setClearColor(Vec4(0,0,0,1))
        self.texto1 = OnscreenText(text="Collect 8 balls and meet Sonic behind the building", style=1, fg=(1,1,1,1), pos=(0,-0.1), align=TextNode.ACenter, scale = .07)
        self.texto2 = OnscreenText(text="Eat bananas for energy and avoid green stones", style=1, fg=(1,1,1,1), pos=(0,-0.2), align=TextNode.ACenter, scale = .07)
        self.texto3 = OnscreenText(text="Arrow keys move the player", style=1, fg=(1,1,1,1), pos=(0,-0.3), align=TextNode.ACenter, scale = .07)
        self.texto4 = OnscreenText(text="a and s help you view the scene", style=1, fg=(1,1,1,1), pos=(0,-0.4), align=TextNode.ACenter, scale = .07)

        self.noOfbanana = self.makeStatusLabel(0)
        self.noOfBalls = self.makeStatusLabel(1)
        self.points = self.makeStatusLabel(2)
            
        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, -3)
        self.environ1 = self.loader.loadModel("models/env")
        self.environ1.reparentTo(self.render)
        self.environ1.setScale(50,50,30)
        self.environ1.setPos(0, -170, -3)
        #self.environ1.setHpr(90,0,0)

        self.house1 = self.loader.loadModel("models/houses/church")
        self.house1.reparentTo(self.render)
        self.house1.setScale(0.30)
        self.house1.setPos(25, -150, -3)
        self.house1.setHpr(90,0,0)
        self.house2 = self.loader.loadModel("models/houses/building")
        self.house2.reparentTo(self.render)
        self.house2.setScale(0.30)
        self.house2.setPos(18, -200, -3)
        self.house2.setHpr(180,0,0)
        self.house3 = self.loader.loadModel("models/houses/farmhouse")
        self.house3.reparentTo(self.render)
        self.house3.setScale(0.30)
        self.house3.setPos(20, -130, -3)
        self.house3.setHpr(90,0,0)
        self.house4 = self.loader.loadModel("models/houses/dojo")
        self.house4.reparentTo(self.render)
        self.house4.setScale(0.05)
        self.house4.setPos(5, -220, -3)
        self.house5 = self.loader.loadModel("models/houses/beachhouse2")
        self.house5.reparentTo(self.render)
        self.house5.setScale(0.30)
        self.house5.setPos(-10, -180, -3)
        self.house5.setHpr(-90,0,0)

        self.house6 = self.loader.loadModel("models/houses/gazebo")
        self.house6.reparentTo(self.render)
        self.house6.setScale(0.50)
        self.house6.setPos(-10, -200, -3)
        self.house7 = self.loader.loadModel("models/houses/building")
        self.house7.reparentTo(self.render)
        self.house7.setScale(0.30)
        self.house7.setPos(-10, -120, -3)



        self.tunnel = [None for i in range(10)]
    
        for x in range(10):
          #Load a copy of the tunnel
          self.tunnel[x] = loader.loadModel('models/tunnel')
          self.tunnel[x].setHpr(0,90,0)
          self.tunnel[x].setScale(0.5)
          self.tunnel[x].setPos(0,177.5 + 25*x, 0)
          self.tunnel[x].reparentTo(self.render)
##        ###World specific-code
##    
##        #Create an instance of fog called 'distanceFog'.
##        #'distanceFog' is just a name for our fog, not a specific type of fog.
##        self.fog = Fog('distanceFog')
##        #Set the initial color of our fog to black.
##        self.fog.setColor(0, 0, 0)
##        #Set the density/falloff of the fog.  The range is 0-1.
##        #The higher the numer, the "bigger" the fog effect.
##        self.fog.setExpDensity(.08)
##        #We will set fog on render which means that everything in our scene will
##        #be affected by fog. Alternatively, you could only set fog on a specific
##        #object/node and only it and the nodes below it would be affected by
##        #the fog.
##        render.setFog(self.fog)
        self.banana = [None for i in range(20)]
        self.flag = [0 for i in range(20)]
        self.fla = [0 for i in range(5)]
        self.fl = [0 for i in range(8)]
        for x in range(10):
          #Load a copy of the tunnel
          self.banana[x] = loader.loadModel('models/banana/banana')
          #self.banana[x].setHpr(0,90,0)
          self.banana[x].setScale(0.7)
          if(x%2==0):
              self.banana[x].setPos(-1,180 + 25*x, -2)
          else:
              self.banana[x].setPos(1,177.5 + 25*x, -2)
          self.banana[x].reparentTo(self.render)

        self.banana[11] = self.loader.loadModel("models/banana/banana")
        self.banana[11].reparentTo(self.render)
        self.banana[11].setPos(12, 8, -2)
        self.banana[12] = self.loader.loadModel("models/banana/banana")
        self.banana[12].reparentTo(self.render)
        self.banana[12].setPos(0, 120, -2)
        self.banana[13] = self.loader.loadModel("models/banana/banana")
        self.banana[13].reparentTo(self.render)
        self.banana[13].setPos(12, 100, -2)
        self.banana[14] = self.loader.loadModel("models/banana/banana")
        self.banana[14].reparentTo(self.render)
        self.banana[14].setPos(22, 80, -2)
        self.banana[15] = self.loader.loadModel("models/banana/banana")
        self.banana[15].reparentTo(self.render)
        self.banana[15].setPos(12, 50, -2)
        self.banana[16] = self.loader.loadModel("models/banana/banana")
        self.banana[16].reparentTo(self.render)
        self.banana[16].setPos(15, 30, -2)
        self.banana[17] = self.loader.loadModel("models/banana/banana")
        self.banana[17].reparentTo(self.render)
        self.banana[17].setPos(-10, 8, -2)
        self.banana[18] = self.loader.loadModel("models/banana/banana")
        self.banana[18].reparentTo(self.render)
        self.banana[18].setPos(-20, -30, -2)
        self.banana[19] = self.loader.loadModel("models/banana/banana")
        self.banana[19].reparentTo(self.render)
        self.banana[19].setPos(-50, -50, -2)
        
        self.candy = self.loader.loadModel("models/candy/candycane2")
        self.candy.reparentTo(self.render)
        self.candy.setScale(0.001)
        self.candy.setPos(-6, 10, -2)

        self.fire = self.loader.loadModel("models/candy/candycane2")
        self.fire.reparentTo(self.render)
        self.fire.setScale(0.001)
        self.fire.setPos(0, 2, -2)

        self.ball = [None for i in range(8)]
        self.ball[0] = self.loader.loadModel("models/ball/soccerball")
        self.ball[0].reparentTo(self.render)
        self.ball[0].setPos(-6, 6, -2)
        self.ball[0].setScale(0.7)
        self.ball[1] = self.loader.loadModel("models/ball/soccerball")
        self.ball[1].reparentTo(self.render)
        self.ball[1].setPos(-6, -6, -2)
        self.ball[1].setScale(0.7)
        self.ball[2] = self.loader.loadModel("models/ball/soccerball")
        self.ball[2].reparentTo(self.render)
        self.ball[2].setPos(-15, 10, -2)
        self.ball[2].setScale(0.7)
        self.ball[3] = self.loader.loadModel("models/ball/soccerball")
        self.ball[3].reparentTo(self.render)
        self.ball[3].setPos(-19, 0, -2)
        self.ball[3].setScale(0.7)
        self.ball[4] = self.loader.loadModel("models/ball/soccerball")
        self.ball[4].reparentTo(self.render)
        self.ball[4].setPos(-6, -20, -2)
        self.ball[4].setScale(0.7)
        self.ball[5] = self.loader.loadModel("models/ball/soccerball")
        self.ball[5].reparentTo(self.render)
        self.ball[5].setPos(6, 6, -2)
        self.ball[5].setScale(0.7)
        self.ball[6] = self.loader.loadModel("models/ball/soccerball")
        self.ball[6].reparentTo(self.render)
        self.ball[6].setPos(19, 10, -2)
        self.ball[6].setScale(0.7)
        self.ball[7] = self.loader.loadModel("models/ball/soccerball")
        self.ball[7].reparentTo(self.render)
        self.ball[7].setPos(-15, 12, -2)
        self.ball[7].setScale(0.7)

        self.rock = [None for i in range(8)]
        self.rock[0] = self.loader.loadModel("models/greencrystal")
        self.rock[0].reparentTo(self.render)
        self.rock[0].setPos(0,306, -4)
        self.rock[0].setScale(0.007)
        self.rock[0].setHpr(90,0,0)
        self.rock[1] = self.loader.loadModel("models/greencrystal")
        self.rock[1].reparentTo(self.render)
        self.rock[1].setPos(-2, 150, -3)
        self.rock[1].setScale(0.007)
        self.rock[1].setHpr(90,0,0)
        self.rock[2] = self.loader.loadModel("models/greencrystal")
        self.rock[2].reparentTo(self.render)
        self.rock[2].setPos(-10, 10, -3)
        self.rock[2].setScale(0.007)
        self.rock[2].setHpr(90,0,0)
        self.rock[3] = self.loader.loadModel("models/greencrystal")
        self.rock[3].reparentTo(self.render)
        self.rock[3].setPos(5, 0, -3)
        self.rock[3].setScale(0.007)
        self.rock[3].setHpr(90,0,0)
        self.rock[4] = self.loader.loadModel("models/greencrystal")
        self.rock[4].reparentTo(self.render)
        self.rock[4].setPos(-2, -120, -3)
        self.rock[4].setScale(0.007)
        self.rock[4].setHpr(90,0,0)

        self.tire = self.loader.loadModel("models/tire/tire")
        self.tire.reparentTo(self.render)
        self.tire.setScale(0.25, 0.25, 0.25)
        self.tire.setPos(-20, 3, -2)
        
        self.bunny1 = self.loader.loadModel("models/bunny")
        self.bunny1.reparentTo(self.render)
        self.bunny1.setScale(0.2)
        self.bunny1.setPos(15, -160, -3)
        self.bunny1.setHpr(-60,0,0)
        self.bunny2 = self.loader.loadModel("models/bunny")
        self.bunny2.reparentTo(self.render)
        self.bunny2.setScale(0.2)
        self.bunny2.setPos(15, -161, -3)
        self.bunny2.setHpr(-145,0,0)
        # Add the spinCameraTask procedure to the task manager.
        #self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
 
        # Load and transform the panda actor.
        self.pandaActor = Actor("models/panda-model",
                                {"walk": "models/panda-walk4"})
        self.pandaActor.setScale(0.005, 0.005, 0.005)
        #self.pandaActor.setPos(0,100,-3)
        self.pandaActor.reparentTo(self.render)
        # Loop its animation.
        self.pandaActor.loop("walk")
 
        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        pandaPosInterval1 = self.pandaActor.posInterval(20,
                                                        Point3(0, -110, -3),
                                                        startPos=Point3(0, -90, -3))
        pandaPosInterval2 = self.pandaActor.posInterval(20,
                                                        Point3(0, -90, -3),
                                                        startPos=Point3(0, -110, -3))
        pandaHprInterval1 = self.pandaActor.hprInterval(3,
                                                        Point3(180, 0, 0),
                                                        startHpr=Point3(0, 0, 0))
        pandaHprInterval2 = self.pandaActor.hprInterval(3,
                                                        Point3(0, 0, 0),
                                                        startHpr=Point3(180, 0, 0))
 
        # Create and play the sequence that coordinates the intervals.
        self.pandaPace = Sequence(pandaPosInterval1,
                                  pandaHprInterval1,
                                  pandaPosInterval2,
                                  pandaHprInterval2,
                                  name="pandaPace")
        self.pandaPace.loop()
        self.eve = Actor("models/eve",
                                {"walk": "models/eve-walk"})
        self.eve.setScale(0.5, 0.5, 0.5)
        self.eve.setPos(-1,-140,-3)
        self.eve.reparentTo(self.render)
        # Loop its animation.
        self.eve.loop("walk")
 
        # Create the four lerp intervals needed for the panda to
        # walk back and forth.
        evePosInterval1 = self.eve.posInterval(20,
                                                        Point3(-1, -160, -3),
                                                        startPos=Point3(-1, -140, -3))
        evePosInterval2 = self.eve.posInterval(20,
                                                        Point3(-1, -140, -3),
                                                        startPos=Point3(-1, -160, -3))
        eveHprInterval1 = self.eve.hprInterval(3,
                                                        Point3(180, 0, 0),
                                                        startHpr=Point3(0, 0, 0))
        eveHprInterval2 = self.eve.hprInterval(3,
                                                        Point3(0, 0, 0),
                                                        startHpr=Point3(180, 0, 0))
 
        # Create and play the sequence that coordinates the intervals.
        self.evePace = Sequence(evePosInterval1,eveHprInterval1,evePosInterval2,eveHprInterval2,name="evePace")
        self.evePace.loop()
        self.ralph = Actor("models/r/ralph",
                                {"run":"models/ralph-run",
                                 "walk": "models/ralph-walk"})
        self.ralph.setScale(0.5, 0.5, 0.5)
        self.ralph.setPos(0, 420, -3)
        self.ralph.reparentTo(self.render)
        self.boy = Actor("models/soni/sonic",
                                {"anim":"models/soni/sonic-win"})
        self.boy.setScale(0.05, 0.05, 0.05)
        self.boy.setPos(33, -203, -2)
        self.boy.setHpr(-90,0,0)
        self.boy.reparentTo(self.render)
        self.boy.loop("anim")

        self.boy1 = Actor("models/boy/boymodel",
                                {"anim":"models/boy/boyanimation"})
        self.boy1.setScale(0.007)
        self.boy1.setPos(-5, -200, -2)
        self.boy1.setHpr(180,0,0)
        self.boy1.reparentTo(self.render)
        self.boy1.loop("anim")

        self.character=Actor()
        self.character.loadModel('models/dancer')
        self.character.setPos(3,150,-3)
        self.character.reparentTo(render)
        self.character.setHpr(180,0,0)
        self.character.setScale(0.6)
        self.character.loadAnims({'win':'models/dancer'})
        self.character.loop('win')

        self.character1=Actor()
        self.character1.loadModel('models/gorillawalking')
        self.character1.setPos(2,-13,-3)
        self.character1.setScale(0.6)
        self.character1.reparentTo(render)
        self.character1.setHpr(180,0,0)
        self.character1.loadAnims({'win':'models/gorillawalking'})
        self.character1.loop('win')
        
        self.accept("escape", sys.exit)
        self.accept("arrow_left", self.setKey, ["left",1])
        self.accept("arrow_right", self.setKey, ["right",1])
        self.accept("arrow_up", self.setKey, ["forward",1])
        self.accept("a", self.setKey, ["cam-left",1])
        self.accept("s", self.setKey, ["cam-right",1])
        self.accept("arrow_left-up", self.setKey, ["left",0])
        self.accept("arrow_right-up", self.setKey, ["right",0])
        self.accept("arrow_up-up", self.setKey, ["forward",0])
        self.accept("a-up", self.setKey, ["cam-left",0])
        self.accept("s-up", self.setKey, ["cam-right",0])

        taskMgr.add(self.move,"moveTask")
        taskMgr.add(self.find,"fisdTask")
        taskMgr.add(self.potask,"potaskTask")
        # Game state variables
        self.isMoving = False

        # Set up the camera
        
        base.disableMouse()
        base.camera.setPos(self.ralph.getX(),self.ralph.getY()+10,-1)
        #print self.ralph.getX(), self.ralph.getY()

        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
        self.updateStatusLabel()
        
    def potask(self,task):
        global points
        if(self.ralph.getY()<410):
            self.texto1.destroy()
            self.texto2.destroy()
            self.texto3.destroy()
            self.texto4.destroy()
        if(points<0):
            OnscreenText(text="Game Over", style=1, fg=(1,1,1,1), pos=(0,0), align=TextNode.ACenter, scale = 0.4)
            OnscreenText(text="You are out of energy", style=1, fg=(1,1,1,1), pos=(0,-0.20), align=TextNode.ACenter, scale = 0.05)
        return Task.cont
        
        
    def find(self,task):
        global nob, points, noba
        #print self.ralph.getX(),self.ralph.getY()
        if ((self.ralph.getX()>=-3 and self.ralph.getX()<=-1) and (self.ralph.getY()>=145 and self.ralph.getY()<=165) and self.fla[1] == 0):
            self.rock[1].removeNode()
            points= points - 20
            self.fla[1]=1
        elif((self.ralph.getX()>=-11 and self.ralph.getX()<=-9) and (self.ralph.getY()>=9 and self.ralph.getY()<=11) and self.fla[2] == 0):
            self.rock[2].removeNode()
            points= points - 20
            self.fla[2]=1
        elif((self.ralph.getX()>=4 and self.ralph.getX()<=6) and (self.ralph.getY()>=-1 and self.ralph.getY()<=1) and self.fla[3] == 0):
            self.rock[3].removeNode()
            points= points - 20
            self.fla[3]=1
        elif((self.ralph.getX()>=-1 and self.ralph.getX()<=1) and (self.ralph.getY()>=305 and self.ralph.getY()<=307) and self.fla[0] == 0):
            self.rock[0].removeNode()
            points= points - 20
            self.fla[0]=1
        elif((self.ralph.getX()>=-3 and self.ralph.getX()<=-1) and (self.ralph.getY()>=-121 and self.ralph.getY()<=-119) and self.fla[4] == 0):
            self.rock[4].removeNode()
            points= points - 20
            self.fla[4]=1

            
        if ((self.ralph.getX()>=-7.5 and self.ralph.getX()<=-6.5) and (self.ralph.getY()>=-7.5 and self.ralph.getY()<=-6.5) and self.fl[1] == 0):
            self.ball[1].removeNode()
            noba= noba + 1
            self.fl[1]=1
        elif((self.ralph.getX()>=-15.5 and self.ralph.getX()<=-14.5) and (self.ralph.getY()>=9.5 and self.ralph.getY()<=10.5) and self.fl[2] == 0):
            self.ball[2].removeNode()
            noba= noba + 1
            self.fl[2]=1
        elif((self.ralph.getX()>=-19.5 and self.ralph.getX()<=-18.5) and (self.ralph.getY()>=-0.5 and self.ralph.getY()<=0.5) and self.fl[3] == 0):
            self.ball[3].removeNode()
            noba= noba + 1
            self.fl[3]=1
        elif((self.ralph.getX()>=-6.5 and self.ralph.getX()<=-5.5) and (self.ralph.getY()>=5.5 and self.ralph.getY()<=6.5) and self.fl[0] == 0):
            self.ball[0].removeNode()
            noba= noba + 1
            self.fl[0]=1
        elif((self.ralph.getX()>=-6.5 and self.ralph.getX()<=-5.5) and (self.ralph.getY()>=-20.5 and self.ralph.getY()<=-19.5) and self.fl[4] == 0):
            self.ball[4].removeNode()
            noba= noba + 1
            self.fl[4]=1
        elif((self.ralph.getX()>=5.5 and self.ralph.getX()<=6.5) and (self.ralph.getY()>=5.5 and self.ralph.getY()<=6.5) and self.fl[5] == 0):
            self.ball[5].removeNode()
            noba= noba + 1
            self.fl[5]=1
        elif((self.ralph.getX()>=18.5 and self.ralph.getX()<=19.5) and (self.ralph.getY()>=9.5 and self.ralph.getY()<=10.5) and self.fl[6] == 0):
            self.ball[6].removeNode()
            noba= noba + 1
            self.fl[6]=1
        elif((self.ralph.getX()>=-15.5 and self.ralph.getX()<=-14.5) and (self.ralph.getY()>=11.5 and self.ralph.getY()<=12.5) and self.fl[7] == 0):
            self.ball[7].removeNode()
            noba= noba + 1
            self.fl[7]=1
        

        if ((self.ralph.getX()>=11.5 and self.ralph.getX()<=12.5) and (self.ralph.getY()>=7.5 and self.ralph.getY()<=8.5) and self.flag[11]==0):
            self.banana[11].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[11]=1
        elif ((self.ralph.getX()>=0.5 and self.ralph.getX()<=1.5) and (self.ralph.getY()>=404.5 and self.ralph.getY()<=405.5) and self.flag[9]==0):
            self.banana[9].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[9]=1
        elif ((self.ralph.getX()>=0.5 and self.ralph.getX()<=1.5) and (self.ralph.getY()>=354.5 and self.ralph.getY()<=355.5) and self.flag[7]==0):
            self.banana[7].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[7]=1
        elif ((self.ralph.getX()>=0.5 and self.ralph.getX()<=1.5) and (self.ralph.getY()>=304.5 and self.ralph.getY()<=305.5) and self.flag[5]==0):
            self.banana[5].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[5]=1
        elif ((self.ralph.getX()>=0.5 and self.ralph.getX()<=1.5) and (self.ralph.getY()>=254.5 and self.ralph.getY()<=255.5) and self.flag[3]==0):
            self.banana[3].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[3]=1
        elif ((self.ralph.getX()>=0.5 and self.ralph.getX()<=1.5) and (self.ralph.getY()>=204.5 and self.ralph.getY()<=205.5) and self.flag[1]==0):
            self.banana[1].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[1]=1
        elif ((self.ralph.getX()>=-1.5 and self.ralph.getX()<=-0.5) and (self.ralph.getY()>=379.5 and self.ralph.getY()<=380.5) and self.flag[8]==0):
            self.banana[8].removeNode()
            #print 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
            nob= nob + 1
            points= points + 10
            self.flag[8]=1
        elif ((self.ralph.getX()>=-1.5 and self.ralph.getX()<=-0.5) and (self.ralph.getY()>=329.5 and self.ralph.getY()<=330.5) and self.flag[6]==0):
            self.banana[6].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[6]=1
        elif ((self.ralph.getX()>=-1.5 and self.ralph.getX()<=-0.5) and (self.ralph.getY()>=279.5 and self.ralph.getY()<=280.5) and self.flag[4]==0):
            self.banana[4].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[4]=1
        elif ((self.ralph.getX()>=-1.5 and self.ralph.getX()<=-0.5) and (self.ralph.getY()>=229.5 and self.ralph.getY()<=230.5) and self.flag[2]==0):
            self.banana[2].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[2]=1
        elif ((self.ralph.getX()>=-1.5 and self.ralph.getX()<=-0.5) and (self.ralph.getY()>=179.5 and self.ralph.getY()<=180.5) and self.flag[0]==0):
            self.banana[0].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[0]=1
        elif ((self.ralph.getX()>=-0.5 and self.ralph.getX()<=0.5) and (self.ralph.getY()>=119.5 and self.ralph.getY()<=120.5) and self.flag[12]==0):
            self.banana[12].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[12]=1
        elif ((self.ralph.getX()>=11.5 and self.ralph.getX()<=12.5) and (self.ralph.getY()>=99.5 and self.ralph.getY()<=100.5) and self.flag[13]==0):
            self.banana[13].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[13]=1
        elif ((self.ralph.getX()>=21.5 and self.ralph.getX()<=22.5) and (self.ralph.getY()>=79.5 and self.ralph.getY()<=80.5) and self.flag[14]==0):
            self.banana[14].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[14]=1
        elif ((self.ralph.getX()>=11.5 and self.ralph.getX()<=12.5) and (self.ralph.getY()>=49.5 and self.ralph.getY()<=50.5) and self.flag[15]==0):
            self.banana[15].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[15]=1
        elif ((self.ralph.getX()>=14.5 and self.ralph.getX()<=15.5) and (self.ralph.getY()>=29.5 and self.ralph.getY()<=30.5) and self.flag[16]==0):
            self.banana[16].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[16]=1
        elif ((self.ralph.getX()>=-10.5 and self.ralph.getX()<=-9.5) and (self.ralph.getY()>=7.5 and self.ralph.getY()<=8.5) and self.flag[17]==0):
            self.banana[17].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[17]=1
        elif ((self.ralph.getX()>=-20.5 and self.ralph.getX()<=-19.5) and (self.ralph.getY()>=-30.5 and self.ralph.getY()<=-29.5) and self.flag[18]==0):
            self.banana[18].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[18]=1
        elif ((self.ralph.getX()>=-50.5 and self.ralph.getX()<=-49.5) and (self.ralph.getY()>=-50.5 and self.ralph.getY()<=-49.5) and self.flag[19]==0):
            self.banana[19].removeNode()
            nob= nob + 1
            points= points + 10
            self.flag[19]=1
        
        if(self.ralph.getX()>30 and self.ralph.getY()<-200 and noba <8):
            self.boy.loop("anim")
            #self.ralph.removeNode()
            OnscreenText(text="Game Over", style=1, fg=(1,1,1,1), pos=(0,0), align=TextNode.ACenter, scale = 0.4)
            OnscreenText(text="Task not Completed", style=1, fg=(1,1,1,1), pos=(0,-0.20), align=TextNode.ACenter, scale = 0.05)
        elif(self.ralph.getX()>30 and self.ralph.getY()<-200 and noba ==8):
            #self.ralph.removeNode()
            OnscreenText(text="Game Over", style=1, fg=(1,1,1,1), pos=(0,0), align=TextNode.ACenter, scale = 0.4)
            OnscreenText(text="Cheers Task Completed", style=1, fg=(1,1,1,1), pos=(0,-0.20), align=TextNode.ACenter, scale = 0.05)
        self.updateStatusLabel()  
        return Task.cont
         
 
    

    #Records the state of the arrow keys
    def setKey(self, key, value):
        self.keyMap[key] = value
    

    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):
        
        if(self.ralph.getY()<160):
            
            
            # If the camera-left key is pressed, move camera left.
            # If the camera-right key is pressed, move camera right.
            base.camera.lookAt(self.ralph)
            if (self.keyMap["cam-left"]!=0):
                base.camera.setX(base.camera, -20 * globalClock.getDt())
            if (self.keyMap["cam-right"]!=0):
                base.camera.setX(base.camera, +20 * globalClock.getDt())

            # save ralph's initial position so that we can restore it,
            # in case he falls off the map or runs into something.

            startpos = self.ralph.getPos()

            # If a move-key is pressed, move ralph in the specified direction.

            if (self.keyMap["left"]!=0):
                self.ralph.setH(self.ralph.getH() + 300 * globalClock.getDt())
            if (self.keyMap["right"]!=0):
                self.ralph.setH(self.ralph.getH() - 300 * globalClock.getDt())
            if (self.keyMap["forward"]!=0):
                self.ralph.setY(self.ralph, -25 * globalClock.getDt())

            # If ralph is moving, loop the run animation.
            # If he is standing still, stop the animation.

            if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0):
                if self.isMoving is False:
                    self.ralph.loop("run")
                    self.isMoving = True
            else:
                if self.isMoving:
                    self.ralph.stop()
                    self.ralph.pose("walk",5)
                    self.isMoving = False
        else:
            # If the camera-left key is pressed, move camera left.
            # If the camera-right key is pressed, move camera right.
            base.camera.lookAt(self.ralph)
            startpos = self.ralph.getPos()

            # If a move-key is pressed, move ralph in the specified direction.

            if ((self.keyMap["left"]!=0) and self.ralph.getX()<2.5):
                self.ralph.setH(self.ralph.getH() + 200 * globalClock.getDt())
            if ((self.keyMap["right"]!=0) and self.ralph.getX()>-2.5):
                self.ralph.setH(self.ralph.getH() - 200 * globalClock.getDt())
            if ((self.keyMap["forward"]!=0) and self.ralph.getX()>-3 and self.ralph.getX()<3):
                self.ralph.setY(self.ralph, -25 * globalClock.getDt())
            elif (self.ralph.getX()<-3):
                self.ralph.setX(-2.9)
            elif  (self.ralph.getX()>3):
                self.ralph.setX(2.9)

            # If ralph is moving, loop the run animation.
            # If he is standing still, stop the animation.

            if (self.keyMap["forward"]!=0) or (self.keyMap["left"]!=0) or (self.keyMap["right"]!=0):
                if self.isMoving is False:
                    self.ralph.loop("run")
                    self.isMoving = True
            else:
                if self.isMoving:
                    self.ralph.stop()
                    self.ralph.pose("walk",5)
                    self.isMoving = False


        camvec = self.ralph.getPos() - base.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        if (camdist > 10.0):
            base.camera.setPos(base.camera.getPos() + camvec*(camdist-10))
            camdist = 10.0
        if (camdist < 5.0):
            base.camera.setPos(base.camera.getPos() - camvec*(5-camdist))
            camdist = 5.0

        return task.cont

    def updateStatusLabel( self ):
        global nob, points
        self.noOfbanana.setText("Bananas Taken: " + str(nob))
        self.points.setText("Energy Meter: " + str(points))
        self.noOfBalls.setText("Balls found: " + str(noba))
 
app = MyApp()
app.run()
