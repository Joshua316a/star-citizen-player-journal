"""
Journal module for managing gameplay sessions
"""

from typing import List, Dict, Any
from datetime import datetime, timedelta
from src.session import Session


class Journal:
    """Main journal class for tracking Star Citizen gameplay"""
    
    def __init__(self):
        """Initialize the journal"""
        self.sessions: List[Session] = []
    
    def add_session(self, session: Session) -> None:
        """
        Add a new session to the journal
        
        Args:
            session: Session object to add
        """
        self.sessions.append(session)
    
    def get_sessions(self, limit: int = None) -> List[Session]:
        """
        Get all sessions or a limited number of recent sessions
        
        Args:
            limit: Maximum number of sessions to return (most recent first)
            
        Returns:
            List of Session objects
        """
        if limit:
            return self.sessions[-limit:]
        return self.sessions
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Calculate and return gameplay statistics
        
        Returns:
            Dictionary containing various statistics
        """
        if not self.sessions:
            return {
                'total_sessions': 0,
                'total_playtime': '0h 0m',
                'most_used_ship': 'N/A'
            }
        
        # Calculate total playtime
        total_time = timedelta()
        ship_usage = {}
        
        for session in self.sessions:
            if session.end_time:
                duration = session.end_time - session.start_time
                total_time += duration
            
            # Track ship usage
            if session.ship:
                ship_usage[session.ship] = ship_usage.get(session.ship, 0) + 1
        
        # Find most used ship
        most_used_ship = max(ship_usage.items(), key=lambda x: x[1])[0] if ship_usage else 'N/A'
        
        # Format playtime
        hours = int(total_time.total_seconds() // 3600)
        minutes = int((total_time.total_seconds() % 3600) // 60)
        
        return {
            'total_sessions': len(self.sessions),
            'total_playtime': f'{hours}h {minutes}m',
            'most_used_ship': most_used_ship,
            'ship_usage': ship_usage
        }
    
    def save_to_file(self, filename: str) -> None:
        """
        Save journal data to a file
        
        Args:
            filename: Path to save file
        """
        # TODO: Implement file saving
        pass
    
    def load_from_file(self, filename: str) -> None:
        """
        Load journal data from a file
        
        Args:
            filename: Path to load file
        """
        # TODO: Implement file loading
        pass
