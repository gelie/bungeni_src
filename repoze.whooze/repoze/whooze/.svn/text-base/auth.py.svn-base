from zope.interface import implements
from zope.event import notify
from zope.security.interfaces import IGroupAwarePrincipal
from zope.security.interfaces import IGroup
from zope.app.security.interfaces import IAuthentication
from zope.app.security.interfaces import IUnauthenticatedPrincipal
from repoze.whooze.events import PrincipalCreated

class UnauthenticatedPrincipal(object):
    implements(IUnauthenticatedPrincipal)
    id = 'zope.anybody'
    title = description = u'Unauthenticated User'

class WhoGroup(object):
    implements(IGroup)
    def __init__(self, id):
        self.id = id
        self.title = id
        self.description = id

class WhoPrincipal(object):
    implements(IGroupAwarePrincipal)

    def __init__(self, id, title, description, groups):
        self.id = id
        self.title = title
        self.description = description
        self.groups = dict(
            (group_id, WhoGroup(group_id)) for group_id in groups)
        
class WhoAuthentication(object):
    implements(IAuthentication)

    def authenticate(self, request):
        identity = request.get('repoze.who.identity')
        if identity is None:
            return self.unauthenticatedPrincipal()
        userid = identity['repoze.who.userid']
        title = identity.get('title')
        description = identity.get('description')
        groups = identity.get('groups', ())
        principal = WhoPrincipal(userid, title, description, groups)
        notify(PrincipalCreated(self, principal, request))
        return principal

    def unauthenticatedPrincipal(self):
        return UnauthenticatedPrincipal()
    
    def unauthorized(self, id, request):
        request.response.setStatus(401)

    def getPrincipal(self, id):
        # Repeat after me: I'm a lame API, I'm a lame API, ...
        return WhoPrincipal(id, '', '', ())
