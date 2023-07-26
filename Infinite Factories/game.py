print ("Importing Libraries...")

import pygame
import math
import time
import random
import os
pygame.init()

notation = ["", "K", "M", "B", "T", "Qu", "Qn", "Sx", "Sp", "O", "N", "De", "UDe", "DDe", "TDe", "QuDe", "QnDe", "SxDe", "SpDe", "ODe", "NDe", "Vg"]

song_name = "goingfast.mp3"
song_path = os.path.join(os.path.dirname(__file__), song_name)

pygame.mixer.music.load(song_path)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

window = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Infinite Factories")

bgColor = (0, 16, 32)
gameFont = pygame.font.SysFont("Agency FB", 50)
smallFont = pygame.font.SysFont("Agency FB", 25)

points = 20
fps = 60
lastframe = time.time()
generation = 0
shop1 = 0
shop2 = 0
shop3 = 0
smoothfps = 60
lasttime = round(time.time()/10)
newss = 0
news = ["220 Lines of Code!", "hi :)", "asdfghjkl!!!", "why are you here", "fard", 'what are you even making? what even is a "point"?', "eh", "i don't know", "ZeroDivisionError: division by zero", '"siiiaaaaaaiifbbbbbbbbbbbbbfgs[]]]]]]]]]];;;;;;;;;;zzzzzzzqqqqqqqqqqq" -my cat', "11th news message!", "Breaking news: Nobody still knows what a point is supposed to be.", "😎 nooo my emoji isn't working :(", "the next peice of news is a lie!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "{} is a big number".format(points),"You matter! (unless you multiply yourself by c^2, then you energy)", "This sentence is false.", "{} total news messages".format(newss)]
currentNews = random.choice(news)
shop2show = False
shop3show = False

def text(textname, text, xpos, ypos, size):
    if size == 1:
        textname = gameFont.render(text, 1, (255,255,255))
    else:
        textname = smallFont.render(text, 1, (255,255,255))
    window.blit(textname, (xpos, ypos))

def mouseinside(rect):
    mousex, mousey = pygame.mouse.get_pos()
    return rect.left <= mousex <= rect.right and rect.top <= mousey <= rect.bottom

def notate(number):
    if number != 0:
        magnitude = math.floor(math.log(number, 1000))
        truncated = number/math.pow(1000, magnitude)
        if number >= 1000:
            return str(math.floor(truncated*10)/10) + notation[magnitude]
        else:
            return math.floor(number)
    else:
        return 0
    
shopitem1 = pygame.Rect(100, 200, 500, 100)
shopitem2 = pygame.Rect(100, 350, 500, 100)
shopitem3 = pygame.Rect(100, 500, 500, 100)

print("Loading Save...")

image_path = os.path.join(os.path.dirname(__file__), "icon.png")

icon = pygame.image.load(image_path)
pygame.display.set_icon(icon)

def read(line): #Code by GPT-3.5
    file_name = "save.txt"
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    with open(file_path, 'r') as file:
        lines = file.readlines()
        if 1 <= line <= len(lines):
            print(lines[line - 1])
            return lines[line - 1]
        else:
            return 0
    file.close

def write(line_number, new_content):
    file_name = "save.txt"
    file_path = os.path.join(os.path.dirname(__file__), file_name)

    with open(file_path, 'r') as file:
        lines = file.readlines()

    if 1 <= line_number <= len(lines):
        lines[line_number - 1] = str(new_content) + '\n'
        with open(file_path, 'w') as file:
            file.writelines(lines)
        print(f"Successfully wrote to line {line_number}.")
    else:
        print(f"Line {line_number} does not exist in the file.")
    file.close

points = float(read(1))
shop1 = int(read(2))
shop2 = int(read(3))
shop3 = int(read(4))

print ("Have Fun!")

running = True
while running: # Game Loop
    pygame.display.update()

    deltatime = time.time() - lastframe
    if deltatime != 0:
        fps = 1 / deltatime
    lastframe = time.time()
    if fps != 0:
        smoothfps += (fps-smoothfps)/fps

    if pygame.mouse.get_pressed()[0]:
        if not lastmouse:
            if mouseinside(shopitem1):
                if points >= 20:
                    points -= 20
                    shop1+=1
            elif mouseinside(shopitem2):
                if points >= 10000:
                    points -= 10000
                    shop2+=1
            elif mouseinside(shopitem3):
                if points >= 150000:
                    points -= 150000
                    shop3+=1
            lastmouse = True
    else:
        lastmouse = False

    points = points + (generation/10000)/(deltatime+0.01)

    window.fill(bgColor)
    if not mouseinside(shopitem1):
        pygame.draw.rect(window, (0, 55, 110), shopitem1) 
    else:
        pygame.draw.rect(window, (0, 27, 55), shopitem1)
    
    if shop2show:
        if not mouseinside(shopitem2):
            pygame.draw.rect(window, (0, 55, 110), shopitem2) 
        else:
            pygame.draw.rect(window, (0, 27, 55), shopitem2)

        pygame.draw.rect(window, (114, 147, 168), shopitem2, width=10)

        text("shop2Text", "Tier II Factory", 120, 355, 1)
        text("shop2Amount", "x" + str(shop2), 220, 410, 0)
        text("shop2Price", "10K Points", 120, 410, 0)

    if shop3show:
        if not mouseinside(shopitem3):
            pygame.draw.rect(window, (0, 55, 110), shopitem3) 
        else:
            pygame.draw.rect(window, (0, 27, 55), shopitem3)

        pygame.draw.rect(window, (114, 147, 168), shopitem3, width=10)

        text("shop3Text", "Tier III Factory", 120, 505, 1)
        text("shop3Amount", "x" + str(shop3), 220, 560, 0)
        text("shop3Price", "150K Points", 120, 560, 0)
    
    pygame.draw.rect(window, (114, 147, 168), shopitem1, width=10)

    if lasttime != round(time.time()/10):
        currentNews = random.choice(news)

        for i in range(1,4):
            write(i, "")
        write(1, points)
        write(2, shop1)
        write(3, shop2)
        write(4, shop3)

    lasttime = round(time.time()/10)

    if points >= 5000:
        shop2show = True
    
    if points >= 30000:
        shop3show = True

    text("pointsText", "Points: " + str(notate(points)), 100, 100, 1)
    text("speedText", "Generation: " + str(generation), 100, 150, 0)
    text("fpsText", "FPS: " + str(math.floor(smoothfps)), 25, 25, 0)

    text("shop1Text", "Tier I Factory", 120, 205, 1)
    text("shop1Amount", "x" + str(shop1), 220, 260, 0)
    text("shop1Price", "20 Points", 120, 260, 0)

    text("newsText", currentNews, 25, 50, 0)
    text("creditText", "Music by Cursedsnake", 25, 850, 0)

    generation = (shop1 + (shop2*20) + (shop3*400))

    newss = len(news)
    news[17] = "{} total news messages".format(newss)
    news[14] = "{} is a big number".format(notate(points))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            for i in range(1,4):
                write(i, "")
            write(1, points)
            write(2, shop1)
            write(3, shop2)
            write(4, shop3)
            running = False



pygame.quit()