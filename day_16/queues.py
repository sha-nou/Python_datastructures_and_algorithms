# queues.py

import queue

class Ticket:
    def __init__(self, ticket_id, description):
        self.ticket_id = ticket_id
        self.description = description

    def __str__(self):
        return f"Ticket #{self.ticket_id}, Description: {self.description}"

class TicketSystem:
    def __init__(self):
        self.tickets = queue.Queue()
        self.waiting_tickets = queue.Queue()
        self.next_ticket_id = 1  

    def create_ticket(self, description):
        ticket = Ticket(self.next_ticket_id, description)
        self.tickets.put(ticket)
        return f"Ticket ${ticket.ticket_id} created."

    def view_ticket(self):
        if not self.tickets.empty():
            ticket = self.tickets.get()
            self.waiting_tickets.put(ticket)  
            return f"Viewing Ticket ${ticket.ticket_id}, Description: {ticket.description}"
        else:
            return "No tickets in queue."

    def process_ticket(self):
        if not self.waiting_tickets.empty():
            ticket = self.waiting_tickets.get()
            return f"Processing Ticket #{ticket.ticket_id}, Description: {ticket.description}"
        else:
            return "No waiting tickets."

if __name__ == "__main__":
    ticket_system = TicketSystem()
    
    print(ticket_system.create_ticket('Movie night'))
    print(ticket_system.create_ticket('Concert tickets'))
    print(ticket_system.view_ticket())
    
