"""
SMS commands.
"""

from twisted.python.constants import Values, ValueConstant
from twisted.protocols.amp import Command, Integer, ListOf, String

# http://frightanic.com/software-development/regex-for-gsm-03-38-7bit-character-set/


class SMSConstants(Values):
    """
    """
    NOKIA = ValueConstant(0)
    SIEMENS = ValueConstant(1)

    READ = ValueConstant('DEL READ')
    UNREAD = ValueConstant('DEL UNREAD')
    SENT = ValueConstant('DEL SENT')
    UNSENT = ValueConstant('DEL UNSENT')
    RECEIVED = ValueConstant('DEL INBOX')
    ALL = ValueConstant('DEL ALL')

    BUFFER_MODE = ValueConstant(0)
    DISCARD_MODE = ValueConstant(1)
    FLUSH_MODE = ValueConstant(2)
    FORWARD_MODE = ValueConstant(3)

    NO_SMSDELIVER_MT = ValueConstant(0)
    ROUTE_SMSDELIVER_MT = ValueConstant(1)
    CLASS3_SMSDELIVER_MT = ValueConstant(2)


class SMSCodeModeTest(Command):
    """
    Get supported ranges and parameters for SMS code mode.
    """
    response = [
        ('modes', ListOf(Integer()))
    ]


class SMSCodeModeRead(Command):
    """
    Get SMS code mode.
    """
    response = [
        ('mode', Integer())
    ]


class SMSCodeModeWrite(Command):
    """
    Change SMS code mode.
    """
    arguments = [
        ('mode', Integer())
    ]
    requiresAnswer = False


class SMSDeleteMessagesTest(Command):
    """
    Get supported types for deleting SMS messages.
    """
    response = [
        ('types', ListOf(String()))
    ]


class SMSDeleteMessagesWrite(Command):
    """
    Delete SMS messages.
    """
    arguments = [
        ('messageType', String())
    ]
    requiresAnswer = False


class SMSNewMessageIndicationsTest(Command):
    """
    Get supported ranges and parameters for new SMS message indications.
    """
    response = [
        ('modes', ListOf(Integer())),
        ('mt', ListOf(Integer())),
        ('bm', ListOf(Integer())),
        ('ds', ListOf(Integer())),
        ('bfr', ListOf(Integer()))
    ]


class SMSNewMessageIndicationsRead(Command):
    """
    Get new SMS message indications.
    """
    response = [
        ('mode', Integer()),
        ('mt', Integer()),
        ('bm', Integer()),
        ('ds', Integer()),
        ('bfr', Integer())
    ]


class SMSNewMessageIndicationsWrite(Command):
    """
    Change new SMS message indications.
    """
    arguments = [
        ('mode', Integer()),
        ('mt', Integer(optional=True)),
        ('bm', Integer(optional=True)),
        ('ds', Integer(optional=True)),
        ('bfr', Integer(optional=True))
    ]
    requiresAnswer = False


class SMSServiceCenterAddressRead(Command):
    """
    Get SMS service center address.
    """
    response = [
        ('sca', String()),
        ('tosca', Integer()),
        ('scaAlpha', String(optional=True))
    ]


class SMSServiceCenterAddressWrite(Command):
    """
    Change SMS service center address.

    Updates the SMSC address, through which mobile originated SMS are
    transmitted.
    """
    arguments = [
        ('sca', Integer()),
        ('tosca', Integer(optional=True))
    ]
    requiresAnswer = False


class SMSSendMessage(Command):
    """
    Send SMS message.
    """
    maxResponseTime = 60

    TEST_COMMAND = ValueConstant({
        'command': 'AT+CMGS=?'
    })
    WRITE_COMMAND = ValueConstant({
        'command': '+CMGS=<da>[,<toda>] <CR>text is entered <ctrl-Z/ESC>',
        'response': '+CMGS: <mr>',
        'params': {
            'da': 0,
            'toda': 0,
            'length': 0
        }
    })


class SMSReadMessage(Command):
    """
    Read SMS Message.
    """
    maxResponseTime = 5

    NORMAL_MODE = ValueConstant(0)
    NO_CHANGE_MODE = ValueConstant(1)

    TEST_COMMAND = ValueConstant({
        'command': 'AT+CMGR=?'
    })
    WRITE_COMMAND = ValueConstant({
        'command': 'AT+CMGR=<index>[,<mode>]',
        'response': '+CMGS: <mr>',
        'params': {
            'index': 0,
            'mode': 0
        }
    })


class SMSSelectMessageFormat(Command):
    """
    Select SMS message format.
    """
    PDU_MODE = ValueConstant(0)
    TEXT_MODE = ValueConstant(1)

    TEST_COMMAND = ValueConstant({
        'command': 'AT+CMGF=?',
        'response': '+CMGF: (list of supported <mode>s)'
    })
    READ_COMMAND = ValueConstant({
        'command': 'AT+CMGF?',
        'response': '+CMGF: <mode>'
    })
    WRITE_COMMAND = ValueConstant({
        'command': 'AT+CMGF=[<mode>]',
        'params': {
            'mode': 0
        }
    })


class SMSDeleteMessage(Command):
    """
    Delete SMS message.
    """
    maxResponseTime = 25

    DELETE_AT_INDEX = ValueConstant(0)
    DELETE_READ = ValueConstant(1)
    DELETE_READ_SENT = ValueConstant(2)
    DELETE_SENT_UNSENT = ValueConstant(3)
    DELETE_ALL = ValueConstant(4)

    TEST_COMMAND = ValueConstant({
        'command': 'AT+CMGD=?',
        'response': '+CMGD: (list of supported <index>s),(list of supported <delflag>s)'
    })
    WRITE_COMMAND = ValueConstant({
        'command': 'AT+CMGD=<index>[,<delflag>]',
        'response': '+CMGF: <mode>',
        'params': {
            'mode': 0
        }
    })
