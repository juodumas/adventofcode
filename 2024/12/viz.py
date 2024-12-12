import os
from math import sqrt

style = [
    "body { font-family: monospace; font-size: 0; white-space: nowrap; background: #666; }",
    "table { border-spacing: 0; }",
    "td { font-family: monospace; font-size: 18px; padding: 0.2em; width: 1em; height: 1em; vertical-align: middle; text-align: center; }",
    "td > div { border:        2px solid transparent; }",
    ".right   { border-right:  2px solid black; }",
    ".bottom  { border-bottom: 2px solid black; }",
    ".left    { border-left:   2px solid black; }",
    ".top     { border-top:    2px solid black; }",
]
html = ["<!DOCTYPE html>\n<html><body>"]

dir_to_border = {1: "right", 1j: "bottom", -1: "left", -1j: "top"}


def viz(coords, data):
    h = s = l = 20
    colors = {}
    borders = {}
    plants = set(coords.values())
    for plant, perimeter in data:
        for c, d in perimeter:
            borders.setdefault(c, [])
            borders[c].append(dir_to_border[d])
        if plant not in colors:
            h += 255 // len(plants)
            s = s + 10 if s < 100 else 20
            l = l + 10 if l < 70 else 40
            colors[plant] = (h, s, l)
            style.append(f".{plant} {{ background: hsl({h}, {s}%, {l}%); }}")
    html.extend(("<style>", "\n".join(style), "</style><table><tr><td>"))
    sz = int(sqrt(len(coords)))
    for x in range(sz):
        html.append(f"<td>{x}")
    for y in range(sz):
        html.append(f"<tr><td>{y}j")
        for x in range(sz):
            plant = coords.get(x + 1j * y)
            classes = [border for border in borders.get(x + 1j * y, [])]
            if classes:
                classes.append("border")
            html.append(f'<td class="{plant}"><div class="{" ".join(classes)}">{plant}</div>')
    html.append("</table></body></html>")
    open(os.path.dirname(__file__) + os.path.sep + "viz.html", "w").write("\n".join(html))
