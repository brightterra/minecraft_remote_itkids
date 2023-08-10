from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

def Sentaku():
    mc.postToChat("どれを選びますか？下の中から一つ選んでクリックしてね。")

def Kinkakuji(mc, width=80, width2=40):
    mc.setBlocks(-width,  param.Y_SEA,   -width,    width,  param.Y_SEA,   width,  param.AIR       )
    mc.setBlocks(-width,  param.Y_SEA,   -width,    width,  param.Y_SEA,   width,  param.WATER     )
    mc.setBlocks(-width2, param.Y_SEA,   -width2,   width2, param.Y_SEA,   width2, param.STONE     )
    mc.setBlocks(-width2, param.Y_SEA+1, -width2,   width2, param.Y_SEA+1, width2, param.HARF_STONE)

def Ginkakuji():
    mc.setBlocks


if __name__ == "__main__":
    mc = Minecraft.create(port=param.PORT_MC)
    
    Kinkakuji(mc, width=80)