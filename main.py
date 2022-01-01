#box dimensions
x, y, z = 60, 80, 20
#material
thickness = 2
sheet_x = 297
sheet_y = 210
#print settings
color = '#FFF' #outline color
line_width = .5

#necessary varibles
css = f'fill: none; stroke: {color}; stroke-width: {line_width}px;'
center_x = sheet_x/2
center_y = sheet_y/2

#it's actually a quadrilateral
def polygon(vert1, vert2, vert3, vert4, id = 0):
    x1, y1 = vert1
    x2, y2 = vert2
    x3, y3 = vert3
    x4, y4 = vert4
    return f'<polygon points="{x1} {y1}, {x2} {y2}, {x3} {y3}, {x4} {y4}" id="poly{id}" style="{css}"/>\n'

def rect(x, y, width, height, id = 0):
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" id="rect{id}" style="{css}"/>\n'

if __name__ == '__main__':
    svg = '<svg width="297mm" height="210mm" viewBox="0 0 297 210">\n'
    svg += rect(center_x - x/2, center_y - y/2, x, y) #center
    svg += '</svg>'
    print(svg)
    file = open('output.svg', 'w')
    file.write(svg)
    file.close()
