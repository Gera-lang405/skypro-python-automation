from address import Address
from mailing import Mailing

to_address = Address("190000", "Санкт-Петербург", "Невский проспект",
                     "28", "15")
from_address = Address("101000", "Москва", "Тверская улица", "7", "42")

mailing = Mailing(to_address, from_address, 350, "RA123456789RU")

print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - "
      f"{mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
