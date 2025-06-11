from datetime import datetime, timedelta


class Service:
    def __init__(self, name: str, cost: str, duration: str = '1'):
        self.name = name
        self.duration = duration
        self.cost = cost


class Master:
    def __init__(self, name: str):
        self.name = name
        self.service = []
        self.schedule = {}

    def get_month_free_hours_dict(self, start=10, end=20, year=None, month=None):
        """
        Возвращает словарь: ключ — строка 'YYYY-MM-DD HH:MM', значение — True
        для всех часов с 10:00 до 19:00 включительно на каждый день указанного месяца.
        Если год и месяц не указаны — берёт текущие.
        """
        now = datetime.now()
        year = year or now.year
        month = month or now.month

        # Находим первый день месяца
        first_day = datetime(year, month, 1)
        # Находим первый день следующего месяца
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)

        day = first_day
        while day < next_month:
            # Пропускаем выходные (если нужно)
            # if day.weekday() >= 5:
            #     day += timedelta(days=1)
            #     continue

            for hour in range(start, end):  # 10:00 до 19:00 включительно
                dt = day.replace(hour=hour, minute=0, second=0, microsecond=0)
                key = dt.strftime("%Y-%m-%d %H:%M")
                self.schedule[key] = True
            day += timedelta(days=1)

    def is_available(self, appointment_time: datetime):
        dt_form = appointment_time.strftime("%Y-%m-%d %H:%M")
        return self.schedule.get(dt_form, False)

    def book_time(self, appointment_time: datetime):
        dt_form = appointment_time.strftime("%Y-%m-%d %H:%M")
        self.schedule[dt_form] = False

    def cancel_time(self, appointment_time: datetime):
        dt_form = appointment_time.strftime("%Y-%m-%d %H:%M")
        if dt_form in self.schedule:
            self.schedule[dt_form] = True


class Client:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def view_appointments(self):
        return self.appointments


class Appointment:
    def __init__(
            self,
            appointment_time: datetime,
            master: Master,
            client: Client,
            service: Service,
            description: str = ''
    ):
        self.appointment_time = appointment_time
        self.master = master
        self.client = client
        self.service = service
        self.description = description
        self.confirmed = False

    def confirm(self):
        self.confirmed = True

    def cancel(self):
        self.confirmed = False


inna = Master('Инна')
dt1 = datetime(2025, 6, 1, 12)
dt5 = datetime(2025, 6, 1, 11)
inna.get_month_free_hours_dict()
inna.book_time(dt5)
print(inna.schedule)
inna.cancel_time(dt5)
print(inna.schedule)
print(inna.is_available(dt5))


hairXL = Service('покраскаXL', '4700', '1500')
alla = Client('Алла', '+79265550077')


