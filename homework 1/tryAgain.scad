// Function to create a single hexagon
module hexagon(side) {
    difference() {
        circle(r=side/2);
        circle(r=0.9*side/2);
    }
}

// Function to create a honeycomb recursively within a ring
module honeycomb_within_ring(side, depth, ring_radius) {
    if (depth == 0) {
        hexagon(side);
    } else {
        for (i = [0:5]) {
            angle = i * 60;
            x_offset = side * cos(angle);
            y_offset = side * sin(angle);
            // Calculate distance from origin
            distance = sqrt(x_offset^2 + y_offset^2);
            // Only proceed if within ring radius
            if (distance < ring_radius) {
                translate([x_offset, y_offset, 0])
                    honeycomb_within_ring(side, depth - 1, ring_radius);
            }
        }
    }
}

// Function to create a ring
module ring(inner_radius, outer_radius, thickness) {
    difference() {
        circle(r=outer_radius);
        circle(r=inner_radius);
        translate([0, 0, -thickness])
            cylinder(r=outer_radius, h=thickness);
    }
}

// Parameters
side_length = 10;
recursion_depth = 3;
ring_inner_radius = 20;
ring_outer_radius = 30;
ring_thickness = 5;

// Generate ring
ring(ring_inner_radius, ring_outer_radius, ring_thickness);

// Generate honeycomb within ring
translate([ring_outer_radius, ring_outer_radius, 0])
    honeycomb_within_ring(side_length, recursion_depth, ring_inner_radius - side_length/2);