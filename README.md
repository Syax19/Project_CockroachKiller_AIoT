# Cockroach Killer 蟑．狼

* **成品影片連結**：
> 待影片剪好再附上

* **專題解說影片連結**：
> 待影片剪好再附上

* 本戰車為一主動式滅蟑智慧戰車，主要功能如下：
1. 自動巡守家園並迴避障礙物
2. 自動追蹤並噴灑藥劑殺滅蟑螂
3. 回傳任務訊息給使用者的Line

* 硬體及戰車環境建置
本戰車為使用JetBot AI智能小車改裝而成，搭載Jetson nano 2GB 主板\
拖車部分為依需求自行設計紙模後，再請壓克力店製作出1:1的載具\
車體本體組裝及JetBot環境建置可參考：
> JetBot_Setup.txt\


* 戰車驅動馬達測試
可參考JetBot環境建置後內附的程式碼：
> basic_motion.ipynb\


* 噴射裝置測試
噴射裝置由酒精噴槍改裝而成，控制噴射馬達程式碼可參考：
> Spray.py

\
* 迴避障礙模型
依照JetBot GitHub提供兩種模型進行訓練並比較效能，擇優選擇了Alexnet
### 障礙迴避模型效能比較
|               |      Alexnet      |       Resnet18       |
|:-------------:|:-----------------:|:--------------------:|
| Test Accuracy |       98.4%       |         92.2%        |
| Training Time |      ~15 min      |        ~20 min       | 

\
* 蟑螂資料庫收集
使用JetBot AI Kit中附的遙控器搭配遠程遙控程式碼透過戰車搭載的CSI相機獲取照片\
詳細程式碼可參考：
> Data Collection through Teleoperation.ipynb

* 



