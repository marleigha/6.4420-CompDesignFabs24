# An example script to use your DSL and compile to an SVG

from tab import Tab, generate_root_tab, generate_child_tab, draw_svg

root = generate_root_tab(500,500, (3.14/2))
child1 = generate_child_tab(root, 50, 30, 3.14/2)
child2 = generate_child_tab(root, 50, 30, 3.14/2)
child3 = generate_child_tab(root, 50, 5, 3.14/2)
child4 = generate_child_tab(root, 30, 440, 3.14/2)
child5 = generate_child_tab(child1, 30, 10, 3.14/2)
child6 = generate_child_tab(child3, 30, 30, 3.14/2)
child7 = generate_child_tab(child2, 30, 30, 3.14/2)
# child2 = generate_child_tab(root, ...)
# child3 = generate_child_tab(child1, ...)

draw_svg(root, "example.svg")