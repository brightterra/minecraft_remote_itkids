from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

def Sentaku():
    mc.postToChat("どれを選びますか？下の中から一つ選んでクリックしてね。")

def Kinkakuji(mc, width=20 ,X=0 ,Z=0):
    mc.setBlocks(-width*2+X,  param.Y_SEA+1,  -width*2+Z,   width*2+X,   param.AXIS_TOP, width*2+Z,    param.AIR        )
    mc.setBlocks(-width*2+X,  param.Y_SEA-1,  -width*2+Z,   width*2+X,   0,              width*2+Z,    param.STONE      )
    mc.setBlocks(-width*2+X,  param.Y_SEA,    -width*2+Z,   width*2+X,   param.Y_SEA,    width*2+Z,    param.GRASS_BLOCK)
    mc.setBlocks(-width*2+X,  param.Y_SEA,    -width*2+Z,   width*2+X,   param.Y_SEA,    width*2+Z,    param.WATER      )
    mc.setBlocks(-width+X,    param.Y_SEA,    -width+Z,     width+X,     param.Y_SEA,    width+Z,      param.STONE      )
    mc.setBlocks(-width+1+X,  param.Y_SEA+1,  -width+1+Z,   width-1+X,   param.Y_SEA+1,  width-1+Z,    param.FENCE      )
    mc.setBlocks(-width+2+X,  param.Y_SEA+1,  -width+2+Z,   width-2+X,   param.Y_SEA+1,  width-2+Z,    param.CONCRETE   )
    mc.setBlocks(-width+1+X,  param.Y_SEA+2,  -width+1+Z,   width-1+X,   param.Y_SEA+2,  width-1+Z,    param.SPRUCE     )
    mc.setBlocks(-width+1+X,  param.Y_SEA+3,  -width+1+Z,   width-1+X,   param.Y_SEA+3,  width-1+Z,    param.FENCE      )
    mc.setBlocks(-width+2+X,  param.Y_SEA+3,  -width+2+Z,   width-2+X,   param.Y_SEA+3,  width-2+Z,    param.AIR        )
    mc.setBlocks(-width+1+X,  param.Y_SEA+3,  -width+4+Z,   -width+1+X,  param.Y_SEA+3,  width+Z,      param.AIR        )
    mc.setBlocks(-width+1+X,  param.Y_SEA+3,  width-1+Z,    width-10+X,  param.Y_SEA+3,  width+1+Z,    param.AIR        )
    mc.setBlocks(-width+4+X,  param.Y_SEA+3,  -width+5+Z,   width-4+X,   param.Y_SEA+7,  width-4+Z,    param.CONCRETE   )
    mc.setBlocks(-width+4+X,  param.Y_SEA+3,  -width+5+Z,   width-4+X,   param.Y_SEA+8,  -width+5+Z,   param.SPRUCE     )    
    mc.setBlocks(-width+4+X,  param.Y_SEA+6,  -width+5+Z,   width-4+X,   param.Y_SEA+6,  width-4+Z,    param.DARK       )    
    mc.setBlocks(-width+4+X,  param.Y_SEA+8,  -width+5+Z,   width-4+X,   param.Y_SEA+8,  width-4+Z,    param.DARK       )
    mc.setBlocks(-width+5+X,  param.Y_SEA+3,  -width+6+Z,   width-5+X,   param.Y_SEA+8,  width-5+Z,    param.AIR        )
    mc.setBlocks(-width+4+X,  param.Y_SEA+3,  -width+5+Z,   -width+4+X,  param.Y_SEA+8,  -width+5+Z,   param.DARK       )
    mc.setBlock( -width+4+X,  param.Y_SEA+6,  -width+4+Z,   param.FENCE      )
    mc.setBlock( -width+4+X,  param.Y_SEA+7,  -width+4+Z,   param.TORCH      )
    mc.setBlock( -width+3+X,  param.Y_SEA+6,  -width+5+Z,   param.FENCE      )
    mc.setBlock( -width+3+X,  param.Y_SEA+7,  -width+5+Z,   param.TORCH      )
    mc.setBlocks(-width+4+X,  param.Y_SEA+3,  -width+13+Z,  -width+4+X,  param.Y_SEA+8,  -width+13+Z,  param.DARK       )
    mc.setBlock( -width+3+X,  param.Y_SEA+6,  -width+13+Z,  param.FENCE      )
    mc.setBlock( -width+3+X,  param.Y_SEA+7,  -width+13+Z,  param.TORCH      )
    mc.setBlocks(-width+4+X,  param.Y_SEA+3,  Z,            -width+4+X,  param.Y_SEA+8,  Z,            param.DARK       )
    mc.setBlock( -width+3+X,  param.Y_SEA+6,  Z,            param.FENCE      )
    mc.setBlock( -width+3+X,  param.Y_SEA+7,  Z,            param.TORCH      )
    mc.setBlocks(-width+4+X,  param.Y_SEA+3,  -width+28+Z,  -width+4+X,  param.Y_SEA+8,  -width+28+Z,  param.DARK       )
    mc.setBlock( -width+3+X,  param.Y_SEA+6,  -width+28+Z,  param.FENCE      )
    mc.setBlock( -width+3+X,  param.Y_SEA+7,  -width+28+Z,  param.TORCH      )
    mc.setBlocks(-width+4+X,  param.Y_SEA+3,  width-4+Z,    -width+4+X,  param.Y_SEA+8,  width-4+Z,    param.DARK       )
    mc.setBlock( -width+3+X,  param.Y_SEA+6,  width-4+Z,    param.FENCE      )
    mc.setBlock( -width+3+X,  param.Y_SEA+7,  width-4+Z,    param.TORCH      )
    mc.setBlock( -width+4+X,  param.Y_SEA+6,  width-3+Z,    param.FENCE      )
    mc.setBlock( -width+4+X,  param.Y_SEA+7,  width-3+Z,    param.TORCH      )
    mc.setBlocks(-width+12+X, param.Y_SEA+3,  width-4+Z,    -width+12+X, param.Y_SEA+8,  width-4+Z,    param.DARK       )
    mc.setBlock( -width+12+X, param.Y_SEA+6,  width-3+Z,    param.FENCE      )
    mc.setBlock( -width+12+X, param.Y_SEA+7,  width-3+Z,    param.TORCH      )
    mc.setBlocks(X,           param.Y_SEA+3,  width-4+Z,    X,           param.Y_SEA+8,  width-4+Z,    param.DARK       )
    mc.setBlock( X,           param.Y_SEA+6,  width-3+Z,    param.FENCE      )
    mc.setBlock( X,           param.Y_SEA+7,  width-3+Z,    param.TORCH      )
    mc.setBlocks(-width+28+X, param.Y_SEA+3,  width-4+Z,    -width+28+X, param.Y_SEA+8,  width-4+Z,    param.DARK       )
    mc.setBlock( -width+28+X, param.Y_SEA+6,  width-3+Z,    param.FENCE      )
    mc.setBlock( -width+28+X, param.Y_SEA+7,  width-3+Z,    param.TORCH      )
    mc.setBlocks(width-4+X,   param.Y_SEA+3,  width-4+Z,    width-4+X,   param.Y_SEA+8,  width-4+Z,    param.DARK       )
    mc.setBlock( width-4+X,   param.Y_SEA+6,  width-3+Z,    param.FENCE      )
    mc.setBlock( width-4+X,   param.Y_SEA+7,  width-3+Z,    param.TORCH      )
    mc.setBlock( width-3+X,   param.Y_SEA+6,  width-4+Z,    param.FENCE      )
    mc.setBlock( width-3+X,   param.Y_SEA+7,  width-4+Z,    param.TORCH      )
    mc.setBlocks(width-4+X,   param.Y_SEA+3,  width-12+Z,   width-4+X,   param.Y_SEA+8,  width-12+Z,   param.DARK       )
    mc.setBlock( width-3+X,   param.Y_SEA+6,  width-12+Z,   param.FENCE      )
    mc.setBlock( width-3+X,   param.Y_SEA+7,  width-12+Z,   param.TORCH      )
    mc.setBlocks(width-4+X,   param.Y_SEA+3,  Z,            width-4+X,   param.Y_SEA+8,  Z,            param.DARK       )
    mc.setBlock( width-3+X,   param.Y_SEA+6,  Z,            param.FENCE      )
    mc.setBlock( width-3+X,   param.Y_SEA+7,  Z,            param.TORCH      )
    mc.setBlocks(width-4+X,   param.Y_SEA+3,  width-28+Z,   width-4+X,   param.Y_SEA+8,  width-28+Z,   param.DARK       )        
    mc.setBlock( width-3+X,   param.Y_SEA+6,  width-28+Z,   param.FENCE      )
    mc.setBlock( width-3+X,   param.Y_SEA+7,  width-28+Z,   param.TORCH      )
    mc.setBlocks(width-4+X,   param.Y_SEA+3,  -width+5+Z,   width-4+X,   param.Y_SEA+8,  -width+5+Z,   param.DARK       )
    mc.setBlock( width-4+X,   param.Y_SEA+6,  -width+4+Z,   param.FENCE      )
    mc.setBlock( width-4+X,   param.Y_SEA+7,  -width+4+Z,   param.TORCH      )
    mc.setBlock( width-3+X,   param.Y_SEA+6,  -width+5+Z,   param.FENCE      )
    mc.setBlock( width-3+X,   param.Y_SEA+7,  -width+5+Z,   param.TORCH      )
    mc.setBlocks(width-12+X,  param.Y_SEA+3,  -width+5+Z,   width-12+X,  param.Y_SEA+8,  -width+5+Z,   param.DARK       )
    mc.setBlock( width-12+X,  param.Y_SEA+6,  -width+4+Z,   param.FENCE      )
    mc.setBlock( width-12+X,  param.Y_SEA+7,  -width+4+Z,   param.TORCH      )
    mc.setBlocks(X,           param.Y_SEA+3,  -width+5+Z,   X,           param.Y_SEA+8,  -width+5+Z,   param.DARK       )
    mc.setBlock( X,           param.Y_SEA+6,  -width+4+Z,   param.FENCE      )
    mc.setBlock( X,           param.Y_SEA+7,  -width+4+Z,   param.TORCH      )
    mc.setBlocks(width-28+X,  param.Y_SEA+3,  -width+5+Z,   width-28+X,  param.Y_SEA+8,  -width+5+Z,   param.DARK       )
    mc.setBlock( width-28+X,  param.Y_SEA+6,  -width+4+Z,   param.FENCE      )
    mc.setBlock( width-28+X,  param.Y_SEA+7,  -width+4+Z,   param.TORCH      )  
    mc.setBlocks(-width+5+X,  param.Y_SEA+8,  -width+6+Z,   width-5+X,   param.Y_SEA+8,  width-5+Z,    param.GLOWSTONE  )
    mc.setBlocks(-width+2+X,  param.Y_SEA+9,  -width+2+Z,   width-2+X,   param.Y_SEA+9,  width-2+Z,    param.GOLD_BLOCK )
    mc.setBlock( -width+2+X,  param.Y_SEA+8,  -width+2+Z,   param.LANTERN )
    mc.setBlock( -width+2+X,  param.Y_SEA+8,  width-2+Z,    param.LANTERN )
    mc.setBlock( width-2+X,   param.Y_SEA+8,  -width+2+Z,   param.LANTERN )
    mc.setBlock( width-2+X,   param.Y_SEA+8,  width-2+Z,    param.LANTERN )
    mc.setBlocks(-width+2+X,  param.Y_SEA+10, -width+2+Z,   width-2+X,   param.Y_SEA+10, width-2+Z,    param.FENCE      )
    mc.setBlocks(-width+3+X,  param.Y_SEA+10, -width+3+Z,   width-3+X,   param.Y_SEA+10, width-3+Z,    param.AIR        )
    mc.setBlocks(-width+5+X,  param.Y_SEA+10, -width+5+Z,   width-5+X,   param.Y_SEA+14, width-5+Z,    param.GOLD_BLOCK )
    mc.setBlocks(-width+5+X,  param.Y_SEA+13, -width+5+Z,   width-5+X,   param.Y_SEA+13, width-5+Z,    param.DARK       )
    mc.setBlocks(-width+5+X,  param.Y_SEA+15, -width+5+Z,   width-5+X,   param.Y_SEA+15, width-5+Z,    param.DARK       )
    mc.setBlocks(-width+6+X,  param.Y_SEA+10, -width+6+Z,   width-6+X,   param.Y_SEA+15, width-6+Z,    param.AIR        )
    mc.setBlocks(-width+6+X,  param.Y_SEA+15, -width+6+Z,   width-6+X,   param.Y_SEA+15, width-6+Z,    param.GLOWSTONE  )
    mc.setBlocks(width-5+X,   param.Y_SEA+10, -width+5+Z,   width-25+X,  param.Y_SEA+14, -width+12+Z,  param.GOLD_BLOCK )
    mc.setBlocks(width-5+X,   param.Y_SEA+13, -width+5+Z,   width-25+X,  param.Y_SEA+13, -width+12+Z,  param.DARK       )
    mc.setBlocks(width-5+X,   param.Y_SEA+15, -width+5+Z,   width-25+X,  param.Y_SEA+15, -width+12+Z,  param.DARK       )
    mc.setBlocks(width-5+X,   param.Y_SEA+10, -width+5+Z,   width-24+X,  param.Y_SEA+15, -width+11+Z,  param.AIR        )
    mc.setBlocks(-width+5+X,  param.Y_SEA+10, -width+5+Z,   -width+5+X,  param.Y_SEA+15, -width+5+Z,   param.DARK       )
    mc.setBlock( -width+5+X,  param.Y_SEA+13, -width+4+Z,    param.FENCE      )
    mc.setBlock( -width+5+X,  param.Y_SEA+14, -width+4+Z,    param.TORCH      )
    mc.setBlock( -width+4+X,  param.Y_SEA+13, -width+5+Z,    param.FENCE      )
    mc.setBlock( -width+4+X,  param.Y_SEA+14, -width+5+Z,    param.TORCH      )
    mc.setBlocks(-width+5+X,  param.Y_SEA+10, -width+12+Z,  -width+5+X,  param.Y_SEA+15, -width+12+Z,  param.DARK       )
    mc.setBlock( -width+4+X,  param.Y_SEA+13, -width+12+Z,  param.FENCE      )
    mc.setBlock( -width+4+X,  param.Y_SEA+14, -width+12+Z,  param.TORCH      )
    mc.setBlocks(-width+5+X,  param.Y_SEA+10, Z,            -width+5+X,  param.Y_SEA+15, Z,            param.DARK       )
    mc.setBlock( -width+4+X,  param.Y_SEA+13, Z,            param.FENCE      )
    mc.setBlock( -width+4+X,  param.Y_SEA+14, Z,            param.TORCH      )
    mc.setBlocks(-width+5+X,  param.Y_SEA+10, -width+28+Z,  -width+5+X,  param.Y_SEA+15, -width+28+Z,  param.DARK       )
    mc.setBlock( -width+4+X,  param.Y_SEA+13, -width+28+Z,  param.FENCE      )
    mc.setBlock( -width+4+X,  param.Y_SEA+14, -width+28+Z,  param.TORCH      )
    mc.setBlocks(-width+5+X,  param.Y_SEA+10, width-5+Z,    -width+5+X,  param.Y_SEA+15, width-5+Z,    param.DARK       )
    mc.setBlock( -width+4+X,  param.Y_SEA+13, width-5+Z,    param.FENCE      )
    mc.setBlock( -width+4+X,  param.Y_SEA+14, width-5+Z,    param.TORCH      )
    mc.setBlock( -width+5+X,  param.Y_SEA+13, width-4+Z,    param.FENCE      )
    mc.setBlock( -width+5+X,  param.Y_SEA+14, width-4+Z,    param.TORCH      )
    mc.setBlocks(-width+12+X, param.Y_SEA+10, width-5+Z,    -width+12+X, param.Y_SEA+15, width-5+Z,    param.DARK       )
    mc.setBlock( -width+12+X, param.Y_SEA+13, width-4+Z,    param.FENCE      )
    mc.setBlock( -width+12+X, param.Y_SEA+14, width-4+Z,    param.TORCH      )
    mc.setBlocks(X,           param.Y_SEA+10, width-5+Z,    X,           param.Y_SEA+15, width-5+Z,    param.DARK       )
    mc.setBlock( X,           param.Y_SEA+13, width-4+Z,    param.FENCE      )
    mc.setBlock( X,           param.Y_SEA+14, width-4+Z,    param.TORCH      )
    mc.setBlocks(-width+28+X, param.Y_SEA+10, width-5+Z,    -width+28+X, param.Y_SEA+15, width-5+Z,    param.DARK       )
    mc.setBlock( -width+28+X, param.Y_SEA+13, width-4+Z,    param.FENCE      )
    mc.setBlock( -width+28+X, param.Y_SEA+14, width-4+Z,    param.TORCH      )
    mc.setBlocks(width-5+X,   param.Y_SEA+10, width-5+Z,    width-5+X,   param.Y_SEA+15, width-5+Z,    param.DARK       )
    mc.setBlock( width-5+X,   param.Y_SEA+13, width-4+Z,    param.FENCE      )
    mc.setBlock( width-5+X,   param.Y_SEA+14, width-4+Z,    param.TORCH      )
    mc.setBlock( width-4+X,   param.Y_SEA+13, width-5+Z,    param.FENCE      )
    mc.setBlock( width-4+X,   param.Y_SEA+14, width-5+Z,    param.TORCH      )
    mc.setBlocks(width-5+X,   param.Y_SEA+10, width-12+Z,   width-5+X,   param.Y_SEA+15, width-12+Z,   param.DARK       )
    mc.setBlock( width-4+X,   param.Y_SEA+13, width-12+Z,   param.FENCE      )
    mc.setBlock( width-4+X,   param.Y_SEA+14, width-12+Z,   param.TORCH      )
    mc.setBlocks(width-5+X,   param.Y_SEA+10, Z,            width-5+X,   param.Y_SEA+15, Z,            param.DARK       )
    mc.setBlock( width-4+X,   param.Y_SEA+13, Z,            param.FENCE      )
    mc.setBlock( width-4+X,   param.Y_SEA+14, Z,            param.TORCH      )
    mc.setBlocks(width-5+X,   param.Y_SEA+10, width-28+Z,   width-5+X,   param.Y_SEA+15, width-28+Z,   param.DARK       )
    mc.setBlock( width-4+X,   param.Y_SEA+13, width-28+Z,   param.FENCE      )
    mc.setBlock( width-4+X,   param.Y_SEA+14, width-28+Z,   param.TORCH      )
    mc.setBlock( width-5+X,   param.Y_SEA+13, width-29+Z,   param.FENCE      )
    mc.setBlock( width-5+X,   param.Y_SEA+14, width-29+Z,   param.TORCH      )
    mc.setBlocks(width-15+X,  param.Y_SEA+10, width-28+Z,   width-15+X,  param.Y_SEA+15, width-28+Z,   param.DARK       )
    mc.setBlock( width-15+X,  param.Y_SEA+13, width-29+Z,   param.FENCE      )
    mc.setBlock( width-15+X,  param.Y_SEA+14, width-29+Z,   param.TORCH      )
    mc.setBlocks(width-24+X,  param.Y_SEA+10, width-28+Z,   width-24+X,  param.Y_SEA+15, width-28+Z,   param.DARK       )
    mc.setBlocks(width-25+X,  param.Y_SEA+10, width-29+Z,   width-25+X,  param.Y_SEA+15, width-29+Z,   param.DARK       )
    mc.setBlock( width-24+X,  param.Y_SEA+13, width-29+Z,   param.FENCE      )
    mc.setBlock( width-24+X,  param.Y_SEA+14, width-29+Z,   param.TORCH      )
    mc.setBlocks(width-25+X,  param.Y_SEA+10, -width+5+Z,   width-25+X,  param.Y_SEA+15, -width+5+Z,   param.DARK       )    
    mc.setBlock( width-25+X,  param.Y_SEA+13, -width+4+Z,   param.FENCE      )
    mc.setBlock( width-25+X,  param.Y_SEA+14, -width+4+Z,   param.TORCH      )
    mc.setBlock( width-24+X,  param.Y_SEA+13, -width+5+Z,   param.FENCE      )
    mc.setBlock( width-24+X,  param.Y_SEA+14, -width+5+Z,   param.TORCH      )
    mc.setBlocks(-width+5+X,  param.Y_SEA+10, -width+5+Z,   -width+5+X,  param.Y_SEA+15, -width+5+Z,   param.DARK       )
    mc.setBlock( -width+5+X,  param.Y_SEA+13, -width+4+Z,   param.FENCE      )
    mc.setBlock( -width+5+X,  param.Y_SEA+14, -width+4+Z,   param.TORCH      )
    mc.setBlock( -width+4+X,  param.Y_SEA+13, -width+5+Z,   param.FENCE      )
    mc.setBlock( -width+4+X,  param.Y_SEA+14, -width+5+Z,   param.TORCH      )
    mc.setBlocks(-width+3+X,  param.Y_SEA+16, -width+3+Z,   width-3+X,   param.Y_SEA+16, width-3+X,    param.GOLD_BLOCK )
    mc.setBlocks(-width+1+X,  param.Y_SEA+17, -width+1+Z,   width-1+X,   param.Y_SEA+17, width-1+Z,    param.NETHERITE  )
    mc.setBlocks(-width+4+X,  param.Y_SEA+18, -width+4+Z,   width-4+X,   param.Y_SEA+18, width-4+Z,    param.NETHERITE  )
    mc.setBlocks(-width+6+X,  param.Y_SEA+19, -width+6+Z,   width-6+X,   param.Y_SEA+19, width-6+Z,    param.NETHERITE  )
    mc.setBlocks(-width+7+X,  param.Y_SEA+20, -width+7+Z,   width-7+X,   param.Y_SEA+20, width-7+Z,    param.GOLD_BLOCK )
    mc.setBlock( -width+1+X,  param.Y_SEA+16, -width+1+Z,   param.LANTERN )
    mc.setBlock( width-1+X,   param.Y_SEA+16, -width+1+Z,   param.LANTERN )
    mc.setBlock( -width+1+X,  param.Y_SEA+16, width-1+Z,    param.LANTERN )
    mc.setBlock( width-1+X,   param.Y_SEA+16, width-1+Z,    param.LANTERN )
    mc.setBlocks(-width+7+X,  param.Y_SEA+21, -width+7+Z,   width-7+X,   param.Y_SEA+21, width-7+Z,    param.FENCE      )
    mc.setBlocks(-width+8+X,  param.Y_SEA+21, -width+8+Z,   width-8+X,   param.Y_SEA+21, width-8+Z,    param.AIR        )
    mc.setBlocks(-width+10+X, param.Y_SEA+21, -width+10+Z,  width-10+X,  param.Y_SEA+24, width-10+Z,   param.GOLD_BLOCK )
    mc.setBlocks(-width+10+X, param.Y_SEA+23, -width+10+Z,  width-10+X,  param.Y_SEA+23, width-10+Z,   param.DARK       )
    mc.setBlocks(-width+10+X, param.Y_SEA+25, -width+10+Z,  width-10+X,  param.Y_SEA+25, width-10+Z,   param.DARK       )
    mc.setBlocks(-width+11+X, param.Y_SEA+21, -width+11+Z,  width-11+X,  param.Y_SEA+24, width-11+Z,   param.AIR        )
    mc.setBlocks(-width+11+X, param.Y_SEA+25, -width+11+Z,  width-11+X,  param.Y_SEA+25, width-11+Z,   param.GLOWSTONE  )

if __name__ == "__main__":
    mc = Minecraft.create(port=param.PORT_MC)
    
    mc.postToChat("I`m going to bulit Kinkakuji!")
    sleep(1)
    Kinkakuji(mc, width=20, X=0, Z=0)
