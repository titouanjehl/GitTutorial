import pytest


@pytest.fixture
def factorial_inputs_outputs():
    rtn = {
        'errors': [-1, 0.3],
        'tests': [
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24)
        ]}
    return rtn

def test_factorial(factorial_inputs_outputs):
    from mypackage.myfile import factorial
    for inp in factorial_inputs_outputs['errors']:
        msg = "n must be a positive integer"
        with pytest.raises(ValueError, match=msg):
            factorial(inp)

    for test in factorial_inputs_outputs['tests']:
        inp, oup = test
        assert oup == factorial(inp)
