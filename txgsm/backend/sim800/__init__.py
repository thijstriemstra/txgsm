"""
SIM800 backend.
"""

from twisted.protocols.amp import CommandLocator

from txgsm.backend.sim800.sms import SMSManager
from txgsm.backend.sim800.tts import TTSManager
from txgsm.backend.sim800.audio import AudioManager


class SIM800Locator(SMSManager, TTSManager, AudioManager):
    pass

