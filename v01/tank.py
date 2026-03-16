from parameters import EngineParameters

def get_tank_pressure(t: float, params:EngineParameters) -> float:
    # v01: constant pressure model
    return params.tank_pressure_Pa

def get_fuel_pressure(t: float, params:EngineParameters) -> float:
    tank_p = get_tank_pressure(t, params)
    return max(tank_p - params.piston_pressure_loss_Pa, 0.0)


