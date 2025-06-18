from smartphone import Smartphone


catalog = []


catalog.append(Smartphone("Apple", "iPhone 14", "+79001234567"))
catalog.append(Smartphone("Samsung", "Galaxy S22", "+79007654321"))
catalog.append(Smartphone("Huawei", "P50 Pro", "+79009876543"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "+79003456789"))
catalog.append(Smartphone("Google", "Pixel 6", "+79005432123"))


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. "
          f"{smartphone.phone_number}")
