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
    cd_fuel: float = 0
    area_ox_m2: float = 0
    area_fuel_m2: float = 0

    # Fluid Properties 
    rho_ox_kg_m3: float = 0
    rho_fuel_kg_m3: float = 0


    # Feed Pressures 
    tank_pressure_Pa: float = 000
    piston_pressure_loss_Pa: float = 0

    # Timing 
    t_open_ox_s: float = 0
    t_open_fuel_s: float = 0
    t_shutdown_s: float = 0

