from zope import interface

class IPrincipalCreated(interface.Interface):
    """A principal has been created."""
    
    principal = interface.Attribute(
        "The principal that was created.")

    plugin = interface.Attribute(
        "The authentication plugin that created the principal.")

    request = interface.Attribute(
        "The request the user was authenticated against")
