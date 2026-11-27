"""Parametric validation bracket in mm; nominal dimensions, no fit assumptions."""
from cadgen import build123d as bd
from cadgen import step, stl, threemf

LENGTH: float = 30.0
WIDTH: float = 20.0
THICKNESS: float = 3.0
UPRIGHT_HEIGHT: float = 15.0
HOLE_DIAMETER: float = 3.0
HOLE_PITCH: float = 20.0

@step(out='bracket.step')
@stl(out='bracket.stl')
@threemf(out='bracket.3mf')
def bracket():
    base = bd.Box(LENGTH, WIDTH, THICKNESS, align=(bd.Align.MIN, bd.Align.MIN, bd.Align.MIN))
    upright = bd.Pos(0, WIDTH - THICKNESS, 0) * bd.Box(LENGTH, THICKNESS, UPRIGHT_HEIGHT, align=(bd.Align.MIN, bd.Align.MIN, bd.Align.MIN))
    body = base + upright
    for x in ((LENGTH - HOLE_PITCH) / 2, (LENGTH + HOLE_PITCH) / 2):
        body = body - bd.Pos(x, 8, 0) * bd.Cylinder(HOLE_DIAMETER / 2, THICKNESS, align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN))
    body.label = 'validation-bracket'
    return body

if __name__ == '__main__':
    bracket()
