"""Custom agents"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy

from pysc2.agents import base_agent
from pysc2.lib import actions
from pysc2.lib import features

_PLAYER_RELATIVE = features.SCREEN_FEATURES.player_relative.index
_PLAYER_FRIENDLY = 1
_PLAYER_NEUTRAL = 3  # beacon/minerals
_PLAYER_HOSTILE = 4
_NO_OP = actions.FUNCTIONS.no_op.id
_MOVE_SCREEN = actions.FUNCTIONS.Move_screen.id
_ATTACK_SCREEN = actions.FUNCTIONS.Attack_screen.id
_SELECT_ARMY = actions.FUNCTIONS.select_army.id
_BUILD_BASE = actions.FUNCTIONS.Build_CommandCenter_screen.id
_MINERALS_FOR_BASE = 400
_MINERAL_INDEX = 7
_NOT_QUEUED = [0]
_SELECT_ALL = [0]

#seems like collect minerals and gas map forces a terran race?

class CollectMineralsAndGas(base_agent.BaseAgent):
  """An agent specifically for solving the CollectMineralShards map."""

  def step(self, obs):
    super(CollectMineralsAndGas, self).step(obs)
    #iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues
    #print(obs.observation.keys())
    #cargo', 'minimap', 'game_loop', 'available_actions', 'screen', 'control_groups', 'multi_select', 'cargo_slots_available', 'player', 'single_select', 'build_queue', 'score_cumulative'
    #print(obs.observation["cargo"])
    #print(obs.observation["player"])
    #print(obs.observation["build_queue"])
    #print(obs.observation["score_cumulative"])
    #print(obs.observation["minimap"])
    #print(obs.observation["screen"])
    #print(obs.observation)
    if _MINERALS_FOR_BASE < obs.observation["score_cumulative"][_MINERAL_INDEX]:
      if _BUILD_BASE in obs.observation["available_actions"]:
        #find nearest available nexus point
        #if base point on screen, build nexus
        #else move camera to center on nexus
        _BASE_X, _BASE_Y = numpy.random.randint(0, 1), numpy.random.randint(0, 1)
        print("built a command center! (" + str(_BASE_X) + ", " + str(_BASE_Y) + ")")
        return actions.FunctionCall(_BUILD_BASE, [_BASE_X, _BASE_Y])
        
      #else:
        #print("didn't build a nexus...")
        #select random probe
    

    #for each base:
    #  if base is rallied to a base that is full of workers
    #    find the unfilled base with fewest probes (if it exists) and set rally there


    # if our number of probes queued + number of probes existing is >= our supply
      #build a pylon in a random nearby place

    #find a base with a rally point set to an unfull base with no worker queued
      #enqueue worker

    #if we have enough for an assimilator, build an assimilator

    #if we haveempty assimillator slots, move a mineral worker there

    return actions.FunctionCall(_NO_OP, [])
