class User:

    def __init__(self, name, number):
        self.name = name
        self.numberOfTickets = number

    def get_user_name(self):
        return self.name

    def get_number_of_tickets(self):
        return self.numberOfTickets
