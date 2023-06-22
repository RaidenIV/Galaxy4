import pyqtgraph.opengl as gl
import numpy as np
from PyQt5.QtWidgets import QApplication
from pyqtgraph.Qt import QtGui, QtCore
import pygame
import os

# Create a 3D plot widget
app = QApplication([])
w = gl.GLViewWidget()
w.setGeometry(0, 0, 1920, 1080)
w.showFullScreen()
w.show()
w.setWindowTitle('Galaxy Scatterplot')

# Define the number of points to plot
n = 1000000

# Generate random x, y, and z coordinates for the points
x = np.random.normal(size=n)
y = np.random.normal(size=n)
z = np.random.normal(size=n)

# Calculate the distance of each point from the origin
r = np.sqrt(x**2 + y**2 + z**2)

# Define a colormap for the points
c = np.ones((n, 4))
c[:, 0] = r / np.max(r)
c[:, 1] = 0.1 * (1 - r / np.max(r))
c[:, 2] = 0.9 * (1 - r / np.max(r))
c[:, 3] = 1

# Create a scatterplot item and add it to the plot widget
sp = gl.GLScatterPlotItem(pos=np.column_stack((x, y, z)), size=1, color=c)
w.addItem(sp)

# Set the camera position and orientation
w.setCameraPosition(distance=50, elevation=25, azimuth=45)

delta = 0
d2 = 0

pygame.mixer.init()

# Load the audio file
sound = pygame.mixer.Sound("filepath")

# Start playback
sound.play()

counter = 0

def update():
    global delta, d2, x, y, z, counter
    delta += 0.0625
    d2 += 0.00125 # Demonstration speed is 0.0025
    sp.setData(pos=np.column_stack((x, y, z)))
    w.setCameraPosition(distance=d2, azimuth=delta)
    counter += 1

t = QtCore.QTimer()
t.timeout.connect(update)
t.start(17)

# Start the event loop
app.exec_()
