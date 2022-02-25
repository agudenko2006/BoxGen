#box dimensions
x, y, z = 80, 60, 20
#material
thickness = 0
sheet_y = 297
sheet_x = 210

#print settings
color = '#000' #outline color
line_width = .5

#necessary varibles
center_x = sheet_x/2
center_y = sheet_y/2

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

def base():
    l = y/200 * 80
    svg  = rect('center', 0, 0, x, y)
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
    return svg

def lid():
    svg  = rect('lid', 0, +y +z +thickness*4, x, y)
    svg += trapezoid('lid-lock', 0, +y*1.5 +z*1.5 +thickness*5, x+z*2, z -thickness*2, z, z)
    return svg

def main():
    common_x = x + z*4 + thickness*12
    common_y = y*2 + z*3 +thickness*8
    global sheet_x, sheet_y, center_x, center_y
    if common_x > common_y:
        sheet_x, sheet_y = sheet_y, sheet_x
        center_x = sheet_x/2
        center_y = sheet_y/2
    center_y = sheet_y -y/2 -z -thickness*2 - 15
    if(common_y > sheet_y):
        return False
    if(common_x > sheet_x):
        return False
    svg = f'<svg width="{sheet_x}mm" height="{sheet_y}mm" viewBox="0 0 {sheet_x} {sheet_y}">\n'
    svg += base()
    svg += lid()
    svg += '</svg>'
    file = open('output.svg', 'w')
    file.write(svg)
    file.close()
    return True

if __name__ == '__main__':
    main()
