from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

def Sentaku():
    mc.postToChat("どれを選びますか？下の中から一つ選んでクリックしてね。")

def Kinkakuji(mc, width=20):
    mc.setBlocks(-width*2,  param.Y_SEA,    -width*2,   width*2,   param.Y_SEA,    width*2,    param.WATER      )
    mc.setBlocks(-width,    param.Y_SEA,    -width,     width,     param.Y_SEA,    width,      param.STONE      )
    mc.setBlocks(-width+1,  param.Y_SEA+1,  -width+1,   width-1,   param.Y_SEA+1,  width-1,    param.FENCE      )
    mc.setBlocks(-width+2,  param.Y_SEA+1,  -width+2,   width-2,   param.Y_SEA+1,  width-2,    param.CONCRETE   )
    mc.setBlocks(-width+1,  param.Y_SEA+2,  -width+1,   width-1,   param.Y_SEA+2,  width-1,    param.SPRUCE     )
    mc.setBlocks(-width+1,  param.Y_SEA+3,  -width+1,   width-1,   param.Y_SEA+3,  width-1,    param.FENCE      )
    mc.setBlocks(-width+2,  param.Y_SEA+3,  -width+2,   width-2,   param.Y_SEA+3,  width-2,    param.AIR        )
    mc.setBlocks(-width+1,  param.Y_SEA+3,  -width+4,   -width+1,  param.Y_SEA+3,  width,      param.AIR        )
    mc.setBlocks(-width+1,  param.Y_SEA+3,  width-1,    width-10,  param.Y_SEA+3,  width+1,    param.AIR        )
    mc.setBlocks(-width+4,  param.Y_SEA+3,  -width+5,   width-4,   param.Y_SEA+7,  width-4,    param.CONCRETE   )
    mc.setBlocks(-width+4,  param.Y_SEA+8,  -width+5,   width-4,   param.Y_SEA+8,  width-4,    param.DARK       )
    mc.setBlocks(-width+4,  param.Y_SEA+3,  -width+5,   width-4,   param.Y_SEA+7,  -width+5,   param.SPRUCE     )
    mc.setBlocks(-width+4,  param.Y_SEA+6,  -width+5,   width-4,   param.Y_SEA+6,  width-4,    param.DARK       )  
    mc.setBlocks(-width+5,  param.Y_SEA+3,  -width+6,   width-5,   param.Y_SEA+8,  width-5,    param.AIR        )
    mc.setBlocks(-width+4,  param.Y_SEA+3,  -width+5,   -width+4,  param.Y_SEA+8,  -width+5,   param.DARK       )
    mc.setBlocks(-width+4,  param.Y_SEA+3,  -width+13,  -width+4,  param.Y_SEA+8,  -width+13,  param.DARK       )
    mc.setBlocks(-width+4,  param.Y_SEA+3,  -width+21,  -width+4,  param.Y_SEA+8,  -width+21,  param.DARK       )
    mc.setBlocks(-width+4,  param.Y_SEA+3,  -width+29,  -width+4,  param.Y_SEA+8,  -width+29,  param.DARK       )
    mc.setBlocks(-width+4,  param.Y_SEA+3,  width-4,    -width+4,  param.Y_SEA+8,  width-4,    param.DARK       )
    mc.setBlocks(-width+12, param.Y_SEA+3,  width-4,    -width+12, param.Y_SEA+8,  width-4,    param.DARK       )
    mc.setBlocks(-width+20, param.Y_SEA+3,  width-4,    -width+20, param.Y_SEA+8,  width-4,    param.DARK       )
    mc.setBlocks(-width+28, param.Y_SEA+3,  width-4,    -width+28, param.Y_SEA+8,  width-4,    param.DARK       )
    mc.setBlocks(width-4,   param.Y_SEA+3,  width-4,    width-4,   param.Y_SEA+8,  width-4,    param.DARK       )
    mc.setBlocks(width-4,   param.Y_SEA+3,  width-12,   width-4,   param.Y_SEA+8,  width-12,   param.DARK       )
    mc.setBlocks(width-4,   param.Y_SEA+3,  width-20,   width-4,   param.Y_SEA+8,  width-20,   param.DARK       )
    mc.setBlocks(width-4,   param.Y_SEA+3,  width-28,   width-4,   param.Y_SEA+8,  width-28,   param.DARK       )        
    mc.setBlocks(width-4,   param.Y_SEA+3,  -width+5,   width-4,   param.Y_SEA+8,  -width+5,   param.DARK       )
    mc.setBlocks(width-12,  param.Y_SEA+3,  -width+5,   width-12,  param.Y_SEA+8,  -width+5,   param.DARK       )
    mc.setBlocks(width-20,  param.Y_SEA+3,  -width+5,   width-20,  param.Y_SEA+8,  -width+5,   param.DARK       )
    mc.setBlocks(width-28,  param.Y_SEA+3,  -width+5,   width-28,  param.Y_SEA+8,  -width+5,   param.DARK       )
    mc.setBlocks(-width+5,  param.Y_SEA+8,  -width+6,   width-5,   param.Y_SEA+8,  width-5,    param.GLOWSTONE  )
    mc.setBlocks(-width+2,  param.Y_SEA+9,  -width+2,   width-2,   param.Y_SEA+9,  width-2,    param.GOLD_BLOCK )
    mc.setBlocks(-width+2,  param.Y_SEA+10, -width+2,   width-2,   param.Y_SEA+10, width-2,    param.FENCE      )
    mc.setBlocks(-width+3,  param.Y_SEA+10, -width+3,   width-3,   param.Y_SEA+10, width-3,    param.AIR        )
    mc.setBlocks(-width+5,  param.Y_SEA+10, -width+5,   width-5,   param.Y_SEA+14, width-5,    param.GOLD_BLOCK )
    mc.setBlocks(-width+5,  param.Y_SEA+13, -width+5,   width-5,   param.Y_SEA+13, width-5,    param.DARK       )
    mc.setBlocks(-width+5,  param.Y_SEA+15, -width+5,   width-5,   param.Y_SEA+15, width-5,    param.DARK       )
    mc.setBlocks(-width+6,  param.Y_SEA+10, -width+6,   width-6,   param.Y_SEA+15, width-6,    param.AIR        )
    mc.setBlocks(-width+6,  param.Y_SEA+15, -width+6,   width-6,   param.Y_SEA+15, width-6,    param.GLOWSTONE  )
    mc.setBlocks(-width+9,  param.Y_SEA+10, -width+9,   -width+9,  param.Y_SEA+15, -width+9,   param.DARK       )
    mc.setBlocks(-width+16, param.Y_SEA+10, -width+9,   -width+16, param.Y_SEA+15, -width+9,   param.DARK       )
    mc.setBlocks(width-16,  param.Y_SEA+10, -width+9,   width-16,  param.Y_SEA+15, -width+9,   param.DARK       )
    mc.setBlocks(width-9,   param.Y_SEA+10, -width+9,   width-9,   param.Y_SEA+15, -width+9,   param.DARK       )
    mc.setBlocks(width-9,   param.Y_SEA+10, -width+16,  width-9,   param.Y_SEA+15, -width+16,  param.DARK       )
    mc.setBlocks(width-9,   param.Y_SEA+10, width-16,   width-9,   param.Y_SEA+15, width-16,   param.DARK       )
    mc.setBlocks(width-9,   param.Y_SEA+10, width-9,    width-9,   param.Y_SEA+15, width-9,    param.DARK       )
    mc.setBlocks(width-16,  param.Y_SEA+10, width-9,    width-16,  param.Y_SEA+15, width-9,    param.DARK       )
    mc.setBlocks(-width+16, param.Y_SEA+10, width-9,    -width+16, param.Y_SEA+15, width-9,    param.DARK       )
    mc.setBlocks(-width+9,  param.Y_SEA+10, width-9,    -width+9,  param.Y_SEA+15, width-9,    param.DARK       )
    mc.setBlocks(-width+9,  param.Y_SEA+10, width-16,   -width+9,  param.Y_SEA+15, width-16,   param.DARK       )
    mc.setBlocks(-width+9,  param.Y_SEA+10, -width+16,  -width+9,  param.Y_SEA+15, -width+16,  param.DARK       )
    mc.setBlocks(-width+1,  param.Y_SEA+16, -width+1,   width-1,   param.Y_SEA+16, width-1,    param.SPRUCE     )
    mc.setBlocks(-width+4,  param.Y_SEA+17, -width+4,   width-4,   param.Y_SEA+17, width-4,    param.SPRUCE     )
    mc.setBlocks(-width+6,  param.Y_SEA+18, -width+6,   width-6,   param.Y_SEA+18,  width-6,   param.SPRUCE     )
    mc.setBlocks(-width+8,  param.Y_SEA+19, -width+8,   width-8,   param.Y_SEA+19,  width-8,   param.SPRUCE     )
    mc.setBlocks(-width+9,  param.Y_SEA+20, -width+9,   width-9,   param.Y_SEA+20,  width-9,   param.SPRUCE     )
    mc.setBlocks(width, param.Y_SEA, width,  width, param.Y_SEA, width,  )
    mc.setBlocks(width, param.Y_SEA, width,  width, param.Y_SEA, width,  )
    mc.setBlocks(width, param.Y_SEA, width,  width, param.Y_SEA, width,  )
    mc.setBlocks(width, param.Y_SEA, width,  width, param.Y_SEA, width,  )
    mc.setBlocks(width, param.Y_SEA, width,  width, param.Y_SEA, width,  )
    

if __name__ == "__main__":
    mc = Minecraft.create(port=param.PORT_MC)
    
    mc.postToChat("I`m going to bulit Kinkakuji!")
    sleep(1)
    set(mc, width=60)
    mc.setBlocks(-width, param.Y_SEA+1, -width,   width, param.AXIS_TOP, width,   param.AIR        )
    mc.setBlocks(-width, param.Y_SEA-1, -width,   width, 0             , width,   param.STONE      )
    mc.setBlocks(-width, param.Y_SEA,   -width,   width, param.Y_SEA   , width,   param.GRASS_BLOCK)
    Kinkakuji(mc, width=20)