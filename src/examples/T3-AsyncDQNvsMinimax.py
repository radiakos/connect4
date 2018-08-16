#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 00:37:35 2018

@author: Arpit
"""

from games.t3Game import T3Game
from environment import Environment
from players.minimaxT3Player import MinimaxT3Player
from players.qPlayer import QPlayer
from brains.qBrain import QBrain
from envThread import EnvThread
from memory.pMemory import PMemory
from settings import charts_folder
from keras.utils import plot_model

isConv = True
layers = [
	{'filters':16, 'kernel_size': (2,2), 'size':24}
	 , {'filters':16, 'kernel_size': (2,2), 'size':24}
	]

game = T3Game(3, isConv=isConv)

brain = QBrain('1', game, layers=layers, load_weights=False)
plot_model(brain.model, show_shapes=True, to_file=charts_folder + 'model.png')

player_config = {"memory":PMemory(1000), "goodMemory":PMemory(1000), "targetNet":False,
                "batch_size":32, "gamma":0.90, "n_step":3}
epsilons = [0.05, 0.15, 0.25, 0.35]

i = 0
threads = []
while i < 4:
    game = T3Game(3, name=i, isConv=isConv)
    p1 = QPlayer(i, game, brain=brain, epsilon=epsilons[i], **player_config)
    p2 = MinimaxT3Player(2, game, epsilon=0.05)
    env = Environment(game, p1, p2)
    threads.append(EnvThread(env))
    i += 1

for t in threads:
    t.start()
