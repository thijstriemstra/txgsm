"""
TTS (text-to-speech) support for SIM800.
"""

from twisted.protocols.amp import CommandLocator

from txgsm.backend.sim800.tts import commands


class TTSManager(CommandLocator):
    """
    TTS Application.
    """

    @commands.PlaybackSettingsTest.responder
    def playbackSettingsTest(self):
        """
        Get list of parameters and value ranges for TTS playback settings.
        """
        atCommandName = 'AT+CTTSPARAM=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CTTSPARAM: (0-100),(0-3),(1-100),(1-100),(0,1)'

        # return AT command result
        return {
            'volumeRange': [0, 100],
            'modeRange': [0, 3],
            'pitchRange': [1, 100],
            'speedRange': [1, 100],
            'channelRange': [0, 1]
        }


    @commands.PlaybackSettingsRead.responder
    def playbackSettingsRead(self):
        """
        Get TTS playback settings.
        """
        atCommandName = 'AT+CTTSPARAM?'

        # XXX: call AT command

        # XXX: parse AT command result
        actualResponse = '+CTTSPARAM: 50,0,50,50,0'
        response = '+CTTSPARAM: <volume>,<mode>,<pitch>,<speed>,<channel>'
        volume = mode = channel = 0
        pitch = speed = 1

        # return AT command result
        return {
            'volume': volume,
            'mode': mode,
            'pitch': pitch,
            'speed': speed,
            'channel': channel
        }


    @commands.PlaybackSettingsWrite.responder
    def playbackSettingsWrite(self, volume=50, mode=0, pitch=50, speed=50,
                              channel=None):
        """
        Change TTS playback settings.

        :param volume: Playback volume. Range is 0-100, the default is 50.
        :type volume: int
        :param mode: Playback mode. Range is 0-3. Default is 0.
        :type mode: int
        :param pitch: Playback pitch. Range is 1-100. Default is 50.
        :type pitch: int
        :param speed: Playback speed. Range is 1-100. Default is 50.
        :type speed: int
        :param channel: Playback channel (optional).
        :type channel: int
        """
        atCommandName = 'AT+CTTSPARAM=<volume>,<mode>,<pitch>,<speed>[,<channel>]'

        # XXX: encode command
        
        # XXX: call AT command

        return {}


    @commands.OperationRead.responder
    def operationRead(self):
        """
        Get TTS playback status.
        """
        atCommandName = 'AT+CTTS?'

        # XXX: parse AT command result
        actualResponse = '+CTTS: 0'
        response = '+CTTS: <status>'

        return {'status': 0}


    @commands.OperationWrite.responder
    def operationWrite(self, mode, text=None):
        """
        Start/stop TTS message playback.

        :param mode:
        :type mode: int
        :param text: The text which is synthetized to speech to be played,
            maximum data length is 956 Bytes.
        :type text: string
        """
        atCommandName = 'AT+CTTS=<mode>[,<text>]'

        return {}


    @commands.EnableDuringIncomingCallRingTest.responder
    def enableDuringIncomingCallRingTest(self):
        """
        Get list of parameters and value ranges for TTS playback during
        incoming call ring.
        """
        atCommandName = 'AT+CTTSRING=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CTTSRING: (0,1)'

        # return AT command result
        return {
            'modeRange': [0, 1]
        }


    @commands.EnableDuringIncomingCallRingRead.responder
    def enableDuringIncomingCallRingRead(self):
        """
        Get status of TTS playback during incoming call ring.
        """
        atCommandName = 'AT+CTTSRING?'

        # XXX: call AT command

        # XXX: parse AT command result
        actualResponse = '+CTTSRING: 0'
        response = '+CTTSRING: <status>'

        return {'mode': 0}


    @commands.EnableDuringIncomingCallRingWrite.responder
    def enableDuringIncomingCallRingWrite(self, mode):
        """
        Enable/disable TTS playback during incoming call ring.

        :param mode: Whether to enable or disable TTS.
        :type mode: int
        """
        atCommandName = 'AT+CTTSRING=<mode>'

        return {}
