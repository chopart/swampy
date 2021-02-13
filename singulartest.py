#encoding: utf-8
from FractalWorld import *

world = FractalWorld(width=1000,height=700,delay=0)
t = Fractal(draw = True)

class Fractalprot(object):
    """base class for a fractal object, must contain all the relevant information for the fractal"""
    def __init__(self,startstate,rules,commands,length,depth):
        self.startstate = startstate
        self.rules = rules
        self.length = length
        self.depth = depth
        self.commands = commands

class Command(Fractalprot):
    """this object translates the fdl file into turtlelingau aka turtlewhispering"""
    def __init__(self,types,args):
        self.types = types
        self.args = args
    def whisper(self,t,Fractal): #teknisk set tager den en length fra Fractal objectet
        if self.types == "fd":           
            fd(t,Fractal.length)
        elif self.types == "lt":
            lt(t,float(self.args))
        elif self.types == "rt":
            rt(t,float(self.args))
        elif self.types == "scale":
            Fractal.length = Fractal.length * float(self.args)
        elif self.types == "bk":
            bk(t,Fractal.length)
        else:
            pass

class Rule(Fractalprot):
    """this object modifies the rules of the fractal"""
    def __init__(self,start,rules):
        self.start = start
        self.rules = rules

def flatten(liste): #testet og virker til at flatten en liste ud, beregnet til rules osv.
    liste2 = []
    for element in liste:
        if isinstance(element,list):
            liste2.extend(element)
        else:
            liste2.append(element)
    return liste2

def applyrule(rule,startstate): #testet og virker giver den færdige liste over rules.
    L = startstate[:]
    for i in range(len(L)):
        if L[i] == rule.start:
            L[i] = rule.rules
    return flatten(L)

def fracdraw(Fractal): #forlænger startstate med depht
    for x in range(Fractal.depth):
        Fractal.startstate = applyrule(Fractal.rules[0],Fractal.startstate)
    for element in Fractal.startstate:
        if element in Fractal.commands.keys():
             Fractal.commands[element].whisper(t,Fractal)

def read_file(filename):
    fil = open(filename,"r")  
    startstate = []
    rules = []
    length = []
    depth = []
    commands = {}
    args = {}
    types = []
    for line in fil:
        line = line.strip()
        split = line.split(" ")
        if split[0] == "start":
            startstate = split[1:]
        elif split[0] == "rule":
            rules.append(Rule(split[1],split[3:]))
        elif split[0] == "length":
            length = float(split[1])
        elif split[0] == "depth":
            depht = int(split[1])
        elif split[0] == "cmd" and (split[2] == "fd" or split[2] == "bk"):
            commands[split[1]] = Command(split[2],length)
            types.append(split[2])
        elif split[0] == "cmd" and split[2] != "fd" and split[2] != "nop":
            commands[split[1]] = Command(split[2],split[3])
            args[split[2]] = split[3]
            types.append(split[2])
        else:
            pass
    frac = Fractalprot(startstate,rules,commands,length,depht)
    return frac

testfrac = read_file("fern.fdl")
fracdraw(testfrac)

wait_for_user()
