#这是我学习python第二天的作业，编写此程序的初衷仅仅是为了实践教程
#所学内容。此命题是我自己根据所学想出来可以做到的效果。因为是初学者
#代码可能会很丑，请见谅。

import time
import random

print ("------------------------------------------------------")
print ("欢迎使用双色球选号器")
print ("------------------------------------------------------")
time.sleep(1)
print ("本工具用于以双色球规则生成6个红色球号码与1个蓝色球号码")
print ("------------------------------------------------------")
time.sleep(1)
print (" ")
print ("请选择要执行的任务：")
print ("1. 生成5组随机号码")
print ("2. 生成1组随机号码")
print ("3. 模拟投注器")
print (" ")
time.sleep(1)
selectnum = int (input("请输入任务编号：")) 
red_ball = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
blue_ball = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
if selectnum == 1:
    generate_r1 = random.sample(red_ball,6)
    generate_r2 = random.sample(red_ball,6)
    generate_r3 = random.sample(red_ball,6)
    generate_r4 = random.sample(red_ball,6)
    generate_r5 = random.sample(red_ball,6)
    generate_b1 = random.sample(blue_ball,1)
    generate_b2 = random.sample(blue_ball,1)
    generate_b3 = random.sample(blue_ball,1)
    generate_b4 = random.sample(blue_ball,1)
    generate_b5 = random.sample(blue_ball,1)
    print (" ")
    print ("------------------------------------------------------")
    print (" ")
    print (f"红色球：{generate_r1} - 蓝色球：{generate_b1}")
    print (f"红色球：{generate_r2} - 蓝色球：{generate_b2}")
    print (f"红色球：{generate_r3} - 蓝色球：{generate_b3}")
    print (f"红色球：{generate_r4} - 蓝色球：{generate_b4}")
    print (f"红色球：{generate_r5} - 蓝色球：{generate_b5}")
elif selectnum == 2:
    generate_r1 = random.sample(red_ball,6)
    generate_b1 = random.sample(blue_ball,1)
    print (" ")
    print ("------------------------------------------------------")
    print (" ")
    print (f"红色球：{generate_r1} - 蓝色球：{generate_b1}")
elif selectnum == 3:
    print ("功能正在开发中...")
else:
    print ("请输入要执行的任务对应数字，目前只开发了3个功能")


