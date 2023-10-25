from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
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

def test_pressure_loss_from_fitting():
    assert pressure_loss_from_fittings(0, 3) == approx(0, abs=1e3)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0, abs=1e3)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=1e3)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=1e3)
    assert pressure_loss_from_fittings(1.75, 50 ) == approx(-0.306, abs=1e3)

def test_reynold_number():
    assert reynolds_number(0.048692, 0) == approx(0, abs=1e3)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1e1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1e1)
    assert reynolds_number(0.28687, 1.65) == approx(471729, abs=1e1)
    assert reynolds_number(0.28687, 1.75) == approx(500318, abs=1e1)

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692) == approx(0, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
