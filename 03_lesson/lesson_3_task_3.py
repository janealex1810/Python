from adress import Address
from mailing import Mailing


to_address = Address("101000", "Москва", "Тверская", "1", "45")
from_address = Address("101001", "Санкт-Петербург", "Невский", "10", "12")


mailing = Mailing(to_address, from_address, cost=150.50, track="TRK123456")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
