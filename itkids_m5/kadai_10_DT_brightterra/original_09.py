

def get_building_data(x, y, z, x_range, y_range, z_range):
    """
    建造物をcsvデータとして出力する
    :param x: 建造物の角 x座標の最小値
    :param y: 建造物の角 y座標の最小値
    :param z: 建造物の角 z座標の最小値
    :param x_range: 建造物の大きさ x方向
    :param y_range: 建造物の大きさ y方向
    :param z_range: 建造物の大きさ z方向
    :return: out 座標とブロックデータのリスト[[x, y, z, id, data]]
    """
    out = [["x", "y", "z", "id", "data"]]
    for y_ in range(y_range):
        for x_ in range(x_range):
            for z_ in range(z_range):
                x_pos = x + x_
                y_pos = y + y_
                z_pos = z + z_
                block = mc.getBlockWithData(x_pos, y_pos, z_pos)
                out.append([x_, y_, z_, block.id, block.data])

    return out

# get_blocks = [[168, 0], [168, 1], [168, 2], [19, 1], [41, 0]]
# 168,0:海洋ブロック 168,1:海洋レンガ, 168,2:シーランタン
# 19,1:濡れたスポンジ, 41,0:金ブロック

def judge_get_block(get_blocks, target_block):
    """
    取得するブロックかどうかの判定
    :param get_blocks: 取得するブロックの種類を限定する ブロックid,dataのリスト
    :param target_block: minecraft内で配置されているブロック
    :return: target_blockがget_blocksに含まれているならTrue、含まれていないならFalse
    """
    for get_block in get_blocks:
        if get_block[0] == target_block.id and get_block[1] == target_block.data:
            return True
    return False

# ignore_blocks = [[8, 0], [13, 0], [12, 0], [16, 1], [15, 0]]
# 8,0:水 13,0:砂利, 12,0:砂
# 16,0:石炭鉱石, 15,0:鉄鉱石
