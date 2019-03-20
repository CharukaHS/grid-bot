''' Filter and Draw lines '''
import time
import cv2

# Calculate gradient of each line, append it to List
# loop through lines, check for simmilar gradients
# if simmilar gradients found increase the frequency (f) of that line
# draw the most frequent on screen

# Currently app crash in draw()

def draw(img, lines):
    Time = time.time()
    filtteredLines = [] #[(x1,y1),(x2,y2),m,f]
    try:
        for line in lines:
            for x1, y1, x2, y2 in line:
                m = abs((y2-y1)/(x2-x1)) * 100 #find gradient

                if not filtteredLines:
                    filtteredLines.append([(x1, y1), (x2, y2), m, 1])

                for fLine in filtteredLines:
                    if fLine[2] + 2 > m > fLine[2] -2:
                        fLine[3] = fLine[3] + 1
                    else:
                        filtteredLines.append([(x1, y1), (x2, y2), m, 1])
        
        filtteredLines = []
        print(time.time() - Time)
        for line in filtteredLines:
            cv2.line(img, (line[0][0], line[0][1]), (line[1][0], line[1][1]), (255, 0, 0), 10)

    except:
        print('error')