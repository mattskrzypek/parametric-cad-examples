"""Nominal 30 x 20 mm template with two diameter-3 holes 20 mm apart."""
from cadgen import build123d as bd
from cadgen import dxf

LENGTH: float = 30.0
WIDTH: float = 20.0
HOLE_DIAMETER: float = 3.0
HOLE_PITCH: float = 20.0

@dxf
def hole_template():
    with bd.BuildSketch() as drawing:
        bd.Rectangle(LENGTH, WIDTH)
        with bd.Locations((-HOLE_PITCH / 2, 0), (HOLE_PITCH / 2, 0)):
            bd.Circle(HOLE_DIAMETER / 2, mode=bd.Mode.SUBTRACT)
    return drawing.sketch

if __name__ == '__main__':
    hole_template()
