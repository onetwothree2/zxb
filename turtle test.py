import turtle,datetime
#绘制数码管间隔
def drawGap():
    turtle.penup()
    turtle.fd(5)
    
#绘制单段数码管
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)

#根据数字绘制单个数字对应的七段数码管    
def drawDigit(d):
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

#获得要输出的几个数字    
def drawDate(date):
    turtle.pencolor("blue")
    for i in range(date,-1,-1):
        num=str(i)
        for n in num:
            drawDigit(eval(n))
            turtle.clear()
            slen=len(num)
            #回退到原来的位置
            turtle.fd(-65*slen)
        
def main():
    turtle.setup(500,350,20,20)
    time=input("请输入倒计时的时间：")
    turtle.penup()
    turtle.fd(-50)
    turtle.pensize(5)
    drawDate(eval(time))
    turtle.hideturtle()
    
main()
