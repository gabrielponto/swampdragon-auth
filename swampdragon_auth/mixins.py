
class TokenAuthMixin(object):
    def handle(self,data):
        if 'auth' in data['args']:
            auth_token = data['args'].pop('auth')
            self.connection.authenticate(auth_token)
        super(TokenAuthMixin, self).handle(data)

