#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:14:13 2019

@author: shrikar.amirisetty
"""

"""
Game class, used to refer champion, elite four and gym leaders of particular games
"""
class Game:
    def __init__(self, champion, eliteFourList, gymLeaderList):
        self.champion = champion
        self.eliteFourList = eliteFourList
        self.gymLeaderList = gymLeaderList

"""
Opponent class, used to assign the pokemon team of each opponent to an instance each
"""
class _Opponent:
    def __init__(self, pokemonList):
        self.pokemonList = pokemonList

"""
Pokemon class, used to define the characteristics each pokemon that your team needs
to go against. These characteristics will be used to calculate the heuristics of
each pokemon you could use to battle against them
"""
class _Pokemon:
    def __init__(self, typeList, level, hp, attack, defense, spAttack, spDefense,
                 speed, ability, heldItem, moveList):
        self.typeList = typeList
        self.level = level
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.spAttack = spAttack
        self.spDefense = spDefense
        self.speed = speed
        self.ability = ability
        self.heldItem = heldItem
        self.moveList = moveList

"""
List of gym leaders for each game
"""
gymLeadersREDGREENBLUE = []
gymLeadersYELLOW = []
gymLeadersGOLDSILVER = []
gymLeadersCRYSTAL = []
gymLeadersRUBYSAPPHIRE = []
gymLeadersFIREREDLEAFGREEN = []
gymLeadersEMERALD = []
gymLeadersDIAMONDPEARL = []
gymLeadersPLATINUM = []
gymLeadersHEARTGOLDSOULSILVER = []
gymLeadersBLACKWHITE = []
gymLeadersBLACK2WHITE2 = []
gymLeadersXY = []
gymLeadersOMEGARUBYALPHASAPPHIRE = []
gymLeadersSUNMOON = []
gymLeadersULTRASUNULTRAMOON = []

"""
Setting Brock for RED, GREEN, BLUE
"""
BrockREDGREENBLUE = _Opponent([])
BrockREDGREENBLUE.pokemonList += _Pokemon(["rock", "ground"], 12, 35, 27, 32, 15,
                                          15, 13, None, None, ["tackle", "defense-curl"])
BrockREDGREENBLUE.pokemonList += _Pokemon(["rock", "ground"], 14, 38, 21, 54, 17,
                                          21, 28, None, None, ["tackle", "screech",
                                          "bide", "bind"])
gymLeadersREDGREENBLUE += BrockREDGREENBLUE

"""
Setting Brock for YELLOW
"""
BrockYELLOW = _Opponent([])
BrockYELLOW.pokemonList += _Pokemon(["rock", "ground"], 10, 31, 24, 28, 14,
                                          14, 12, None, None, ["tackle"])
BrockYELLOW.pokemonList += _Pokemon(["rock", "ground"], 12, 34, 19, 47, 15,
                                          19, 25, None, None, ["tackle", "screech",
                                          "bide", "bind"])
gymLeadersYELLOW += BrockYELLOW

"""
Setting Brock for FIRERED, LEAFGREEN
"""
BrockFIREREDLEAFGREEN = _Opponent([])
BrockFIREREDLEAFGREEN.pokemonList += _Pokemon(["rock", "ground"], 12, 35, 27, 32, 15,
                                          15, 13, "rock-head", None, ["tackle",
                                          "defense-curl"])
BrockFIREREDLEAFGREEN.pokemonList += _Pokemon(["rock", "ground"], 14, 38, 21, 54, 17,
                                          21, 28, "rock-head", None, ["tackle",
                                          "rock-tomb", "bind"])
gymLeadersFIREREDLEAFGREEN += BrockFIREREDLEAFGREEN


"""
Setting Misty for RED, GREEN, BLUE
"""
MistyREDGREENBLUE = _Opponent([])
MistyREDGREENBLUE.pokemonList += _Pokemon(["water"], 18, 44, 26, 30, 35, 30, 41,
                                          None, None, ["tackle", "water-gun"])
MistyREDGREENBLUE.pokemonList += _Pokemon(["water", "psychic"], 21, 62, 43, 47,
                                          53, 47, 59, None, None, ["tackle", "water-gun",
                                          "bubble-beam"])
gymLeadersREDGREENBLUE += MistyREDGREENBLUE

"""
Setting Misty for YELLOW
"""
MistyYELLOW = _Opponent([])
MistyYELLOW.pokemonList += _Pokemon(["water"], 18, 44, 26, 30, 35, 30, 41,
                                          None, None, ["tackle", "water-gun"])
MistyYELLOW.pokemonList += _Pokemon(["water", "psychic"], 21, 62, 43, 47,
                                          53, 47, 59, None, None, ["tackle", "water-gun",
                                          "bubble-beam", "harden"])
gymLeadersYELLOW += MistyYELLOW

"""
Setting Misty for FIRERED, LEAFGREEN
"""
MistyFIREREDLEAFGREEN = _Opponent([])
MistyFIREREDLEAFGREEN.pokemonList += _Pokemon(["water"], 18, 44, 26, 30, 35, 30, 41,
                                          "natural-cure", None, ["tackle", "water-pulse",
                                          "harden", "recover"])
MistyFIREREDLEAFGREEN.pokemonList += _Pokemon(["water", "psychic"], 21, 62, 43, 47,
                                          53, 47, 59, "natural-cure", None, ["rapid-spin",
                                          "water-pulse", "recover", "swift"])
gymLeadersFIREREDLEAFGREEN += MistyFIREREDLEAFGREEN

"""
Setting Lt. Surge for RED, GREEN, BLUE
"""
LtSurgeREDGREENBLUE = _Opponent([])
LtSurgeREDGREENBLUE.pokemonList += _Pokemon(["electric"], 21, 54, 24, 32, 34, 34,
                                            53, None, None, ["tackle", "sonic-boom",
                                            "screech"])
LtSurgeREDGREENBLUE.pokemonList += _Pokemon(["electric"], 18, 46, 30, 24, 28, 28,
                                            42, None, None, ["thunder-shock", "growl",
                                          "thunder-wave", "quick-attack"])
LtSurgeREDGREENBLUE.pokemonList += _Pokemon(["electric"], 24, 70, 55, 38, 55, 50,
                                            65, None, None, ["thunder-shock", "growl",
                                          "thunderbolt"])
gymLeadersREDGREENBLUE += LtSurgeREDGREENBLUE

"""
Setting Lt. Surge for YELLOW
"""
LtSurgeYELLOW = _Opponent([])
LtSurgeYELLOW.pokemonList += _Pokemon(["electric"], 28, 80, 64, 44, 64, 58, 75,
                                      None, None, ["mega-punch", "growl", "thunderbolt",
                                      "mega-kick"])
gymLeadersYELLOW += LtSurgeYELLOW

"""
Setting Lt. Surge for FIRERED, LEAFGREEN
"""
LtSurgeFIREREDLEAFGREEN = _Opponent([])
LtSurgeFIREREDLEAFGREEN.pokemonList += _Pokemon(["electric"], 21, 54, 24, 32, 34,
                                                34, 53, "soundproof", None, ["tackle",
                                                "sonic-boom", "screech", "shock-wave"])
LtSurgeFIREREDLEAFGREEN.pokemonList += _Pokemon(["electric"], 18, 46, 30, 24, 28,
                                                28, 42, "static", None, ["shock-wave",
                                                "double-team", "thunder-wave", "quick-attack"])
LtSurgeFIREREDLEAFGREEN.pokemonList += _Pokemon(["electric"], 24, 70, 55, 38, 55,
                                                50, 65, "static", None, ["shock-wave",
                                                "double-team", "thunder-wave", "quick-attack"])
gymLeadersFIREREDLEAFGREEN += LtSurgeFIREREDLEAFGREEN

"""
Setting Erika for RED, GREEN, BLUE
"""
ErikaREDGREENBLUE = _Opponent([])
ErikaREDGREENBLUE.pokemonList += _Pokemon(["grass", "poison"], 29, 94, 74, 51, 71,
                                          54, 54, None, None, ["razor-leaf", "wrap",
                                            "poison-powder", "sleep-powder"])
ErikaREDGREENBLUE.pokemonList += _Pokemon(["grass"], 24, 72, 38, 67, 60, 31, 41,
                                          None, None, ["constrict", "bind"])
ErikaREDGREENBLUE.pokemonList += _Pokemon(["grass", "poison"], 29, 91, 60, 63, 77,
                                          66, 42, None, None, ["petal-dance", "poison-powder",
                                          "mega-drain", "sleep-powder"])
gymLeadersREDGREENBLUE += ErikaREDGREENBLUE

"""
Setting Erika for YELLOW
"""
ErikaYELLOW = _Opponent([])
ErikaYELLOW.pokemonList += _Pokemon(["grass", "poison"], 32, 93, 72, 46, 69, 43,
                                    50, None, None, ["razor-leaf", "acid", "stun-spore",
                                    "sleep-powder"])
ErikaYELLOW.pokemonList += _Pokemon(["grass"], 30, 88, 47, 83, 74, 38, 50, None,
                                    None, ["constrict", "bind", "mega-drain", "vine-whip"])
ErikaYELLOW.pokemonList += _Pokemon(["grass", "poison"], 32, 91, 60, 63, 77, 66,
                                    42, None, None, ["petal-dance", "acid", "stun-spore",
                                    "sleep-powder"])
gymLeadersYELLOW += ErikaYELLOW

"""
Setting Erika for FIRERED, LEAFGREEN
"""
ErikaFIREREDLEAFGREEN = _Opponent([])
ErikaFIREREDLEAFGREEN.pokemonList += _Pokemon(["grass", "poison"], 29, 94, 74, 51,
                                              71, 54, 54, "chlorophyll", None, ["stun-spore",
                                              "acid", "poison-powder", "giga-drain"])
ErikaFIREREDLEAFGREEN.pokemonList += _Pokemon(["grass"], 24, 72, 38, 67, 60, 31,
                                              41, "chlorophyll", None, ["constrict",
                                              "poison-powder", "ingrain", "giga-drain"])
ErikaFIREREDLEAFGREEN.pokemonList += _Pokemon(["grass", "poison"], 29, 91, 60, 63,
                                              77, 66, 42, "chlorophyll", None, ["acid",
                                              "stun-spore", "giga-drain", "sleep-powder"])
gymLeadersFIREREDLEAFGREEN += ErikaFIREREDLEAFGREEN

"""
Setting Koga for RED, GREEN, BLUE
"""
KogaREDGREENBLUE = _Opponent([])
KogaREDGREENBLUE.pokemonList += _Pokemon(["poison"], 37, 88, 64, 86, 60, 49, 42,
                                         None, None, ["tackle", "smog", "sludge",
                                         "smoke-screen"])
KogaREDGREENBLUE.pokemonList += _Pokemon(["poison"], 37, 88, 64, 86, 60, 49, 42,
                                         None, None, ["tackle", "smog", "sludge",
                                         "smoke-screen"])
KogaREDGREENBLUE.pokemonList += _Pokemon(["poison"], 39, 142, 68, 75, 67, 95, 56,
                                          None, None, ["disable", "poison-gas",
                                          "minimize", "sludge"])
KogaREDGREENBLUE.pokemonList += _Pokemon(["poison"], 43, 122, 95, 121, 91, 78, 69,
                                         None, None, ["smog", "sludge", "toxic",
                                         "selfdestruct"])
gymLeadersREDGREENBLUE += KogaREDGREENBLUE

"""
Setting Koga for YELLOW
"""
KogaYELLOW = _Opponent([])
KogaYELLOW.pokemonList += _Pokemon(["bug", "poison"], 44, 120, 67, 62, 53, 67, 58,
                                         None, None, ["tackle", "toxic", "sleep-powder",
                                         "psychic"])
KogaYELLOW.pokemonList += _Pokemon(["bug", "poison"], 46, 125, 69, 65, 56, 69, 60,
                                         None, None, ["toxic", "psybeam", "supersonic",
                                         "psychic"])
KogaYELLOW.pokemonList += _Pokemon(["bug", "poison"], 48, 130, 72, 67, 58, 72, 63,
                                          None, None, ["toxic", "psychic", "sleep-powder",
                                          "double-edge"])
KogaYELLOW.pokemonList += _Pokemon(["bug", "poison"], 50, 145, 85, 80, 110, 95,
                                   110, None, None, ["psychic", "leech-life", "toxic",
                                         "double-team"])
gymLeadersYELLOW += KogaYELLOW

"""
Setting Koga for FIRERED, LEAFGREEN
"""
KogaFIREREDLEAFGREEN = _Opponent([])
KogaFIREREDLEAFGREEN.pokemonList += _Pokemon(["poison"], 37, 88, 64, 86, 60, 49,
                                             42, "levitate", None, ["selfdestruct",
                                             "toxic", "sludge", "smoke-screen"])
KogaFIREREDLEAFGREEN.pokemonList += _Pokemon(["poison"], 37, 88, 64, 86, 60, 49,
                                             42, "levitate", None, ["selfdestruct",
                                             "toxic", "sludge", "smoke-screen"])
KogaFIREREDLEAFGREEN.pokemonList += _Pokemon(["poison"], 39, 142, 68, 75, 67, 95,
                                             56, "sticky-hold", None, ["acid-armor",
                                             "toxic", "minimize", "sludge"])
KogaFIREREDLEAFGREEN.pokemonList += _Pokemon(["poison"], 43, 122, 95, 121, 91, 78,
                                             69, "levitate", None, ["tackle", "sludge",
                                             "toxic", "smoke-screen"])
gymLeadersFIREREDLEAFGREEN += KogaFIREREDLEAFGREEN

"""

"""






