class Restoran:
    def __init__(self, name, city, what):
        self.name = name
        self.city = city
        self.what = what

    def run(self):
        log = self.name + " " + self.city + " " + self.what
        return log
my_restoran = Restoran('gzal', 'tehran', 'open')
my_restoran.run()
