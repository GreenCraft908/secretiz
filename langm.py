#nếu bạn dc tôi gửi cho repository này là bạn là người được tôi chọn
#Để chạy code này trên android tải Pydroid3
#Để chạy code trên ios tải Python3IDE
import math 
from turtle import *
def hearta(k):
    return 12 * math.sin(k) ** 3
def heartb(k):
    return 12 * math.cos(k) - 5 * \
            math.cos(2 * k) - 2 * \
            math.cos(3 * k) - \
            math.cos(4 * k)
speed(5556000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i) * 20,heartb(i) * 20)
    for j in range(5):
        color("#ec03fc")
    goto(0,0)   
done()
