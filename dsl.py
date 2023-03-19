class dsl(object):
    def __init__(self,name):
        self.name=name
    def whois(self):
        if self.name == "cat":
            print(f'{self.name} is a cat')
        elif self.name == 'dog':
            print(f'{self.name}is a dog')
        else:
            print(f'{self.name}가 최고다')

    