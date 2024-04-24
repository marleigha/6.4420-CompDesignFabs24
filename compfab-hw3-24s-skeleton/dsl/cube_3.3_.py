# An example script to use your DSL and compile to an SVG

from tab import Tab, generate_root_tab, generate_child_tab, draw_svg

root = generate_root_tab(500,500, (3.14/2))
child1 = generate_child_tab(root, 500, 500, 90)
child3 = generate_child_tab(root, 500, 500, 90)
child4 = generate_child_tab(root, 500, 500, 3.14/2)
child2 = generate_child_tab(child1, 500, 500, 90)
draw_svg(root, "cube.svg")