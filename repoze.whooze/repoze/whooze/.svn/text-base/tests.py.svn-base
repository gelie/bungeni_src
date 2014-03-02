import os.path
import unittest
from zope.component import provideHandler
from zope.publisher.browser import BrowserPage
from zope.app.testing.functional import BrowserTestCase
from zope.app.testing.functional import FunctionalTestSetup

class TestWhoPrincipal(unittest.TestCase):
    def _getTargetClass(self):
        from repoze.whooze.auth import WhoPrincipal
        return WhoPrincipal

    def _makeOne(self, *arg, **kw):
        klass = self._getTargetClass()
        return klass(*arg, **kw)

    def test_ctor(self):
        principal = self._makeOne('id', 'title', 'description', ('Foo',))
        self.assertEqual(principal.id, 'id')
        self.assertEqual(principal.title, 'title')
        self.assertEqual(principal.description, 'description')
        self.assertEqual(len(principal.groups), 1)
        self.assertEqual(tuple(principal.groups)[0], 'Foo')
        self.assertEqual(principal.groups.values()[0].id, 'Foo')

integration_zcml = os.path.join(os.path.dirname(__file__), 'integration.zcml')

class SomePage(BrowserPage):

    def __call__(self):
        return 'Some page'

class PrincipalPage(BrowserPage):

    def __call__(self):
        return self.request.principal.title

class TestWhoAuthenticationIntegration(BrowserTestCase):

    def setUp(self):
        FunctionalTestSetup(integration_zcml).setUp()

    def test_public(self):
        env = {'repoze.who.identity': {'repoze.who.userid': 'testing.somedude',
                                       'title': 'Some Dude',
                                       'description': 'Just some dude',
                                       'groups':('foo',),
                                       }
               }
        response = self.publish('/public.html', env=env)
        self.assertEquals(response.getStatus(), 200)

    def test_unauthorized(self):
        env = {'repoze.who.identity': {'repoze.who.userid': 'testing.somedude',
                                       'title': 'Some Dude',
                                       'description': 'Just some dude',
                                       'groups':('foo',),
                                       }}
        response = self.publish('/protected.html', env=env, handle_errors=True)
        self.assertEquals(response.getStatus(), 401)

    def test_authorized(self):
        env = {'repoze.who.identity': {'repoze.who.userid': 'testing.somemanager',
                                       'title': 'Some Manager',
                                       'description': "It's the manager, dude",
                                       'groups':('foo',),
                                       }
               }
        response = self.publish('/protected.html', env=env)
        self.assertEquals(response.getStatus(), 200)

    def test_unauthenticated(self):
        response = self.publish('/principal.html')
        self.assertEquals(response.getBody(), 'Unauthenticated User')

    def test_principal(self):
        env = {'repoze.who.identity': {'repoze.who.userid': 'testing.somedude',
                                       'title': 'Some Dude',
                                       'description': 'Just some dude',
                                       'groups':('foo',),
                                       }
               }
        response = self.publish('/principal.html', env=env)
        self.assertEquals(response.getBody(), 'Some Dude')

    def test_event(self):
        env = {'repoze.who.identity': {'repoze.who.userid': 'testing.somedude',
                                       'title': 'Some Dude',
                                       'description': 'Just some dude',
                                       'groups':('foo',),
                                       }
               }

        principal = None
        def handler(event):
            principal = event.principal

        from repoze.whooze.interfaces import IPrincipalCreated
        provideHandler(handler, IPrincipalCreated)
        response = self.publish('/principal.html', env=env)
        self.assertEquals(principal.title, 'Some Dude')

def test_suite():
    import sys
    return unittest.findTestCases(sys.modules[__name__])
