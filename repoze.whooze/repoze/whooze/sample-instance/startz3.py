import logging
import os
import sys
try:
    here = os.path.abspath(os.path.dirname(__file__))
except NameError:
    here = os.path.abspath(os.path.dirname(sys.argv[0]))

def main():
    import zope.app.wsgi
    zope_conf = os.path.join(here, 'zope.conf')
    zope = zope.app.wsgi.getWSGIApplication(zope_conf)

    from repoze.who.middleware import PluggableAuthenticationMiddleware
    from repoze.who.config import WhoConfig
    parser = WhoConfig(here)
    parser.parse(open(os.path.join(here, 'who.ini')))
    log_stream = sys.stdout
    log_level = logging.DEBUG

    app = PluggableAuthenticationMiddleware(
        zope,
        parser.identifiers,
        parser.authenticators,
        parser.challengers,
        parser.mdproviders,
        parser.request_classifier,
        parser.challenge_decider,
        log_stream,
        log_level,
        )
    from paste import httpserver
    httpserver.serve(app, host='0.0.0.0', port='9876')

if __name__ == '__main__':
    main()
