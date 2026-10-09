from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79161234567"),
    Smartphone("Samsung", "Galaxy S24", "+79262345678"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79033456789"),
    Smartphone("Google", "Pixel 8", "+79054567890"),
    Smartphone("Honor", "Magic 6", "+79995678901"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
