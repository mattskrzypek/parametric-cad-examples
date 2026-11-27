"""Nominal drawing of the verification bracket; no manufacturing tolerance specified."""
from pathlib import Path
import cadgen
from cadgen.eng_drawing import Sheet, eng_drawing
from bracket import LENGTH, WIDTH, THICKNESS, UPRIGHT_HEIGHT, HOLE_DIAMETER, HOLE_PITCH

@eng_drawing(out='bracket_drawing.pdf')
def bracket_drawing():
    part = cadgen.read_step(Path(__file__).parent / 'bracket.step')
    sheet = Sheet('A3', scale=2, title='VALIDATION BRACKET', part_number='TEST-001', revision='A', material='UNSPECIFIED', notes=['NOMINAL DIMENSIONS. NOT A FLIGHT PART.'])
    top, front, right, iso = sheet.three_views(part, iso=True, gap=35)
    top.overall()
    top.dim(((LENGTH - HOLE_PITCH) / 2, 8, THICKNESS), ((LENGTH + HOLE_PITCH) / 2, 8, THICKNESS))
    top.hole((25, 8, THICKNESS), HOLE_DIAMETER, thru=True, count=2, angle=0)
    front.overall()
    right.overall()
    return sheet

if __name__ == '__main__':
    bracket_drawing()
