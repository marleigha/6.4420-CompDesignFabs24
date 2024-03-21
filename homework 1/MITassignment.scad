
//radius = 10;
module hexagon(radius) {
    difference() {
        cylinder(r= radius, h = 3, $fn=6, center = true);
        cylinder(r= radius -1, h = 3.1, $fn=6, center = true);
    }
}



difference(){
    cylinder(r = 60, h = 10, center = true);
    cylinder(r = 58, h = 10.2, center = true);
}
  