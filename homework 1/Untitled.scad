




// Function to create a single hexagon
module hexagon(side) {
    difference() {
        cylinder(r= side, h = 3, $fn=6, center = true);
        cylinder(r= side -1, h = 3.1, $fn=6, center = true);
    }
}

// Parameters
side_length = 20;
recursion_depth = 4;
n = 5;


//honeycomb(side_length, recursion_depth);
//ring();

//intersection(){
//    circle(37);
//    honeycomb(side_length, n);    
//    }

//render()intersection(){
//    circle(35);
//    honeycomb(side_length, recursion_depth);
//}

render()ring();

module ring(){
difference(){
    cylinder(r = 37, h = 10, center = true);
    cylinder(r = 36, h = 10.2, center = true);
}
}


// The honeycomb shape that fills the inside of our ring
// you can change the size of the pentagons via their sidelengths
// and you can change the depth of the recursion process
module honeycomb(side, depth) {
    if (depth == 0) {
        hexagon(side);
    } else {
        for (i = [0:5]) {
            angle = i * 120;
            x_offset = side * cos(angle);
            y_offset = side * sin(angle);
            translate([x_offset, y_offset, 0])
                honeycomb(side, depth - 1);
        }
    }
}

//our final shape will have 3 parameters
// int size, for the sides of our 