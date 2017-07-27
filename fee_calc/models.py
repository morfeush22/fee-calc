import persistent


class Fee(persistent.Persistent):

    def __init__(self, payee, acceptor, balance):
        super().__init__()
        self.payee = payee
        self.acceptor = acceptor
        self.balance = balance

    def __str__(self):
        return "{} => {}: {}".format(self.acceptor, self.payee, self.balance)

    def as_list(self):
        return list(self.__dict__.values())
