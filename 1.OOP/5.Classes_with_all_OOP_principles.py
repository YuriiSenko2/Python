from abc import ABC, abstractmethod


class ArtMuseum(ABC):
    def __init__(self, name: str = None, creation_year: int = None, author: str = None, for_sale: bool = True):
        self.__name = name
        self.__creationYear = creation_year
        self.__author = author
        self.__sale = for_sale

    @abstractmethod
    def brief_overview(self):
        """The overview of the artwork will be here"""

    @property
    def name(self):
        return '\nName: ' + self.__name

    @property
    def creation_year(self):
        return '\nYear of creation: ' + str(self.__creationYear)

    @property
    def author(self):
        return '\nAuthor: ' + self.__author

    @property
    def sale(self):
        if self.__sale:
            return '\nSale status: for sale'
        return '\nSale status: not for sale'

    @name.setter
    def name(self, value):
        self.__name = value

    @creation_year.setter
    def creation_year(self, value):
        self.__creationYear = value

    @author.setter
    def author(self, value):
        self.__author = value

    @sale.setter
    def sale(self, value):
        self.__sale = value


class Pictures(ArtMuseum):
    def brief_overview(self):
        overview = input()
        return '\nPicture overview: ' + overview

    def __category_description(self):
        return 'A category contains information about pictures of the museum'

    def __access_to_changes(self):
        return 'Only an administrator can adjust the "Pictures category"'

    def info_for_qa(self):
        return '\n\nMemo for QA:\n' + self.__category_description() + '\n' + self.__access_to_changes() + \
               '\n' + 'Just test the "Pictures category"!'


class Sculptures(ArtMuseum):
    def brief_overview(self):
        overview = input()
        return '\nSculpture overview: ' + overview

    def __category_description(self):
        return 'A category contains information about sculptures of the museum'

    def __access_to_changes(self):
        return 'Only an administrator can adjust the "Sculptures category"'

    def info_for_qa(self):
        return '\n\nMemo for QA:\n' + self.__category_description() + '\n' + self.__access_to_changes() + \
               '\n' + 'Just test the "Sculptures category"!'

pic2 = Pictures.info_for_qa(Pictures())
print(pic2)
pic1 = Pictures()
pic1.name = 'The Beast Goes for a Walk'
pic1.creation_year = 1971
pic1.author = 'Maria Prymachenko'
pic1.sale = True
pic1_description = pic1.brief_overview()
pic1_for_qa = pic1.info_for_qa()
pic1_closed = pic1.__category.description()

sculpture1 = Sculptures()
sculpture1.name = 'Violinist on the roof'
sculpture1.creation_year = 2003
sculpture1.author = 'Seyfaddin Gurbanov'
sculpture1.sale = False
sculpture1_description = sculpture1.brief_overview()
sculpture1_for_qa = sculpture1.info_for_qa()

print(pic1.name, pic1.creation_year, pic1.author, pic1.sale, pic1_description, pic1_for_qa)
print(sculpture1.name, sculpture1.creation_year, sculpture1.author, sculpture1.sale,
      sculpture1_description, sculpture1_for_qa)

