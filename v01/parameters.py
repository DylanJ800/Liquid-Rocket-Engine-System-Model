from dataclasses import dataclass

@dataclass
class EngineParameters:
    # Geometry
    chamber_volume_m3: float = 0.025
    throat_area_m2: float = 1.0e-4

    # Chamber Thermodynamics
    chamber_temperature_K: float = 3000.0
    gas_constant_J_per_kgK:float = 300.0
    c_star_m_per_s: float = 1500.0

    # Injector Properties 
    cd_ox: float = 0.8
