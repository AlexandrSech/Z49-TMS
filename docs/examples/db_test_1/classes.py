

class SQL_Generator:
    def __init__(self, connector, table):
        self.connector = connector
        self.table = table

    def select_all(self):
        return self.connector.execute('select * from {};'.format(self.table))


class Holiday(SQL_Generator):
    def __init__(self, connector):
        super().__init__(connector, 'holiday')


