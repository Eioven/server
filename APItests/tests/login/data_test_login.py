from faker import Faker

fake = Faker()

data_test_login_negative = [
  #Несуществующий пользователь
  {
    "email": fake.email(),
    "password": fake.password()
  },
  #Пустые данные
  {
    "email": "",
    "password": ""
  },
  #Email не соответствует маске
  {
    "email": fake.name(),
    "password": fake.password()
  }
]
