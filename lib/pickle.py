#!/usr/bin/python

from chatterbotapi import ChatterBotFactory, ChatterBotType
import sys

factory = ChatterBotFactory()

bot1 = factory.create(ChatterBotType.CLEVERBOT)
bot1session = bot1.create_session()

bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
bot2session = bot2.create_session()

test = raw_input("Say: ");
s = bot2session.think(test);
