from datetime import datetime, timedelta

# ============================================
# Flight Class
# ============================================

class Flight:
    """
    Represents a scheduled flight between two airports.
    """
    
    def __init__(self, date, origin, destination, plane):
        """
        Initialize a flight.
        
        Args:
            date: datetime object for flight date
            origin: Airport object (departure)
            destination: Airport object (arrival)
            plane: Airplane object assigned to this flight
        """
        self.date = date
        self.origin = origin
        self.destination = destination
        self.plane = plane
        
        # Generate ID: DESTINATION-AIRLINECODE-YYYYMMDD
        date_str = date.strftime("%Y%m%d")
        self.id = f"{destination.city}-{plane.company.id}-{date_str}"
    
    def take_off(self):
        """
        Remove plane from origin airport and update location.
        """
        # Remove plane from origin airport
        if self.plane in self.origin.planes:
            self.origin.planes.remove(self.plane)
        
        # Remove flight from origin's scheduled_departures
        if self in self.origin.scheduled_departures:
            self.origin.scheduled_departures.remove(self)
        
        print(f"Flight {self.id} taking off from {self.origin.city}")
    
    def land(self):
        """
        Add plane to destination airport and update location.
        """
        # Update plane's current location
        self.plane.current_location = self.destination
        
        # Add plane to destination airport
        if self.plane not in self.destination.planes:
            self.destination.planes.append(self.plane)
        
        # Remove flight from destination's scheduled_arrivals
        if self in self.destination.scheduled_arrivals:
            self.destination.scheduled_arrivals.remove(self)
        
        print(f"Flight {self.id} landed at {self.destination.city}")
    
    def __str__(self):
        return f"Flight {self.id}: {self.origin.city} -> {self.destination.city} on {self.date.strftime('%Y-%m-%d')}"
    
    def __repr__(self):
        return f"Flight({self.id})"


# ============================================
# Airplane Class
# ============================================

class Airplane:
    """
    Represents an airplane belonging to an airline.
    """
    
    def __init__(self, id, current_location, company):
        """
        Initialize an airplane.
        
        Args:
            id: Unique identifier (int)
            current_location: Airport where plane is currently located
            company: Airline this plane belongs to
        """
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = []  # Sorted list of future flights
        
        # Add plane to current airport and airline
        current_location.planes.append(self)
        company.planes.append(self)
    
    def fly(self, destination):
        """
        Make the airplane take off and land at destination if flight is scheduled.
        
        Args:
            destination: Airport object to fly to
        """
        # Find flight to this destination
        flight_to_take = None
        for flight in self.next_flights:
            if flight.destination == destination:
                flight_to_take = flight
                break
        
        if not flight_to_take:
            print(f"No scheduled flight to {destination.city} for plane {self.id}")
            return
        
        # Execute flight
        flight_to_take.take_off()
        flight_to_take.land()
        
        # Remove flight from next_flights
        self.next_flights.remove(flight_to_take)
    
    def location_on_date(self, date):
        """
        Determine where the plane will be on a specific date.
        
        Args:
            date: datetime object to check
        
        Returns:
            Airport where plane will be on this date
        """
        # Check if there's a flight on this date
        for flight in self.next_flights:
            if flight.date.date() == date.date():
                # Flight lands at destination on this date
                return flight.destination
        
        # No flight on this date, stays at current location
        return self.current_location
    
    def available_on_date(self, date, location):
        """
        Check if plane can fly from location on date.
        
        Args:
            date: datetime object
            location: Airport object
        
        Returns:
            True if plane is available, False otherwise
        """
        # Check if plane is at this location on this date
        plane_location = self.location_on_date(date)
        if plane_location != location:
            return False
        
        # Check if plane already has a flight on this date
        for flight in self.next_flights:
            if flight.date.date() == date.date():
                return False
        
        return True
    
    def add_flight(self, flight):
        """
        Add a flight to next_flights and keep sorted by date.
        """
        self.next_flights.append(flight)
        self.next_flights.sort(key=lambda f: f.date)
    
    def __str__(self):
        return f"Plane {self.id} ({self.company.name}) at {self.current_location.city}"
    
    def __repr__(self):
        return f"Airplane({self.id}, {self.company.id})"


# ============================================
# Airline Class
# ============================================

class Airline:
    """
    Represents an airline company.
    """
    
    def __init__(self, id, name):
        """
        Initialize an airline.
        
        Args:
            id: Two-letter code (str)
            name: Airline name (str)
        """
        self.id = id
        self.name = name
        self.planes = []  # List of Airplane objects
    
    def __str__(self):
        return f"{self.name} ({self.id}) - {len(self.planes)} planes"
    
    def __repr__(self):
        return f"Airline({self.id}, {self.name})"


# ============================================
# Airport Class
# ============================================

class Airport:
    """
    Represents an airport with scheduled flights.
    """
    
    def __init__(self, city):
        """
        Initialize an airport.
        
        Args:
            city: City code (str)
        """
        self.city = city
        self.planes = []  # Planes currently at this airport
        self.scheduled_departures = []  # Future flights from here
        self.scheduled_arrivals = []    # Future flights arriving here
    
    def schedule_flight(self, destination, flight_date, airline=None):
        """
        Schedule a flight to destination on given date.
        Finds available airplane and creates flight.
        
        Args:
            destination: Airport object
            flight_date: datetime object
            airline: Optional Airline to use
        """
        # Find available airplane
        available_plane = None
        
        # Check planes at this airport first
        for plane in self.planes:
            if plane.available_on_date(flight_date, self):
                if airline is None or plane.company == airline:
                    available_plane = plane
                    break
        
        # If no plane found at airport, check all airline planes
        if not available_plane and airline:
            for plane in airline.planes:
                if plane.available_on_date(flight_date, self):
                    available_plane = plane
                    break
        
        if not available_plane:
            print(f"No available plane for flight from {self.city} to {destination.city} on {flight_date.strftime('%Y-%m-%d')}")
            return None
        
        # Create flight
        flight = Flight(flight_date, self, destination, available_plane)
        
        # Add to plane's schedule
        available_plane.add_flight(flight)
        
        # Add to airports' schedules
        self.scheduled_departures.append(flight)
        self.scheduled_departures.sort(key=lambda f: f.date)
        
        destination.scheduled_arrivals.append(flight)
        destination.scheduled_arrivals.sort(key=lambda f: f.date)
        
        print(f"Scheduled: {flight}")
        return flight
    
    def info(self, start_date, end_date):
        """
        Display all scheduled departures between dates.
        
        Args:
            start_date: datetime object
            end_date: datetime object
        """
        print(f"\n{'='*60}")
        print(f"FLIGHTS FROM {self.city} ({start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')})")
        print(f"{'='*60}")
        
        found = False
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f"  {flight.date.strftime('%Y-%m-%d')}: {flight.id} -> {flight.destination.city}")
                found = True
        
        if not found:
            print("  No scheduled flights in this period.")
        
        print(f"{'='*60}")
    
    def __str__(self):
        return f"Airport {self.city} - {len(self.planes)} planes, {len(self.scheduled_departures)} departures, {len(self.scheduled_arrivals)} arrivals"
    
    def __repr__(self):
        return f"Airport({self.city})"


# ============================================
# Test Program
# ============================================

def test_air_management():
    """Test the air management system."""
    print("=" * 70)
    print("AIR TRAFFIC MANAGEMENT SYSTEM - TEST")
    print("=" * 70)
    
    # Create airlines
    print("\n--- Creating Airlines ---")
    el_al = Airline("LY", "El Al")
    delta = Airline("DL", "Delta Air Lines")
    print(f"Created: {el_al}")
    print(f"Created: {delta}")
    
    # Create airports
    print("\n--- Creating Airports ---")
    tlv = Airport("TLV")  # Tel Aviv
    jfk = Airport("JFK")  # New York
    lhr = Airport("LHR")  # London
    print(f"Created: {tlv}")
    print(f"Created: {jfk}")
    print(f"Created: {lhr}")
    
    # Create airplanes
    print("\n--- Creating Airplanes ---")
    plane1 = Airplane(101, tlv, el_al)
    plane2 = Airplane(102, tlv, el_al)
    plane3 = Airplane(201, jfk, delta)
    print(f"Created: {plane1}")
    print(f"Created: {plane2}")
    print(f"Created: {plane3}")
    
    # Schedule flights
    print("\n--- Scheduling Flights ---")
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    day_after = today + timedelta(days=2)
    
    # TLV to JFK flights
    flight1 = tlv.schedule_flight(jfk, tomorrow, el_al)
    flight2 = tlv.schedule_flight(jfk, day_after, el_al)
    
    # JFK to TLV return
    flight3 = jfk.schedule_flight(tlv, tomorrow + timedelta(days=1), el_al)
    
    # TLV to LHR
    flight4 = tlv.schedule_flight(lhr, tomorrow, el_al)
    
    # Display airport info
    print("\n--- Airport Information ---")
    tlv.info(today, day_after + timedelta(days=2))
    jfk.info(today, day_after + timedelta(days=2))
    
    # Test plane location
    print("\n--- Testing Plane Locations ---")
    print(f"Plane {plane1.id} location today: {plane1.current_location.city}")
    print(f"Plane {plane1.id} location tomorrow: {plane1.location_on_date(tomorrow).city}")
    
    # Test availability
    print("\n--- Testing Availability ---")
    print(f"Plane {plane1.id} available tomorrow at TLV: {plane1.available_on_date(tomorrow, tlv)}")
    print(f"Plane {plane1.id} available day after at TLV: {plane1.available_on_date(day_after, tlv)}")
    
    # Execute flight
    print("\n--- Executing Flight ---")
    if flight1:
        print(f"Before flight: Plane at {plane1.current_location.city}")
        plane1.fly(jfk)
        print(f"After flight: Plane at {plane1.current_location.city}")
    
    # Check updated schedules
    print("\n--- Updated Schedules ---")
    tlv.info(today, day_after + timedelta(days=2))
    jfk.info(today, day_after + timedelta(days=2))
    
    # Test location after flight
    print("\n--- Location After Flight ---")
    print(f"Plane {plane1.id} location tomorrow: {plane1.location_on_date(tomorrow).city}")
    print(f"Plane {plane1.id} location day after: {plane1.location_on_date(day_after).city}")
    
    # Final status
    print("\n--- Final Status ---")
    print(f"{tlv}")
    print(f"{jfk}")
    print(f"{lhr}")
    print(f"\n{el_al}")
    print(f"{delta}")
    
    print("\n" + "=" * 70)
    print("TEST COMPLETED SUCCESSFULLY")
    print("=" * 70)


# ============================================
# Main Execution
# ============================================

if __name__ == "__main__":
    test_air_management()