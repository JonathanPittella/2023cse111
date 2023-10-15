from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
from pytest import approx
import pytest 
 
def test_water_column_height():
    assert water_column_height(0, 0) == approx(0, abs=1e-6)
    assert water_column_height(0, 10) == approx(7.5, abs=1e-6)
    assert water_column_height(25, 0) == approx(25, abs=1e-6)
    assert water_column_height(48.3, 12.8) == approx(57.9, abs=1e-6)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0) == approx(0, abs=1e-6)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=1e-3)
    assert pressure_gain_from_water_height(50) == approx(489.450, abs=1e-3)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.018, 1.75, 0) == approx(0, abs=1e-6)
    assert pressure_loss_from_pipe(0.048692, 0, 1.75, 200) == approx(0, abs=1e-6)
    assert pressure_loss_from_pipe(0.048692, 0.018, 0, 200) == approx(0, abs=1e-6)
    assert pressure_loss_from_pipe(0.048692, 0.018, 200, 1.75) == approx(-113.008, abs=1e3)
    assert pressure_loss_from_pipe(0.048692, 0.018, 1.65, 200) == approx(-100.462, abs=1e3)
    assert pressure_loss_from_pipe(0.28687, 0.013, 1.65, 1000) == approx(-61.576, abs=1e3)
    assert pressure_loss_from_pipe(0.28687, 0.013, 1.65, 1800.75) == approx(-110.884, abs=1e3)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
