"""
Draw x, y, z axis in the Minecraft world
    x: stone
    y: grass/dirt
    z: gold
Flatten the world
    width: Size of flat world to produce.
           x, z: from -widh to width
           y: from AXIS_BOTTOM to AXIS_TOP

mc: an instance of Minecraft must be created beforehand
"""

from mcje.minecraft import Minecraft
import param_MCJE as param

from time import sleep

def reset_minecraft_world(mc, width=80):
    mc.setBlocks(-width, param.Y_SEA+1, -width,   width, param.AXIS_TOP, width,   param.AIR        )
    mc.setBlocks(-width, param.Y_SEA-1, -width,   width, 0             , width,   param.STONE      )
    mc.setBlocks(-width, param.Y_SEA,   -width,   width, param.Y_SEA   , width,   param.GRASS_BLOCK)

if __name__ == "__main__":
    mc = Minecraft.create(port=param.PORT_MC)

    mc.postToChat("axis_flat module main part")
    mc.postToChat("reset_minecraft_world")

    reset_minecraft_world(mc, width=100)
    # draw_XYZ_axis(mc, wait=0.2)
    # clear_XYZ_axis(mc, wait=0)

