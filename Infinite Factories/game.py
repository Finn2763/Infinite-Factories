print ("Importing Libraries...")

import pygame
import math
import time
import random
import os
pygame.init()

def roundtonearest(rnd, number):
    return round(number/rnd)*rnd

displayInfo = pygame.display.Info()

def change_window_size(existing_surface, new_width, new_height):
    # Create a new display surface with the desired dimensions
    new_surface = pygame.display.set_mode((new_width, new_height), pygame.SCALED)
    
    # Copy the content from the old surface to the new one
    pygame.transform.scale(existing_surface, (new_width, new_height), new_surface)

notation = ["", "K", "M", "B", "T", "Qu", "Qn", "Sx", "Sp", "O", "N", "De", "UDe", "DDe", "TDe", "QuDe", "QnDe", "SxDe", "SpDe", "ODe", "NDe", "Vg"]

song_name = "goingfast.mp3"
song_path = os.path.join(os.path.dirname(__file__), song_name)

pygame.mixer.music.load(song_path)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

window = pygame.display.set_mode((displayInfo.current_w*0.9, displayInfo.current_h*0.8), pygame.SCALED)
pygame.display.set_caption("Infinite Factories")

bgColor = (0, 16, 32)
gameFont = pygame.font.SysFont("lucidasans", 50)
smallFont = pygame.font.SysFont("lucidasans", 25)

points = 20
fps = 60
lastframe = time.time()
generation = 0
shop1 = 0
shop2 = 0
shop3 = 0
shop4 = 0
shop5 = 0
shop6 = 0
shop7 = 0
shop8 = 0
smoothfps = 60
lasttime = round(time.time()/10)
newss = 0
news = ["430 Lines of Code!", "hi :)", "asdfghjkl!!!", "why are you here", "fard", 'what are you even making? what even is a "point"?', "eh", "i don't know", "ZeroDivisionError: division by zero", '"siiiaaaaaaiifbbbbbbbbbbbbbfgs[]]]]]]]]]];;;;;;;;;;zzzzzzzqqqqqqqqqqq" -my cat', "11th news message!", "Breaking news: Nobody still knows what a point is supposed to be.", "😎 nooo my emoji isn't working :(", "the next peice of news is a lie!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", "{} is a big number".format(points),"You matter! (unless you multiply yourself by c^2, then you energy)", "This sentence is false.", "{} total news messages".format(newss), "61726520796F75206C6F6F6B696E6720666F7220736563726574733F", "Each factory is 20x faster than the last"]
currentNews = random.choice(news)
shop2show = False
shop3show = False
shop4show = False
shop5show = False
shop6show = False
shop7show = False
shop8show = False
lastf11 = False
fullscreen = False

def text(textname, text, xpos, ypos, size):
    if size == 1:
        textname = gameFont.render(text, 1, (255,255,255))
    else:
        textname = smallFont.render(text, 1, (255,255,255))
    window.blit(textname, (xpos, ypos))

def colortext(textname, text, xpos, ypos, size, r, g, b):
    if size == 1:
        textname = gameFont.render(text, 1, (r,g,b))
    else:
        textname = smallFont.render(text, 1, (r,g,b))
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
shopitem4 = pygame.Rect(100, 650, 500, 100)
shopitem5 = pygame.Rect(600, 200, 500, 100)
shopitem6 = pygame.Rect(600, 350, 500, 100)
shopitem7 = pygame.Rect(600, 500, 500, 100)
shopitem8 = pygame.Rect(600, 650, 500, 100)
rebirthrect = pygame.Rect(600, 100, 500, 100)

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
    file.close

points = float(read(1))
shop1 = int(read(2))
shop2 = int(read(3))
shop3 = int(read(4))
shop4 = int(read(5))
shop5 = int(read(6))
shop6 = int(read(7))
shop7 = int(read(8))
shop8 = int(read(9))
rebirth = float(read(10))

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

    rbprice = rebirth*100000000000000

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
            elif mouseinside(shopitem4):
                if points >= 1000000:
                    points -= 1000000
                    shop4+=1
            elif mouseinside(shopitem5):
                if points >= 15000000:
                    points -= 15000000
                    shop5+=1
            elif mouseinside(shopitem6):
                if points >= 50000000:
                    points -= 50000000
                    shop6+=1
            elif mouseinside(shopitem7):
                if points >= 200000000:
                    points -= 200000000
                    shop7+=1
            elif mouseinside(shopitem8):
                if points >= 1000000000:
                    points -= 1000000000
                    shop8+=1
            elif mouseinside(rebirthrect):
                if points >= rbprice:
                    points = 20
                    generation = 0
                    shop1 = 0
                    shop2 = 0
                    shop3 = 0
                    shop4 = 0
                    shop5 = 0
                    shop6 = 0
                    shop7 = 0
                    shop8 = 0
                    shop2show = False
                    shop3show = False
                    shop4show = False
                    shop5show = False
                    shop6show = False
                    shop7show = False
                    shop8show = False
                    rebirth += 0.1
            lastmouse = True
    else:
        lastmouse = False

    points = points + ((generation*rebirth)/10000)/(deltatime+0.01)

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
        text("shop2Amount", "x" + str(shop2), 260, 410, 0)
        text("shop2Price", "10K Points", 120, 410, 0)

    if shop3show:
        if not mouseinside(shopitem3):
            pygame.draw.rect(window, (0, 55, 110), shopitem3) 
        else:
            pygame.draw.rect(window, (0, 27, 55), shopitem3)

        pygame.draw.rect(window, (114, 147, 168), shopitem3, width=10)

        text("shop3Text", "Tier III Factory", 120, 505, 1)
        text("shop3Amount", "x" + str(shop3), 280, 560, 0)
        text("shop3Price", "150K Points", 120, 560, 0)
    
    if shop4show:
        if not mouseinside(shopitem4):
            pygame.draw.rect(window, (0, 55, 110), shopitem4) 
        else:
            pygame.draw.rect(window, (0, 27, 55), shopitem4)

        pygame.draw.rect(window, (114, 147, 168), shopitem4, width=10)

        text("shop4Text", "Tier IV Factory", 120, 655, 1)
        text("shop4Amount", "x" + str(shop4), 260, 710, 0)
        text("shop4Price", "1M Points", 120, 710, 0)

    if shop5show:
        if not mouseinside(shopitem5):
            pygame.draw.rect(window, (0, 55, 110), shopitem5) 
        else:
            pygame.draw.rect(window, (0, 27, 55), shopitem5)

        pygame.draw.rect(window, (114, 147, 168), shopitem5, width=10)

        text("shop1Text", "Tier V Factory", 620, 205, 1)
        text("shop1Amount", "x" + str(shop5), 760, 260, 0)
        text("shop1Price", "15M Points", 620, 260, 0)

    if shop6show:
        if not mouseinside(shopitem6):
            pygame.draw.rect(window, (0, 55, 110), shopitem6) 
        else:
            pygame.draw.rect(window, (0, 27, 55), shopitem6)

        pygame.draw.rect(window, (114, 147, 168), shopitem6, width=10)

        text("shop2Text", "Tier VI Factory", 620, 355, 1)
        text("shop2Amount", "x" + str(shop6), 760, 410, 0)
        text("shop2Price", "50M Points", 620, 410, 0)
    
    if shop7show:
        if not mouseinside(shopitem7):
            pygame.draw.rect(window, (0, 55, 110), shopitem7) 
        else:
            pygame.draw.rect(window, (0, 27, 55), shopitem7)

        pygame.draw.rect(window, (114, 147, 168), shopitem7, width=10)

        text("shop3Text", "Tier VII Factory", 620, 505, 1)
        text("shop3Amount", "x" + str(shop7), 780, 560, 0)
        text("shop3Price", "200M Points", 620, 560, 0)

    if shop8show:
        if not mouseinside(shopitem8):
            pygame.draw.rect(window, (0, 55, 110), shopitem8) 
        else:
            pygame.draw.rect(window, (0, 27, 55), shopitem8)

        pygame.draw.rect(window, (114, 147, 168), shopitem8, width=10)

        text("shop4Text", "Tier VIII Factory", 620, 655, 1)
        text("shop4Amount", "x" + str(shop8), 740, 710, 0)
        text("shop4Price", "1B Points", 620, 710, 0)
    
    if shop8 > 0:
        if not mouseinside(rebirthrect):
            pygame.draw.rect(window, (196, 189, 109), rebirthrect) 
        else:
            pygame.draw.rect(window, (99, 96, 0), rebirthrect)

        pygame.draw.rect(window, (237, 228, 132), rebirthrect, width=10)

        text("rebirthButtonText", "Rebirth", 620, 100, 1)
        text("rebirthPrice", notate(rbprice) + "  x" + str(rebirth), 620, 155, 0)
    else:
        colortext("rebirthText", "Rebirths: " + str(notate(round(((rebirth-1)*10)+0.1))), 600, 100, 1, 237, 228, 132)
        colortext("multiText", "Multiplier: " + "x" + str(round(rebirth, 1)), 600, 150, 0, 237, 228, 132)
    pygame.draw.rect(window, (114, 147, 168), shopitem1, width=10)

    if lasttime != round(time.time()/10):
        currentNews = random.choice(news)

        for i in range(1,4):
            write(i, "")
        write(1, points)
        write(2, shop1)
        write(3, shop2)
        write(4, shop3)
        write(5, shop4)
        write(6, shop5)
        write(7, shop6)
        write(8, shop7)
        write(9, shop8)
        write(10, rebirth)
        print("Game saved with {} points.".format(notate(points)))

    lasttime = round(time.time()/10)

    if pygame.key.get_focused():
        pygame.mixer.music.set_volume(0.3)
    else:
        pygame.mixer.music.set_volume(0)

    if points >= 1000:
        shop2show = True
    
    if points >= 15000:
        shop3show = True

    if points >= 100000:
        shop4show = True

    if points >= 1500000:
        shop5show = True
    
    if points >= 5000000:
        shop6show = True

    if points >= 20000000:
        shop7show = True

    if points >= 100000000:
        shop8show = True
    
    text("pointsText", "Points: " + str(notate(points)), 100, 100, 1)
    text("speedText", "Generation: " + str(notate(round(generation*rebirth))), 100, 150, 0)
    text("fpsText", "FPS: " + str(math.floor(smoothfps)), 25, 25, 0)

    text("shop1Text", "Tier I Factory", 120, 205, 1)
    text("shop1Amount", "x" + str(shop1), 245, 260, 0)
    text("shop1Price", "20 Points", 120, 260, 0)

    text("newsText", currentNews, 25, 50, 0)
    text("creditText", "Music by Cursedsnake", 25, pygame.display.get_window_size()[1]-50, 0)

    generation = (shop1 + (shop2*20) + (shop3*400) + (shop4*8000) + (shop5*160000) + (shop6*3200000) + (shop7*64000000) + (shop8*1280000000))

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
            write(5, shop4)
            write(6, shop5)
            write(7, shop6)
            write(8, shop7)
            write(9, shop8)
            write(10, rebirth)
            print("Game saved with {} points.".format(notate(points)))
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == 1073741892:
                change_window_size(window, displayInfo.current_w, displayInfo.current_h)
                pygame.display.toggle_fullscreen()
                fullscreen = not fullscreen
                if fullscreen == False:
                    change_window_size(window, displayInfo.current_w*0.9, displayInfo.current_h*0.8)
            if event.key == 27:
                for i in range(1,4):
                    write(i, "")
                write(1, points)
                write(2, shop1)
                write(3, shop2)
                write(4, shop3)
                write(5, shop4)
                write(6, shop5)
                write(7, shop6)
                write(8, shop7)
                write(9, shop8)
                write(10, rebirth)
                print("Game saved with {} points.".format(notate(points)))
                running = False
                
pygame.quit()
