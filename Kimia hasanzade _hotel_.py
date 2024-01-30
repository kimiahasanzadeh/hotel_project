from abc import ABC, abstractmethod



class Person(ABC):
    def __init__(self, unique_id, name, contact_info):
        self.unique_id = unique_id
        self.name = name
        self.contact_info = contact_info
    
    
    @abstractmethod
    def __str__(self):
        pass

class Guest(Person):
    def __init__(self, unique_id, name, contact_info):
        super().__init__(unique_id, name, contact_info)
    
    def __str__(self):
        print(f"Guest: {self.name} ID: {self.unique_id}  Contact: {self.contact_info}")


#......................

class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.availability = True
        self.booking_details = {}
    
    def check_availability(self, date):
        if date in self.booking_details:
            if self.booking_details[date]['status'] == 'booked':
                return False
            else:
                return True
        else:
            return True
    
    def book(self, date, guest_id):
        if self.check_availability(date=date):
            self.booking_details[date] = {'guest_id': guest_id,'status': 'booked'}
            print("Room Booked")
        else:
            print('Room Booked ')
    
    def __str__(self):
        print(f"Room: {self.room_number}  Type: {self.room_type}")



#................



class Staff(Person):
    def __init__(self, unique_id, name, contact_info, position):
        super().__init__(unique_id, name, contact_info)
        self.position = position


    def __str__(self):
        print(f"Name : {self.name}, : {self.unique_id})
    

#........................

class Hotel:
    def __init__(self, name):
        self.name = name
        self.guests = {}
        self.rooms = {}
        self.staff = {}
     

    def add_guest(self, guest_id, name, contact_info):
        guest = Guest(guest_id, name, contact_info)
        guest.__str__()
        self.guests[guest_id] = {'name':name, 'phone':contact_info}
    
    def remove_guest(self, guest_id):
        if guest_id in self.guests:
            del self.guests[guest_id]
    
    def get_guest_details(self, guest_id):
        if guest_id in self.guests:
            return (self.guests[guest_id])
        else:
            return False
    
    def add_room(self, room_number, room_type):
        room = Room(room_number, room_type)
        room.__str__()
        self.rooms[room_number] = {'room_type':room_type}
    
    def remove_room(self, room_number):
        if room_number in self.rooms:
            del self.rooms[room_number]
    
    def get_room_details(self, room_number):
        if room_number in self.rooms:
            return (self.rooms[room_number])
        else:
            return False
    
    def add_staff(self, staff_id, name, contact_info, position):
        staff = Staff(staff_id, name, contact_info, position)
        staff.__str__()
        self.staff[staff_id] = {'name':name, 'contact_info':contact_info, 'position':position}
    
    def remove_staff(self, staff_id):
        if staff_id in self.staff:
            del self.staff[staff_id]

    
    def __str__(self):
        print( f"Hotel: {self.name}  Number of guests: {len(self.guests)}  Number of rooms: {len(self.rooms)}  Number of staff: {len(self.staff)}")
    


