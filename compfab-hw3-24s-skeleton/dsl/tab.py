from re import S
from turtle import width
#from types import NoneType
#from attr import s
import numpy as np
from typing import Optional, Union
from dataclasses import dataclass
from functools import cache
import svgwrite
from svgwrite.shapes import Polygon
from pathlib import Path


@dataclass
class Tab:
    """
    A structure that represents a tab and a bend with respect to the parent tab.

    Hint: See figure 2 on some guidance to what parameters need to be put here.
    """

    parent: Optional["Tab"]
    children: list["Tab"]
    # TODO 3.2: Add attributes as needed.
    height: float
    width: float
    offsetAngle: float

    #children specific
    #having issues with setting these to None in generate
    #parent tab! so we're commenting them out for now
    # side: int
    # offsetDist: float
    
    
    # def __init__(self, height: float, width: float, offsetAngle: float, children: list["Tab"] ):
    #     #attributes of all tabs
    #     self.height = height
    #     self.width = width
    #     self.offsetAngle = np.radians(offsetAngle)
    #     # attributes of children





    def __hash__(self):
        return id(self)

    @cache
    def compute_corner_points(self) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Computes the four corner points in 2D (2,) based on the attributes.

        Hint: You may want to specify the convention on how you order these points.
        Hint: You can call this function on the parent to help get started.
        """
        # TODO 3.2: Implement this function
        #had trouble working with the angles & such


        p3_x = self.width *np.cos(self.offsetAngle)
        p4_x = (p3_x - self.width) *np.cos(self.offsetAngle)

        p1 = np.array([0, 0])
        #p2 =  np.array([self.length, self.width])
        p2 =  np.array([self.height, p3_x])
        #p3 = np.array([p3_x, self.width])
        p3 = np.array([self.height, self.width])
        #p4 = np.array([p4_x, self.length])
        p4 =  np.array([p4_x, self.height])
        
        return p1, p2, p3, p4


        raise NotImplementedError()

    def compute_all_corner_points(self) -> list[tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]]:
        """
        Computes all four corner points of all tabs in the current subtree.
        """
        cps = [self.compute_corner_points()]
        for child in self.children:
            cps.extend(child.compute_all_corner_points())
        return cps


#h is the height
# w is the width
#ang is the angle of of the parent
def generate_root_tab(w, h, ang) -> Tab:
    """
    Generate a new parent tab
    """
    # TODO: 3.2: Update the arguments and implement this function.

    return Tab(parent= None, height= h, width= w, offsetAngle= ang, children= [])
    
    raise NotImplementedError()

# s is the side it's on
# off is the offset
# w is the width
#h is the height
#ang is the angle off of the parent

def generate_child_tab(parent: Tab, w, h, ang ) -> Tab:
    """
    Generate a child tab. Make sure to update the children of parent accordingly.
    """
    # TODO: 3.2: Update the arguments and implement this function.
    
    #having issues if i wanted to make all my designated parameters
    childTab = Tab(parent= parent, height= h, width= w, offsetAngle= ang, children= [])
    parent.children.append(childTab)
    return childTab
    raise NotImplementedError()


def draw_svg(root_tab: Tab, output: Union[str, Path], stroke_width: float = 1):
    cps = root_tab.compute_all_corner_points()
    points = np.array(cps).reshape(-1, 2)
    min_point = points.min(axis=0)  # (2,)
    max_point = points.max(axis=0)  # (2,)
    points -= min_point
    points += 2 * stroke_width
    size = max_point - min_point  # (2,)
    size += 4 * stroke_width
    rects = points.reshape(-1, 4, 2)

    dwg = svgwrite.Drawing(str(output), size=(size[0], size[1]), profile="tiny")

    for rect in rects:
        dwg.add(Polygon(rect, stroke="black", fill="lightgray", stroke_width=stroke_width))

    dwg.save()
