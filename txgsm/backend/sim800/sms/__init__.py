"""
SMS support.
"""

from twisted.protocols.amp import CommandLocator

from txgsm.backend.sim800.sms import commands


class SMSManager(CommandLocator):
    """
    SMS manager.
    """
    @commands.SMSCodeModeTest.responder
    def smsCodeModeTest(self):
        """
        Get list of supported SMS code modes.
        """
        atCommandName = 'AT+CCODE=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CCODE: (0,1)'

        # return AT command result
        return {
            'modes': [0, 1]
        }


    @commands.SMSCodeModeRead.responder
    def smsCodeModeRead(self):
        """
        Get current SMS code mode.
        """
        atCommandName = 'AT+CCODE?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CCODE: <mode>'

        # return AT command result
        return {
            'mode': 0
        }


    @commands.SMSCodeModeWrite.responder
    def smsCodeModeWrite(self, mode):
        """
        Change current SMS code mode.

        :param mode:
        :type mode: int
        """
        atCommandName = 'AT+CCODE=<mode>'

        # XXX: call AT command

        return {}


    @commands.SMSDeleteMessagesTest.responder
    def smsDeleteMessagesTest(self):
        """
        Get supported types for deleting all SMS messages.
        """
        atCommandName = 'AT+CMGDA=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CMGDA: (list of supported <type>s)'

        # return AT command result
        return {
            'modes': ['foo', 'bar']
        }


    @commands.SMSDeleteMessagesWrite.responder
    def smsDeleteMessagesWrite(self, messageType):
        """
        Delete all SMS messages by ``messageType``.

        :param messageType:
        :type messageType: string
        """
        atCommandName = 'AT+CMGDA=<type>'

        # XXX: maxResponseTime = 25
        # XXX: call AT command

        return {}


    @commands.SMSNewMessageIndicationsTest.responder
    def smsNewMessageIndicationsTest(self):
        """
        Get list of supported SMS message indication types.
        """
        atCommandName = 'AT+CNMI=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CNMI: (list of supported <mode>s),(list of supported <mt>s),(list of supported <bm>s),(list of supported <ds>s),(list of supported <bfr>s)'

        # return AT command result
        return {
            'modes': [0, 1],
            'mt': [0, 1],
            'bm': [0, 1],
            'ds': [0, 1],
            'bfr': [0, 1]
        }


    @commands.SMSNewMessageIndicationsRead.responder
    def smsNewMessageIndicationsRead(self):
        """
        Get new SMS message indications.
        """
        atCommandName = 'AT+CNMI?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CNMI: <mode>,<mt>,<bm>,<ds>,<bfr>'

        # return AT command result
        return {
            'mode': 0,
            'mt': 0,
            'bm': 0,
            'ds': 0,
            'bfr': 0
        }


    @commands.SMSNewMessageIndicationsWrite.responder
    def smsNewMessageIndicationsWrite(self, mode, mt=None, bm=None, ds=None,
                                      bfr=None):
        """
        Change new SMS message indications.

        :param mode:
        :type mode: int
        :param mt:
        :type mt: int
        :param bm:
        :type bm: int
        :param ds:
        :type ds: int
        :param bfr:
        :type bfr: int
        """
        atCommandName = 'AT+CNMI=<mode>[,<mt>[,<bm>[,<ds>[,<bfr>]]]]'

        # XXX: call AT command

        return {}


    def deleteMessage(self, index):
        """
        Delete SMS message.

        :param index:
        :type index: int
        """
        # XXX: txgsm.backends.sim800.sms.commands.SMSDeleteMessage
        pass


    def readMessage(self, index):
        """
        Read SMS message.

        :param index: Value in the range of location numbers supported by the
          associated memory.
        :type index: int
        """
        # XXX: txgsm.backends.sim800.sms.commands.SMSReadMessage
        pass


    def sendMessage(self):
        """
        Sends message to the network.
        """
        # XXX: txgsm.backends.sim800.sms.commands.SMSSendMessage
        pass


    def selectMessageFormat(self, mode):
        """
        Select SMS message format.

        :param mode: Denotes which input and output format of messages to use.
        :type mode: int
        """
        # XXX: txgsm.backends.sim800.sms.commands.SMSSelectMessageFormat
        pass


    @commands.SMSServiceCenterAddressRead.responder
    def smsServiceCenterAddressRead(self):
        """
        Get SMS service center address.
        """
        atCommandName = 'AT+CSCA?'

        # XXX: maxResponseTime = 5

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CSCA: <sca>,<tosca>[,<scaAlpha>]'

        # return AT command result
        return {
            'sca': 'foo',
            'tosca': 0,
            'scaAlpha': 'bar'
        }


    @commands.SMSServiceCenterAddressWrite.responder
    def smsServiceCenterAddressWrite(self, sca, tosca=None):
        """
        Change SMS service center address.

        Updates the SMSC address, through which mobile originated SMS are
        transmitted.

        :param sca:
        :type sca: string
        :param tosca:
        :type tosca: int
        """
        atCommandName = 'AT+CSCA=<sca>[,<tosca>]'

        # XXX: maxResponseTime = 5
        # XXX: call AT command

        return {}
