from datetime import datetime

class Reservation:
    def __init__(self, reservation_id, customer_id, vehicle_id, start_date, end_date, total_cost, status):
        self.__reservation_id = reservation_id
        self.__customer_id = customer_id
        self.__vehicle_id = vehicle_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__total_cost = total_cost
        self.__status = status

    def calculate_total_cost(self, daily_rate):
        start = datetime.strptime(self.__start_date, "%Y-%m-%d")
        end = datetime.strptime(self.__end_date, "%Y-%m-%d")
        days = (end - start).days
        self.__total_cost = daily_rate * max(days, 1)
        return self.__total_cost

    def get_reservation_id(self): return self.__reservation_id
    def get_customer_id(self): return self.__customer_id
    def get_vehicle_id(self): return self.__vehicle_id
    def get_start_date(self): return self.__start_date
    def get_end_date(self): return self.__end_date
    def get_total_cost(self): return self.__total_cost
    def get_status(self): return self.__status

    def set_reservation_id(self, reservation_id): self.__reservation_id = reservation_id
    def set_customer_id(self, customer_id): self.__customer_id = customer_id
    def set_vehicle_id(self, vehicle_id): self.__vehicle_id = vehicle_id
    def set_start_date(self, start_date): self.__start_date = start_date
    def set_end_date(self, end_date): self.__end_date = end_date
    def set_total_cost(self, total_cost): self.__total_cost = total_cost
    def set_status(self, status): self.__status = status
