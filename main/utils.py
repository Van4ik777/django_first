
class DataMixin:
    def get_user_context(self, **kwargs):
        context = {}
        context['user_authenticated'] = self.request.user.is_authenticated
        context.update(kwargs)
        return context