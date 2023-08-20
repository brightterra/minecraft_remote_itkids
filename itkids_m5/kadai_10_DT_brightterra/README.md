# マイクラ課題

動作環境
Minecraft Java版　1．16.5  
forge 36.2.39  
Remotecontrollermod 1.16.5_0.05  

9. 地面を平らにする
（yが63以上なら全部消す、yが62なら土になる、yが61以下なら全部石にする）
10. 地面を平らにして金閣寺っぽいものを作る
(変数XとZで、好きなところに建築することができる。大きさの変更はできない)
9以降がオリジナル(自分で作成したやつ)

original_10.pyについて　　
プログラムのうち、最後の部分のX座標とZ座標を、それぞれ、XとZに入れておくと、好きな場所で金閣寺を建築することができるようになる。

実際にはこうなります。
[<img src="2023-08-15_17.09.26.png" width="400" >](2023-08-15_17.09.26.png)

```minecraft
/tp 0 100 0
/time set day
/weather clear
```

```bash
cd itkids_m5/kadai_10_DT_brightterra
ls -la
python original_10.py
```

夜にしたい場合→マイクラのコマンドで時刻を設定してから実行する。

[<img src="2023-08-19_12.55.10.png" width="400" >](2023-08-19_12.55.10.png)

```minecraft
/tp 0 100 0
/time set night
/weather clear
```

```bash
cd itkids_m5/kadai_10_DT_brightterra
ls -la
python original_10.py
```

ジャングルの場合  
→①/locateコマンドを使って、ジャングルの寺院を探す。  
 ②そこの座標を調べて、プログラムの305行目に打ち込む。（コミットをする必要はない。）  
 ③実行する。  

[<img src="2023-08-19_12.40.50.png" width="400" >](2023-08-19_12.40.50.png)

```minecraft
/tp 3189 100 -1419
/time set day
/weather clear
```

```bash
cd itkids_m5/kadai_10_DT_brightterra
ls -la
python original_10.py
```