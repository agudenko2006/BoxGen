#box dimensions
x, y, z = 80, 60, 20
#material
thickness = 2
sheet_y = 297
sheet_x = 210
#print settings
color = '#000' #outline color
line_width = .5

#necessary varibles
center_x = sheet_x/2
center_y = sheet_y/2
l = y/200 * 80

css = f'fill: none; stroke: {color}; stroke-width: {line_width}px;'

def rect(name, x, y, width, height):
    y *= -1
    x += center_x - width/2
    y += center_y - height/2
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" id="rect{name}" style="{css}"/>\n'

def trapezoid(name, x, y, width, height, l = thickness, r = thickness, mirror = False):
    y *= -1
    x += center_x - width/2
    y += center_y - height/2
    x1, x2, x3, x4 = x, x+l, x+ width-r, x+width
    y1, y2 = y, y+height
    if mirror:
        y1, y2 = y2, y1
    return f'<polygon points="{x2} {y1}, {x3} {y1}, {x4} {y2}, {x1} {y2}" id="poly{name}" style="{css}"/>\n'

if __name__ == '__main__':
    svg = f'<svg width="{sheet_x}mm" height="{sheet_y}mm" viewBox="0 0 {sheet_x} {sheet_y}">\n'
    svg += rect('center', 0, 0, x, y)
    svg += rect('right1', +x/2 +z*0.5 +thickness*2, 0, z, y)
    svg += rect('right2', +x/2 +z*1.5 +thickness*4, 0, z, y)
    svg += rect('left-1', -x/2 -z*0.5 -thickness*2, 0, z, y)
    svg += rect('left-2', -x/2 -z*1.5 -thickness*4, 0, z, y)
    svg += rect('top-1', 0, +y/2 +z/2 +thickness*2, x, z)
    svg += rect('corner1', -x/2 -l*0.5 -thickness, +y/2 +z/2 +thickness*2, l, z -thickness*2)
    svg += rect('corner2', +x/2 +l*0.5 +thickness, +y/2 +z/2 +thickness*2, l, z -thickness*2)
    svg += rect('bottom', 0, -y/2 -z/2 -thickness*2, x, z)
    svg += rect('corner3', -x/2 -l*0.5 -thickness, -y/2 -z/2 -thickness*2, l, z -thickness*2)
    svg += rect('corner4', +x/2 +l*0.5 +thickness, -y/2 -z/2 -thickness*2, l, z -thickness*2)
    svg += rect('lid', 0, +y +z +thickness*4, x, y)
    #svg += rect('lid-end', 0, +y*1.5 +z*1.5 +thickness*5, x+z, z -thickness*2)
    svg += trapezoid('lid-lock', 0, +y*1.5 +z*1.5 +thickness*5, x+z*2, z -thickness*2, z, z)
    svg += '</svg>'
    file = open('output.svg', 'w')
    file.write(svg)
    file.close()
