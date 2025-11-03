"""
Utility functions for the Star Citizen Player Journal
"""

from datetime import datetime
from typing import Any, Dict
import json


def format_currency(amount: float) -> str:
    """
    Format currency amount in aUEC
    
    Args:
        amount: Amount to format
        
    Returns:
        Formatted currency string
    """
    return f"{amount:,.2f} aUEC"


def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Format datetime object to string
    
    Args:
        dt: Datetime object to format
        format_str: Format string (default: YYYY-MM-DD HH:MM:SS)
        
    Returns:
        Formatted datetime string
    """
    return dt.strftime(format_str)


def parse_datetime(dt_str: str, format_str: str = "%Y-%m-%d %H:%M:%S") -> datetime:
    """
    Parse datetime string to datetime object
    
    Args:
        dt_str: Datetime string to parse
        format_str: Format string (default: YYYY-MM-DD HH:MM:SS)
        
    Returns:
        Datetime object
    """
    return datetime.strptime(dt_str, format_str)


def save_json(data: Dict[str, Any], filename: str) -> None:
    """
    Save data to JSON file
    
    Args:
        data: Data to save
        filename: Path to save file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(filename: str) -> Dict[str, Any]:
    """
    Load data from JSON file
    
    Args:
        filename: Path to load file
        
    Returns:
        Loaded data
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def validate_ship_name(ship: str) -> bool:
    """
    Validate ship name (basic validation)
    
    Args:
        ship: Ship name to validate
        
    Returns:
        True if valid, False otherwise
    """
    return bool(ship and len(ship.strip()) > 0)


def validate_location(location: str) -> bool:
    """
    Validate location name (basic validation)
    
    Args:
        location: Location name to validate
        
    Returns:
        True if valid, False otherwise
    """
    return bool(location and len(location.strip()) > 0)
