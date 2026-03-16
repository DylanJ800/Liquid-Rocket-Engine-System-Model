from parameters import EngineParameters

def valve_open_fraction(t: float, t_open: float, t_close: float) -> float:
    if t < t_open:
        return 0.0
    if t >= t_close:
        return 0.0
    return 1.0

def get_valve_states(t: float, params: EngineParameters) -> tuple[float, float]:
    ox_open = valve_open_fraction(t, params.t_open_ox_s, params.t_shutdown_s)
    fuel_open = valve_open_fraction(t, params.t_open_fuel_s, params.t_shutdown_s)
    return ox_open, fuel_open
