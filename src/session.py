"""
Session module for tracking individual gameplay sessions
"""

from datetime import datetime
from typing import Optional, List, Dict, Any


class Session:
    """Represents a single Star Citizen gameplay session"""
    
    def __init__(
        self,
        start_time: datetime,
        location: str = "",
        ship: str = "",
        end_time: Optional[datetime] = None
    ):
        """
        Initialize a new session
        
        Args:
            start_time: When the session started
            location: Starting location in the game
            ship: Ship being used
            end_time: When the session ended (optional)
        """
        self.start_time = start_time
        self.end_time = end_time
        self.location = location
        self.ship = ship
        self.activities: List[str] = []
        self.earnings: float = 0.0
        self.expenses: float = 0.0
        self.notes: str = ""
    
    def end_session(self, end_time: Optional[datetime] = None) -> None:
        """
        End the current session
        
        Args:
            end_time: When the session ended (defaults to now)
        """
        self.end_time = end_time or datetime.now()
    
    def add_activity(self, activity: str) -> None:
        """
        Add an activity to the session
        
        Args:
            activity: Description of the activity
        """
        self.activities.append(activity)
    
    def add_earnings(self, amount: float, description: str = "") -> None:
        """
        Add earnings to the session
        
        Args:
            amount: Amount earned
            description: Description of the earnings
        """
        self.earnings += amount
        if description:
            self.add_activity(f"Earned {amount} aUEC: {description}")
    
    def add_expense(self, amount: float, description: str = "") -> None:
        """
        Add an expense to the session
        
        Args:
            amount: Amount spent
            description: Description of the expense
        """
        self.expenses += amount
        if description:
            self.add_activity(f"Spent {amount} aUEC: {description}")
    
    def get_net_profit(self) -> float:
        """
        Calculate net profit for the session
        
        Returns:
            Net profit (earnings - expenses)
        """
        return self.earnings - self.expenses
    
    def get_duration(self) -> Optional[str]:
        """
        Get the duration of the session
        
        Returns:
            Formatted duration string or None if session hasn't ended
        """
        if not self.end_time:
            return None
        
        duration = self.end_time - self.start_time
        hours = int(duration.total_seconds() // 3600)
        minutes = int((duration.total_seconds() % 3600) // 60)
        
        return f"{hours}h {minutes}m"
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert session to dictionary
        
        Returns:
            Dictionary representation of the session
        """
        return {
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'location': self.location,
            'ship': self.ship,
            'activities': self.activities,
            'earnings': self.earnings,
            'expenses': self.expenses,
            'net_profit': self.get_net_profit(),
            'notes': self.notes
        }
    
    def __str__(self) -> str:
        """String representation of the session"""
        duration = self.get_duration() or "In progress"
        return (
            f"Session on {self.start_time.strftime('%Y-%m-%d %H:%M')} "
            f"({duration}) - {self.ship} at {self.location}"
        )
    
    def __repr__(self) -> str:
        """Developer representation of the session"""
        return f"Session(start={self.start_time}, ship={self.ship}, location={self.location})"
