class ServiceBase:
    manager = None

    def __init__(self):
        self.records = []

    def create(self, **kwargs):
        if self.manager is None:
            raise NotImplementedError("Subclasses must define a manager")
        return self.manager.create(**kwargs)

    def get(self, **kwargs):
        if self.manager is None:
            raise NotImplementedError("Subclasses must define a manager")
        try:
            return self.manager.get(**kwargs)
        except self.manager.model.DoesNotExist:
            return None

    def filter(self, **kwargs):
        if self.manager is None:
            raise NotImplementedError("Subclasses must define a manager")
        return self.manager.filter(**kwargs)

    def delete(self, **kwargs):
        if self.manager is None:
            raise NotImplementedError("Subclasses must define a manager")
        return self.manager.filter(**kwargs).delete()

    def update(self, filters=None, **kwargs):
        if self.manager is None:
            raise NotImplementedError("Subclasses must define a manager")
        if not filters:
            raise ValueError("Filters must be provided to update records safely")
        qs = self.manager.filter(**filters)
        return qs.update(**kwargs)