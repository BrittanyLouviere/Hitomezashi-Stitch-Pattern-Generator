import random
from graphics import *

X_START = 200
X_END = 600
Y_START = 20
Y_END = 420

def drawAll(win, toDraw):
  for obj in reversed(toDraw):
    obj.draw(win)

def undrawAll(toUndraw):
  for obj in toUndraw:
    obj.undraw()

def getText(obj):
  return obj.getText()

def drawControls(win):
  toDraw = []

  toDraw.append(Text(Point(30, 30), "Width"))
  toDraw.append(Text(Point(30, 80), "Height"))
  toDraw.append(Text(Point(30, 130), "Prob X"))
  toDraw.append(Text(Point(30, 180), "Prob Y"))
  toDraw.append(Text(Point(75, 230), "Press Enter to"))
  toDraw.append(Text(Point(75, 250), "Generate Pattern"))

  width = Entry(Point(110, 30), 10)
  height = Entry(Point(110, 80), 10)
  probX = Entry(Point(110, 130), 10)
  probY = Entry(Point(110, 180), 10)
  toDraw.extend([width, height, probX, probY])
  width.setText("10")
  height.setText("10")
  probX.setText("50")
  probY.setText("50")

  rectangle = Rectangle(Point(X_START, Y_START), Point(X_END, Y_END))
  #rectangle.setOutline("light gray")
  toDraw.append(rectangle)

  drawAll(win, toDraw)
  return [width, height, probX, probY]

def drawStitches(win, stitches, controls):
  width, height, probX, probY = controls
  undrawAll(stitches)
  stitches = []

  #try:
  width = int(width)
  height = int(height)
  probX = float(probX)
  probY = float(probY)
  stitchSize = min((X_END-X_START)/width, (Y_END-Y_START)/height)

  # horizontal stitches
  startStitches = random.choices([True, False], weights=(probX, 100-probX), k=height)
  for y in range(height):
    startStitch = startStitches[y]
    for x in range(width):
      if startStitch:
        xStart = X_START + x * stitchSize
        xEnd = X_START + (x + 1) * stitchSize
        yStart = yEnd = Y_START + (stitchSize * y)
        stitches.append(Line(Point(xStart, yStart), Point(xEnd, yEnd)))
      startStitch = not startStitch

  # vertical stitches
  startStitches = random.choices([True, False], weights=(probY, 100-probY), k=width)
  for x in range(width):
    startStitch = startStitches[x]
    for y in range(height):
      if startStitch:
        yStart = Y_START + y * stitchSize
        yEnd = Y_START + (y + 1) * stitchSize
        xStart = xEnd = X_START + (stitchSize * x)
        stitches.append(Line(Point(xStart, yStart), Point(xEnd, yEnd)))
      startStitch = not startStitch

  drawAll(win, stitches)
    
  #except: pass

  return stitches

def main():
  random.seed()
  win = GraphWin("Hitomezashi Stitch Patterns", 650, 450)
  controls = drawControls(win)
  stitches = drawStitches(win, [], list(map(getText, controls)))

  while True:
    key = win.getKey()
    if key == "Return":
      stitches = drawStitches(win, stitches, list(map(getText, controls)))

main()