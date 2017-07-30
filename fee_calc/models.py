import persistent


class Fee(persistent.Persistent):

    def __init__(self, payee, acceptor, balance, description):
        super().__init__()
        self.payee = payee
        self.acceptor = acceptor
        self.balance = balance
        self.description = description

    def __str__(self):
        return "{}\t=> {}: {}".format(self.acceptor, self.payee, self.balance)

    def as_dict(self):
        return self.__dict__
