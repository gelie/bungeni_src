user_metadata = {
    'testing.somedude':
       {'title':'Some Dude', 'description':'Some Dude',
        'groups':('Foo',)},
    'testing.somemanager':
       {'title':'Some Manager', 'description':'Some Manager',
        'groups':('Bar',)},
     }

class ZopeMetadataProvider(object):
    """ A repoze.who metadata provider for our sample data """
    def add_metadata(self, environ, identity):
        md = user_metadata.get(identity['repoze.who.userid'])
        if md:
            identity.update(md)
        
