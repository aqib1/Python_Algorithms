class TicketingProblem:
    def caught_speeding(self, speed: int, is_birthday: bool):
        NO_TICKET_LIMIT = 65 if is_birthday else 60
        SMALL_TICKET_LIMIT_START = 66 if is_birthday else 61
        SMALL_TICKET_LIMIT_END = 85 if is_birthday else 80
        BIG_TICKET_LIMIT = 86 if is_birthday else 81

        if speed <= NO_TICKET_LIMIT:
            return "No Ticket"
        elif SMALL_TICKET_LIMIT_START <= speed <= SMALL_TICKET_LIMIT_END:
            return "Small Ticket"
        elif speed >= BIG_TICKET_LIMIT:
            return "Big Ticket"
        return None


if __name__ == '__main__':
    ticketProblem = TicketingProblem()
    print(ticketProblem.caught_speeding(81, True))
    print(ticketProblem.caught_speeding(81, False
                                        ))