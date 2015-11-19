# run with twistd -noy amp_server.tac

from twisted.protocols.amp import AMP
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.application.service import Application
from twisted.application.internet import StreamServerEndpointService

from txgsm.backend.sim800 import SIM800Locator

application = Application("Basic txgsm AMP server")

endpoint = TCP4ServerEndpoint(reactor, 1234)
factory = Factory()
factory.protocol = lambda: AMP(locator=SIM800Locator())
service = StreamServerEndpointService(endpoint, factory)
service.setServiceParent(application)
