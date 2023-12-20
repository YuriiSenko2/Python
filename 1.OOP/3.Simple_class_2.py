class Companies:
    def __init__(self, company_name: str = None, number_of_staff: int = None, annual_revenue: int = None):
        self.__company = company_name
        self.__staff = number_of_staff
        self.__revenue = annual_revenue

    def company_name(self):
        return self.__company

    def number_of_staff(self):
        return self.__staff

    def annual_revenue(self):
        return self.__revenue

    def company_size(self):
        if self.__staff <= 100:
            return 'Small company'
        elif self.__staff <= 250:
            return 'Medium-sized company'
        elif self.__staff <= 1000:
            return 'Large company'
        else:
            return 'Giant company'

    def company_affairs(self):
        if self.__revenue <= 100000:
            return 'Need changes'
        elif self.__revenue <= 1000000:
            return 'Still some way to go'
        else:
            return 'Way to go'

    @classmethod
    def company_info(cls, name, staff, revenue):
        return cls(name, staff, revenue)


company_1 = Companies.company_info('Supermarket "Klass"', 1001, 1000001)
print(company_1.company_name())
size_of_company_1 = company_1.company_size()
print(size_of_company_1)
affairs_of_company_1 = company_1.company_affairs()
print(affairs_of_company_1)