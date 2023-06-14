# Mofied from SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# 

import displayio
import terminalio
from adafruit_display_text import label
from adafruit_gizmo import tft_gizmo

# Create the TFT Gizmo display
display = tft_gizmo.TFT_Gizmo()

# Make the display context
splash = displayio.Group()
display.show(splash)

#Top red bar
color_bitmap = displayio.Bitmap(240, 100, 1). #create a box, 240 pixels wide, 100 pixels tall
color_palette = displayio.Palette(1). # add it to a palette
color_palette[0] = 0xFF0000  # Bright Red.  #change the color
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0) #setup a sprite to add it to the display, starting at the top left
splash.append(bg_sprite) #add to group to show on screen

#Draw bottom bar
bottom_bar = displayio.Bitmap(240,20,1)
bottom_pallete = displayio.Palette(1)
bottom_pallete[0] = 0xFF0000  #Red
bottom_sprite = displayio.TileGrid(bottom_bar, pixel_shader=bottom_pallete, x=0, y=220) #if the screen is 240 tall, this fills the bottom
splash.append(bottom_sprite)

#Draw white label background
label_bitmap = displayio.Bitmap(240,120,1)
label_pallete = displayio.Palette(1)
label_pallete[0] = 0xFFFFFF   #White
label_sprite = displayio.TileGrid(label_bitmap, pixel_shader=label_pallete, x=0,y=100)
splash.append(label_sprite)

# Draw the first line label
text_group = displayio.Group(scale=2, x=65, y=25)
text = "Hello, My"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF)
text_group.append(text_area)  # Subgroup for text scaling

#draw the 2nd line
text_group2 = displayio.Group(scale=2,x=80, y=60)
text2 = "Name Is"
text_area2 = label.Label(terminalio.FONT, text=text2, color=0xFFFFFF)
text_group2.append(text_area2)

#now show them
splash.append(text_group)
splash.append(text_group2)

#Draw name
name_group = displayio.Group(scale=3, x=25, y=160)
myname = "HoustonGeek"
name_area = label.Label(terminalio.FONT, text=myname, color=0x000000)
name_group.append(name_area)
splash.append(name_group)

while True:
    pass
