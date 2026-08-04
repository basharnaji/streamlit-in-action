from unit_config import unit_config
from result import Result
from typing import List

def list_quantities() -> List[str]:
    return list(unit_config.keys())

def list_units(quantity: str) -> List[str]:
    if quantity in unit_config:
        return list(unit_config[quantity].units.keys())
    return []

def convert_value(quantity_name: str, from_unit_name: str, to_unit_name: str, value: float) -> Result:
    if quantity_name not in unit_config:
        return Result(success=False, message=f"Quantity '{quantity_name}' not found.")
    
    quantity = unit_config[quantity_name]
    
    if from_unit_name not in quantity.units:
        return Result(success=False, message=f"Unit '{from_unit_name}' not found in quantity '{quantity_name}'.")
    
    if to_unit_name not in quantity.units:
        return Result(success=False, message=f"Unit '{to_unit_name}' not found in quantity '{quantity_name}'.")
    
    from_unit = quantity.units[from_unit_name]
    to_unit = quantity.units[to_unit_name]
    
    # Convert the value to the standard unit
    value_in_std_units = value * from_unit.value_in_std_units
    
    # Convert from standard unit to the target unit
    converted_value = value_in_std_units / to_unit.value_in_std_units
    
    return Result(from_unit, to_unit, value, converted_value)