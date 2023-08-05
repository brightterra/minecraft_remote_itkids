def get_building_data(x, y, z, x_range, y_range, z_range, output_path, get_blocks=None, ignore_blocks=None):
    """
    建造物をcsvデータとして出力する
    :param x: 建造物の角 x座標の最小値
    :param y: 建造物の角 y座標の最小値
    :param z: 建造物の角 z座標の最小値
    :param x_range: 建造物の大きさ x方向
    :param y_range: 建造物の大きさ y方向
    :param z_range: 建造物の大きさ z方向
    :param output_path: csvの出力先
    :param get_blocks: 取得するブロックの種類を限定する ブロックidのリスト
    :param ignore_blocks: 取得しないブロックの種類を指定する ブロックidのリスト
    :return:
    """

    out = [["x", "y", "z", "id", "data"]]
    for y_ in range(y_range):
        for x_ in range(x_range):
            for z_ in range(z_range):
                #ブロックデータの取得
                x_pos = x + x_
                y_pos = y + y_
                z_pos = z + z_
                block = mc.getBlockWithData(x_pos, y_pos, z_pos)
                #取得するブロックかどうかの判定
                if get_blocks is not None:
                    if judge_get_block(get_blocks, block) is False:
                        continue
                if ignore_blocks is not None:
                    if judge_ignore_block(ignore_blocks, block) is True:
                        continue
                out.append([x_, y_, z_, block.id, block.data])

    with open(output_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(out)


