# Automatic Cockroach Killer 蟑．狼

* **成品影片連結**：
> https://youtu.be/eh25jqIfVpo

* **專題解說影片連結**：
> 待影片剪好再附上
<br>

* 本戰車為一台主動式滅蟑智慧戰車，主要功能如下：
1. 自動巡守家園並迴避障礙物
2. 自動追蹤並噴灑藥劑殺滅蟑螂
3. 回傳任務訊息給使用者的Line
<br>

* 硬體及戰車環境建置

本戰車為使用JetBot AI智能小車改裝而成，搭載Jetson nano 2GB 主板\
拖車部分為依需求自行設計紙模後，再請壓克力店製作出1:1的載具\
車體本體組裝及JetBot環境建置可參考：
> JetBot_Setup.txt 
<br> 

* 戰車驅動馬達測試
可參考JetBot環境建置後內附的程式碼：
> basic_motion.ipynb
<br>

* 噴射裝置測試
噴射裝置由酒精噴槍改裝而成，控制噴射馬達程式碼可參考：
> Spray.py
<br>

* 迴避障礙模型

依照JetBot GitHub提供兩種模型進行訓練並比較效能，擇優選擇了Alexnet
<br>

### 障礙迴避模型效能比較
|               |      Alexnet      |       Resnet18       |
|:-------------:|:-----------------:|:--------------------:|
| Test Accuracy |       98.4%       |         92.2%        |
| Training Time |      ~15 min      |        ~20 min       | 

<br>

* 蟑螂資料庫收集

使用JetBot AI Kit中附的控制器，搭配遠程遙控程式碼，透過戰車搭載的CSI相機獲取照片\
詳細程式碼可參考：
> Data Collection through Teleoperation.ipynb
<br>

* Yolov5環境建置

依照JetBot原始環境及Yolov5所需環境建置docker container在local host做訓練\
以下提供docker image供有需要的人下載：
> docker pull syax19/yolov5_jetbot
<br>

* Yolov5模型訓練

參考Yolov5官方GitHub：
> https://github.com/ultralytics/yolov5
<br>

* 分析Yolov5物體偵測後取得資料

> yolov5Dataform.ipynb
<br>

* 利用拍照計算戰車轉動角度，獲取之後調整物體追蹤的參數

> AngleCaculation.ipynb
<br>

* 使用line傳送任務訊息給用戶

> linebot.ipynb
<br>

* 執行蟑螂追蹤、噴灑藥劑、回傳任務訊息(因記憶體不足，此部分執行時使用Jetson nano 4GB主板)
> CockroachKiller.ipynb
<br>
