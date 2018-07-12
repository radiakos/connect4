#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 21:27:02 2018

@author: Arpit
"""
import matplotlib.pyplot as plt
import numpy as np
from c4Game import C4Game
from t3Game import T3Game

class QPlot:
    def __init__(self, stateCnt, actionCnt, ann, interval=1000):
        self.stateCnt = stateCnt
        self.actionCnt = actionCnt
        self.ann = ann
        self.interval = interval
        self.cnt = 0
        self.states = np.empty([0, stateCnt])
        self.actions = []
#        self.getStatesAndActionsC4()
        self.getStatesAndActionsT3()
        self.x = []
        self.ys = np.empty((self.states.shape[0],), dtype=object)
        for i,v in enumerate(self.ys): self.ys[i] = list()
        
    def add(self):
        self.x.append(self.cnt * self.interval)
        preds = self.ann.predict(self.states)
        for index, pred in enumerate(preds):
#            self.ys[index].append(pred[self.actions[index]])
            self.ys[index].append(np.amax(pred))
        self.cnt += 1
        
    def show(self):
        for i in range(0, self.states.shape[0]):
            plt.plot(self.x, self.ys[i], label=i)
            
        plt.legend(loc = "best")
        plt.savefig('/Users/Arpit/Desktop/qPlot.png')
        plt.draw()
        plt.show()

    def printQValues(self):
        preds = self.ann.predict(self.states)
        for index, pred in enumerate(preds):
            print (str(pred[self.actions[index]]) + ", ", end="")
        print ("\n")
        
    def getStatesAndActionsT3(self):
        g = T3Game()
        
        g.newGame()
        g.step(3)
        g.step(0)
        g.step(6)
        g.step(1)
        self.states = np.vstack([self.states, g.getCurrentState()])
        
        g.newGame()
        g.step(4)
        g.step(5)
        self.states = np.vstack([self.states, g.getCurrentState()])

    def getStatesAndActionsC4(self):
        g = C4Game()
        
        g.newGame()
        g.step(0)
        g.step(2)
        g.step(3)
        g.step(2)
        g.step(3)
        g.step(2)
        self.states = np.vstack([self.states, g.getCurrentState()])
        self.actions.append(2)
        self.states = np.vstack([self.states, g.getCurrentState()])
        self.actions.append(3)
        
        g.newGame()
        g.step(0)
        g.step(5)
        g.step(3)
        g.step(6)
        g.step(2)
        g.step(5)
        self.states = np.vstack([self.states, g.getCurrentState()])
        self.actions.append(1)

        g.newGame()
        self.states = np.vstack([self.states, g.getCurrentState()])
        self.actions.append(3)