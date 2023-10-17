import pytest
from utils import certificate

claw = {
    1: [2],
    2: [1, 3, 4],
    3: [2],
    4: [2]
}

wheel = {
    1: [2, 6, 7],
    2: [1, 3, 7],
    3: [2, 4, 7],
    4: [3, 5, 7],
    5: [4, 6, 7],
    6: [1, 5, 7],
    7: [1, 2, 3, 4, 5, 6],
}

disconnected = {
    1: [2],
    2: [1],
    3: [4, 5],
    4: [3, 5],
    5: [3, 4]
}

@pytest.mark.parametrize("graph, cert", [
    (wheel, [1,2,3,4,5]),
    (wheel, [7,2,5]),
    (claw, [1,2,4])
])
def test_is_valid(graph, cert):
    assert certificate.validate(cert, graph)

@pytest.mark.parametrize("graph, cert", [
    (wheel, [1,2,3,4,5,6]),
    (wheel, [5,3]),
    (wheel, [1,7,1]),
    (wheel, [1,7,2,3]),
    (claw, [4,2,1,3]),
    (disconnected, [1,2,3,4,5])
])
def test_is_not_valid(graph, cert):
    assert not certificate.validate(cert, graph)

