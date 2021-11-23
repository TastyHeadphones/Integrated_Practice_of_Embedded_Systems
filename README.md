# Integrated_Practice_of_Embedded_Systems
Atlas 200DK 嵌入式系统实验

2021年秋季课程大作业
基于串口的IM通信系统

## 使用方法
1.开启两个固定虚拟串口 /dev/ttyS10 , /dev/ttyS11

`bash socatopenport.sh`

2.分别在两个终端启动程序

`python3 main.py userinfo1.json`

`python3 main.py userinfo2.json`

3.在shell中输入信息即可发送