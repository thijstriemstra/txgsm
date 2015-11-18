"""
TTS commands.
"""

from twisted.python.constants import Values, ValueConstant
from twisted.protocols.amp import Command, Integer, String, ListOf


class TTSConstants(Values):
    IDLE_STATUS = ValueConstant(0)
    PLAY_STATUS = ValueConstant(1)

    STOP_SPEECH_PLAYBACK_MODE = ValueConstant(0)
    START_SPEECH_PLAYBACK_UCS2_MODE = ValueConstant(1)
    START_SPEECH_PLAYBACK_ASCII_MODE = ValueConstant(2)

    AUTO_READ_NUMBER_MODE = ValueConstant(0)
    AUTO_READ_TELEGRAM_MODE = ValueConstant(1)
    TELEGRAM_READ_MODE = ValueConstant(2)
    NUMBER_READ_MODE = ValueConstant(3)

    MAIN_CHANNEL = ValueConstant(0)
    AUX_CHANNEL = ValueConstant(1)

    DISABLE_PLAYBACK_MODE = ValueConstant(0)
    ENABLE_PLAYBACK_MODE = ValueConstant(1)


class OperationRead(Command):
    response = [('status', Integer())]


class OperationWrite(Command):
    arguments = [('mode', Integer()),
                 ('text', String(optional=True))]
    requiresAnswer = False


class PlaybackSettingsTest(Command):
    response = [
        ('volumeRange', ListOf(Integer())),
        ('modeRange', ListOf(Integer())),
        ('pitchRange', ListOf(Integer())),
        ('speedRange', ListOf(Integer())),
        ('channelRange', ListOf(Integer()))
    ]


class PlaybackSettingsRead(Command):
    response = [
        ('volume', Integer()),
        ('mode', Integer()),
        ('pitch', Integer()),
        ('speed', Integer()),
        ('channel', Integer())
    ]


class PlaybackSettingsWrite(Command):
    arguments = [
        ('volume', Integer()),
        ('mode', Integer()),
        ('pitch', Integer()),
        ('speed', Integer()),
        ('channel', Integer(optional=True))
    ]
    requiresAnswer = False


class EnableDuringIncomingCallRingTest(Command):
    response = [
        ('modeRange', ListOf(Integer()))
    ]


class EnableDuringIncomingCallRingRead(Command):
    response = [
        ('mode', Integer())
    ]


class EnableDuringIncomingCallRingWrite(Command):
    arguments = [
        ('mode', Integer())
    ]
    requiresAnswer = False
