
//Parameters to modify
heightParam = 5;
sideParam = 15;
depthParam = 5;



module hexagon(side) {
    difference() {
        cylinder(r= side, h = 1, $fn=6, center = true);
        cylinder(r= side -2, h = 1.1, $fn=6, center = true);
    }
}
//Creates the outer ring we see in all the models
module outerRing(){
    difference(){
        cylinder(r= 37, h = heightParam, center = true);
        cylinder(r= 36, h = heightParam + 0.3, center = true);
    }
}
module honeycomb(side, depth) {
    if (depth == 0) {
        hexagon(side);
    } else {
        for (i = [0:5]) { //as we want to place a new hexagon on each side
            angle = i * 120; // 120 because of hexagon geometry
            x_offset = side * cos(angle);
            y_offset = side * sin(angle);
            translate([x_offset, y_offset, 0])
                honeycomb(side, depth - 1); // slowly decrease the depth via recursion
        }
    }
}



outerRing();

// in order for the honeycomb to be contained to the outerRing
// I constrained it in a circle that is about the size of the ring
intersection(){
   circle(36);
    honeycomb(sideParam, depthParam);
    }

 
