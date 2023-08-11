from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

def Sentaku():
    mc.postToChat("どれを選びますか？下の中から一つ選んでクリックしてね。")

def Kinkakuji(mc, width=20):
    mc.setBlocks(-width,   param.Y_SEA+1,   -width,      width,     param.Y_SEA+1, width,    param.HARF_STONE)
    mc.setBlocks(-width+1, param.Y_SEA+1,   -width+1,    width-1,   param.Y_SEA+1, width-1,  param.STONE     )
    mc.setBlocks(-width+2, param.Y_SEA+2,   -width+2,    -width+3,  param.Y_SEA+2, width-2,  param.FENCE     )
    mc.setBlocks(-width+3, param.Y_SEA+2,   -width+3,    -width+3,  param.Y_SEA+2, width-3,  param.AIR       )

if __name__ == "__main__":
    mc = Minecraft.create(port=param.PORT_MC)
    
    Kinkakuji(mc, width=20)