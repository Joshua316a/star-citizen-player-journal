#!/usr/bin/env python3
"""
Star Citizen Player Journal
Main entry point for the application
"""

import sys
from datetime import datetime
from src.journal import Journal
from src.session import Session


def main():
    """Main application entry point"""
    print("=" * 50)
    print("Star Citizen Player Journal")
    print("=" * 50)
    print()
    
    journal = Journal()
    
    while True:
        print("\nOptions:")
        print("1. Start new session")
        print("2. View sessions")
        print("3. View statistics")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            start_session(journal)
        elif choice == "2":
            view_sessions(journal)
        elif choice == "3":
            view_statistics(journal)
        elif choice == "4":
            print("\nThank you for using Star Citizen Player Journal!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")


def start_session(journal):
    """Start a new gameplay session"""
    print("\n--- New Session ---")
    location = input("Starting location: ").strip()
    ship = input("Ship: ").strip()
    
    session = Session(
        start_time=datetime.now(),
        location=location,
        ship=ship
    )
    
    print(f"\nSession started at {session.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("Session tracking active...")
    
    # Add session to journal
    journal.add_session(session)


def view_sessions(journal):
    """View all recorded sessions"""
    print("\n--- Session History ---")
    sessions = journal.get_sessions()
    
    if not sessions:
        print("No sessions recorded yet.")
        return
    
    for i, session in enumerate(sessions, 1):
        print(f"\n{i}. {session}")


def view_statistics(journal):
    """View gameplay statistics"""
    print("\n--- Statistics ---")
    stats = journal.get_statistics()
    
    print(f"Total sessions: {stats.get('total_sessions', 0)}")
    print(f"Total playtime: {stats.get('total_playtime', 'N/A')}")
    print(f"Most used ship: {stats.get('most_used_ship', 'N/A')}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting... Goodbye!")
        sys.exit(0)
