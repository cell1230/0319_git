class dsl(object):
    def __init__(self,name):
        self.name=name
    def whois(self):
        if self.name == "cat":
            print(f'{self.name} is a cat')
        elif self.name == 'dog':
            print(f'{self.name}is a dog')
        elif self.name == 'cow':
            print(f'{self.name}is a cow')
        else:
            print(f'{self.name}가 최고다')

    