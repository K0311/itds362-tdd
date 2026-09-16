from kitchen import Quantity


def test_multiplication():
    flour = Quantity(200)
    flour.times(3)
    assert flour.amount == 600
    
def test_multiplication_by_two():
    flour = Quantity(200)
    flour.times(2)
    assert flour.amount == 400

def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)

    assert flour.times(3).amount == 600
    assert flour.times(2).amount == 400