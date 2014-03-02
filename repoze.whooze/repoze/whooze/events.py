from zope.interface import implements
from repoze.whooze.interfaces import IPrincipalCreated

class PrincipalCreated(object):
    implements(IPrincipalCreated)

    def __init__(self, plugin, principal, request):
        self.plugin = plugin
        self.principal = principal
        self.request = request
