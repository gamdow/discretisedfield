from .mesh import Mesh
from .field import Field
from .read import read


def test():
    import pytest  # pragma: no cover
    pytest.main(["-v", "--pyargs", "discretisedfield"])  # pragma: no cover
