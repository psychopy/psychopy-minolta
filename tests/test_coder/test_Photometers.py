from psychopy import hardware, plugins
from psychopy_minolta.minolta import CS100A, LS100

plugins.activatePlugins()


def test_getPhotometers():
    """
    Test that Minolta photometers appear in getAllPhotometers once plugins are activated
    """
    # get all photometers
    photoms = hardware.getAllPhotometers()
    # make sure classes are present
    assert CS100A in photoms
    assert LS100 in photoms