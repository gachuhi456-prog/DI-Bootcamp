# ============================================
# Part 1: Human and Queue Classes
# ============================================

class Human:
    """
    Represents a citizen waiting for vaccination.
    """
    
    BLOOD_TYPES = ["A", "B", "AB", "O"]
    
    def __init__(self, id_number, name, age, priority, blood_type):
        """
        Initialize a human.
        
        Args:
            id_number: Unique identifier (str)
            name: Person's name (str)
            age: Person's age (int)
            priority: Priority status (bool)
            blood_type: Blood type - must be A, B, AB, or O (str)
        """
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        
        if blood_type not in self.BLOOD_TYPES:
            raise ValueError(f"Invalid blood type: {blood_type}. Must be one of {self.BLOOD_TYPES}")
        self.blood_type = blood_type
        
        # Part 2: Family attribute
        self.family = []  # List of family members
    
    def add_family_member(self, person):
        """
        Add a person to this human's family and vice versa.
        
        Args:
            person: Another Human object
        """
        if person not in self.family:
            self.family.append(person)
        if self not in person.family:
            person.family.append(self)
    
    def __str__(self):
        priority_str = "PRIORITY" if self.priority else "normal"
        return f"{self.name} (ID: {self.id_number}, Age: {self.age}, Blood: {self.blood_type}, {priority_str})"
    
    def __repr__(self):
        return f"Human({self.id_number}, {self.name})"


class Queue:
    """
    Manages a queue of humans waiting for vaccination.
    """
    
    def __init__(self):
        """Initialize empty queue."""
        self.humans = []
    
    def add_person(self, person):
        """
        Add a human to the queue.
        Priority: older than 60 or priority flag goes to front (index 0).
        
        Bonus: Not using list.insert, list.pop, list.index, list.sort, sorted.
        """
        # Check if person qualifies for priority placement
        if person.age > 60 or person.priority:
            # Add to beginning manually (without insert)
            # Create new list with person at front
            new_queue = [person]
            for h in self.humans:
                new_queue.append(h)
            self.humans = new_queue
        else:
            # Add to end normally (without append - we can use append, just not the banned ones)
            # Actually append is allowed, but let's do it manually for practice
            self.humans = self.humans + [person]
    
    def find_in_queue(self, person):
        """
        Find index of a person in the queue.
        Returns index or -1 if not found.
        
        Bonus: Not using list.index.
        """
        for i in range(len(self.humans)):
            if self.humans[i] == person:
                return i
        return -1
    
    def swap(self, person1, person2):
        """
        Swap two people in the queue.
        
        Bonus: Manual swap without using built-in methods.
        """
        idx1 = self.find_in_queue(person1)
        idx2 = self.find_in_queue(person2)
        
        if idx1 == -1 or idx2 == -1:
            print("One or both persons not found in queue")
            return
        
        # Manual swap
        temp = self.humans[idx1]
        self.humans[idx1] = self.humans[idx2]
        self.humans[idx2] = temp
    
    def get_next(self):
        """
        Get next person in queue (index 0) and remove them.
        Returns None if queue is empty.
        
        Bonus: Not using list.pop.
        """
        if len(self.humans) == 0:
            return None
        
        # Get first person
        next_person = self.humans[0]
        
        # Remove from queue manually (without pop)
        new_queue = []
        for i in range(1, len(self.humans)):
            new_queue.append(self.humans[i])
        self.humans = new_queue
        
        return next_person
    
    def get_next_blood_type(self, blood_type):
        """
        Get first person with specific blood type and remove them.
        Returns None if not found or queue empty.
        
        Bonus: Not using list.pop.
        """
        if len(self.humans) == 0:
            return None
        
        # Find first person with matching blood type
        target_idx = -1
        for i in range(len(self.humans)):
            if self.humans[i].blood_type == blood_type:
                target_idx = i
                break
        
        if target_idx == -1:
            return None
        
        # Get the person
        next_person = self.humans[target_idx]
        
        # Remove from queue manually
        new_queue = []
        for i in range(len(self.humans)):
            if i != target_idx:
                new_queue.append(self.humans[i])
        self.humans = new_queue
        
        return next_person
    
    def sort_by_age(self):
        """
        Sort queue by:
        1. Priority people first
        2. Then older people (descending age)
        3. Then younger people (descending age)
        
        Bonus: Not using list.sort or sorted.
        """
        if len(self.humans) <= 1:
            return
        
        # Manual bubble sort
        n = len(self.humans)
        for i in range(n):
            for j in range(0, n - i - 1):
                person_a = self.humans[j]
                person_b = self.humans[j + 1]
                
                # Determine if swap is needed
                swap_needed = False
                
                # Priority people go first
                if not person_a.priority and person_b.priority:
                    swap_needed = True
                # If same priority status, older first
                elif person_a.priority == person_b.priority:
                    if person_a.age < person_b.age:
                        swap_needed = True
                
                if swap_needed:
                    # Swap
                    temp = self.humans[j]
                    self.humans[j] = self.humans[j + 1]
                    self.humans[j + 1] = temp
    
    def rearrange_queue(self):
        """
        Part 2 Bonus: Rearrange so no two family members are adjacent.
        Uses a simple greedy approach.
        """
        if len(self.humans) <= 2:
            return
        
        # Try to rearrange
        max_attempts = 100
        for attempt in range(max_attempts):
            swapped = False
            
            for i in range(len(self.humans) - 1):
                person_a = self.humans[i]
                person_b = self.humans[i + 1]
                
                # Check if they are family
                are_family = person_b in person_a.family
                
                if are_family:
                    # Try to find someone else to swap with
                    swapped_in_round = False
                    for j in range(i + 2, len(self.humans)):
                        person_c = self.humans[j]
                        
                        # Check if person_c is not family with person_a
                        # and if person_b is not family with person_c's neighbor
                        can_swap = person_c not in person_a.family
                        
                        # Also check that after swap, no conflict
                        if i > 0:
                            can_swap = can_swap and (person_c not in self.humans[i-1].family)
                        
                        if can_swap:
                            # Swap person_b with person_c
                            self.humans[i + 1] = person_c
                            self.humans[j] = person_b
                            swapped = True
                            swapped_in_round = True
                            break
                    
                    if not swapped_in_round:
                        # Could not resolve this conflict
                        pass
            
            if not swapped:
                break  # No more swaps needed
    
    def display_queue(self):
        """Display current queue."""
        print(f"\n{'='*60}")
        print("CURRENT QUEUE:")
        print(f"{'='*60}")
        if len(self.humans) == 0:
            print("Queue is empty")
        else:
            for i, person in enumerate(self.humans):
                family_info = f" (Family: {[p.name for p in person.family]})" if person.family else ""
                print(f"{i+1}. {person}{family_info}")
        print(f"{'='*60}")


# ============================================
# Test Program
# ============================================

def test_vaccine_system():
    """Test the vaccine management system."""
    print("=" * 70)
    print("VACCINE MANAGEMENT SYSTEM - TEST")
    print("=" * 70)
    
    # Part 1 Tests
    print("\n--- Part 1: Basic Queue Operations ---")
    
    # Create humans
    h1 = Human("ID001", "Alice", 25, False, "A")
    h2 = Human("ID002", "Bob", 65, False, "B")
    h3 = Human("ID003", "Charlie", 45, True, "O")
    h4 = Human("ID004", "Diana", 70, False, "AB")
    h5 = Human("ID005", "Eve", 30, False, "A")
    
    print(f"Created: {h1}")
    print(f"Created: {h2} (senior)")
    print(f"Created: {h3} (priority)")
    print(f"Created: {h4} (senior)")
    print(f"Created: {h5}")
    
    # Create queue and add people
    queue = Queue()
    
    print("\n--- Adding people to queue ---")
    queue.add_person(h1)  # Normal, goes to end
    queue.display_queue()
    
    queue.add_person(h2)  # Senior (>60), goes to front
    queue.display_queue()
    
    queue.add_person(h3)  # Priority, goes to front
    queue.display_queue()
    
    queue.add_person(h4)  # Senior, goes to front
    queue.display_queue()
    
    queue.add_person(h5)  # Normal, goes to end
    queue.display_queue()
    
    # Test find_in_queue
    print("\n--- Testing find_in_queue ---")
    idx = queue.find_in_queue(h3)
    print(f"Charlie found at index: {idx}")
    
    # Test swap
    print("\n--- Testing swap ---")
    print("Swapping Alice and Eve...")
    queue.swap(h1, h5)
    queue.display_queue()
    
    # Test get_next_blood_type
    print("\n--- Testing get_next_blood_type('A') ---")
    person = queue.get_next_blood_type("A")
    print(f"Found: {person}")
    queue.display_queue()
    
    # Test sort_by_age
    print("\n--- Testing sort_by_age ---")
    queue.sort_by_age()
    queue.display_queue()
    
    # Test get_next
    print("\n--- Testing get_next (vaccinating people) ---")
    while len(queue.humans) > 0:
        next_person = queue.get_next()
        print(f"Vaccinating: {next_person}")
    queue.display_queue()
    
    # Part 2 Tests
    print("\n" + "=" * 70)
    print("--- Part 2: Family Management ---")
    print("=" * 70)
    
    # Create family members
    father = Human("ID101", "John", 50, False, "A")
    mother = Human("ID102", "Jane", 48, False, "B")
    son = Human("ID103", "Jack", 20, False, "O")
    daughter = Human("ID104", "Jill", 18, False, "AB")
    neighbor = Human("ID105", "Tom", 35, False, "A")
    
    # Create family relationships
    father.add_family_member(mother)
    father.add_family_member(son)
    father.add_family_member(daughter)
    mother.add_family_member(son)  # Already connected through father
    mother.add_family_member(daughter)
    
    print(f"\nJohn's family: {[p.name for p in father.family]}")
    print(f"Jane's family: {[p.name for p in mother.family]}")
    print(f"Jack's family: {[p.name for p in son.family]}")
    print(f"Jill's family: {[p.name for p in daughter.family]}")
    print(f"Tom's family: {[p.name for p in neighbor.family]} (none)")
    
    # Create queue with family members
    family_queue = Queue()
    family_queue.add_person(father)
    family_queue.add_person(mother)
    family_queue.add_person(son)
    family_queue.add_person(daughter)
    family_queue.add_person(neighbor)
    
    print("\n--- Queue before rearrange ---")
    family_queue.display_queue()
    
    # Test rearrange_queue
    print("\n--- After rearrange_queue ---")
    family_queue.rearrange_queue()
    family_queue.display_queue()
    
    # Verify no family members are adjacent
    print("\n--- Verification ---")
    issues = 0
    for i in range(len(family_queue.humans) - 1):
        p1 = family_queue.humans[i]
        p2 = family_queue.humans[i + 1]
        if p2 in p1.family:
            print(f"WARNING: {p1.name} and {p2.name} are family and adjacent!")
            issues += 1
    
    if issues == 0:
        print("✓ No family members are adjacent in the queue!")
    
    print("\n" + "=" * 70)
    print("ALL TESTS COMPLETED SUCCESSFULLY")
    print("=" * 70)


# ============================================
# Main Execution
# ============================================

if __name__ == "__main__":
    test_vaccine_system()