from turtle import color
from colorgram import extract
colors = extract('IntermediateProjects\Day17HirstPainting\FLumequine.jpg', 10)
color_list = []

for c in colors:
    
    color_list.append((c.rgb.r,c.rgb.g,c.rgb.b))
# removed white colors
color_list = [(239, 242, 247), (241, 228, 89), (24, 24, 61), (183, 73, 38), (144, 17, 31), (39, 29, 21), (214, 145, 85)]