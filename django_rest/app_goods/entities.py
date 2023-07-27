class Item:
    def __init__(self, name, description, weight,group):
        self.name = name
        self.description = description
        self.weight = weight
        self.group = group

    def to_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'weight': self.weight,
            'group':self.group,
        }
