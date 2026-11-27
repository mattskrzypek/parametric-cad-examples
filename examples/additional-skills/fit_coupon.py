"""Experimental diametral allowances; no physical fit result is implied."""
from cadgen import build123d as bd
from cadgen import step, stl

NOMINAL_DIAMETER: float = 3.9
ALLOWANCES: tuple[float, ...] = (-0.2, -0.1, 0.0, 0.1, 0.2)
TILE_WIDTH: float = 10.0
HEIGHT: float = 3.0
PITCH: float = 12.0

@step
@stl
def fit_coupon():
    tiles: list[bd.Shape] = []
    for index, allowance in enumerate(ALLOWANCES):
        tile = bd.Box(TILE_WIDTH, TILE_WIDTH, HEIGHT, align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN))
        bore = bd.Cylinder((NOMINAL_DIAMETER + allowance) / 2, HEIGHT, align=(bd.Align.CENTER, bd.Align.CENTER, bd.Align.MIN))
        tiles.append(bd.Pos(index * PITCH, 0, 0) * (tile - bore))
    return bd.Compound(children=tiles)

if __name__ == '__main__':
    fit_coupon()
