"""
Audio support for SIM800 backend.
"""

from twisted.protocols.amp import CommandLocator
from twisted.python.constants import Values, ValueConstant

from txgsm.backend.sim800.audio import commands


class AudioConstants(Values):
    """
    """
    MAIN_AUDIO_CHANNEL = ValueConstant(0)
    AUX_AUDIO_CHANNEL = ValueConstant(1)
    MAIN_HANDSFREE_AUDIO_CHANNEL = ValueConstant(2)
    AUX_HANDSFREE_AUDIO_CHANNEL = ValueConstant(3)

    MUTE_OFF = ValueConstant(0)
    MUTE_ON = ValueConstant(1)

    REOPEN_MICROPHONE = ValueConstant(0)
    CLOSE_MICROPHONE = ValueConstant(1)

    STOP_RINGTONE = ValueConstant(0)
    START_RINGTONE = ValueConstant(1)

    NORMAL_MODE = ValueConstant(0)
    SILENT_MODE = ValueConstant(1)


class AudioManager(CommandLocator):
    """
    Audio manager.
    """

    @commands.MuteControlTest.responder
    def muteControlTest(self):
        """
        Get list of supported ranges for mute modes.
        """
        atCommandName = 'AT+CMUT=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CMUT: (0,1)'

        # return AT command result
        return {
            'modes': [0, 1]
        }


    @commands.MuteControlRead.responder
    def muteControlRead(self):
        """
        Get current mute mode.
        """
        atCommandName = 'AT+CMUT?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CMUT: <n>'

        # return AT command result
        return {
            'mode': 0
        }


    @commands.MuteControlWrite.responder
    def muteControlWrite(self, mode):
        """
        Change current mute mode.

        :param mode:
        :type mode: int
        """
        atCommandName = 'AT+CMUT=<n>'

        # XXX: call AT command

        return {}


    @commands.MicrophoneGainLevelTest.responder
    def microphoneGainLevelTest(self):
        """
        Get list of supported ranges for microphone channels and gain levels.
        """
        atCommandName = 'AT+CMIC=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CMIC: (list of supported <channel>s),(list of supported <gainlevel>s)'

        # return AT command result
        return {
            'channels': [0, 1, 2, 3],
            'gainLevels': [0, 1, 3, 4, 100]
        }


    @commands.MicrophoneGainLevelRead.responder
    def microphoneGainLevelRead(self):
        """
        Get current gain level for each channel.
        """
        atCommandName = 'AT+CMIC?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CMIC: (<channel0>,<gainlevel0>),...,(<channeln>,<gainleveln>)'

        # return AT command result
        return {
            'levels': [[0, 1], [1, 3]]
        }


    @commands.MicrophoneGainLevelWrite.responder
    def microphoneGainLevelWrite(self, channel, gainLevel):
        """
        Change current microphone gain level for channel.

        The default gain level of the main audio channel is ``10``.

        :param channel:
        :type channel: int
        :param gainLevel:
        :type gainLevel: int
        """
        atCommandName = 'AT+CMIC=<channel>,<gainlevel>'

        # XXX: call AT command

        # return AT command result
        return {}


    @commands.OpenCloseMicrophoneTest.responder
    def openCloseMicrophoneTest(self):
        """
        Get list of supported modes to open or close the microphone.
        """
        atCommandName = 'AT+CEXTERNTONE=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CEXTERNTONE: (0,1)'

        # return AT command result
        return {
            'modes': [0, 1]
        }


    @commands.OpenCloseMicrophoneRead.responder
    def openCloseMicrophoneRead(self):
        """
        Get current gain level for each channel.
        """
        atCommandName = 'AT+CEXTERNTONE?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CEXTERNTONE: <mode>'

        # return AT command result
        return {
            'mode': 0
        }


    @commands.OpenCloseMicrophoneWrite.responder
    def openCloseMicrophoneWrite(self, mode):
        """
        Open or close the microphone.

        :param mode:
        :type mode: int
        """
        atCommandName = 'AT+CEXTERNTONE=<mode>'

        # XXX: call AT command

        # return AT command result
        return {}


    @commands.MonitorSpeakerModeExecution.responder
    def monitorSpeakerModeExecution(self, mode):
        """
        Change monitor speaker mode.

        :param mode: Value from 0 to 9.
        :type mode: int
        """
        atCommandName = 'ATM{0}'.format(mode)

        # XXX: call AT command

        # return AT command result
        return {}


    @commands.MonitorSpeakerLoudnessExecution.responder
    def monitorSpeakerLoudnessExecution(self, volume):
        """
        Set monitor speaker loudness.

        :param volume: Value from 0 to 9.
        :type volume: int
        """
        atCommandName = 'ATL{0}'.format(volume)

        # XXX: call AT command

        # return AT command result
        return {}


    @commands.LoudspeakerVolumeLevelTest.responder
    def loudspeakerVolumeLevelTest(self):
        """
        Get range of supported loudspeaker volume levels.
        """
        atCommandName = 'AT+CLVL=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CLVL: (list of supported <level>s)'

        # return AT command result
        return {
            'levelRange': [0, 100]
        }


    @commands.LoudspeakerVolumeLevelRead.responder
    def loudspeakerVolumeLevelRead(self):
        """
        Get current loudspeaker volume level.
        """
        atCommandName = 'AT+CLVL?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CLVL: <level>'

        # return AT command result
        return {
            'level': 50
        }


    @commands.LoudspeakerVolumeLevelWrite.responder
    def loudspeakerVolumeLevelWrite(self, level):
        """
        Volume level of the loudspeaker.

        :param level: Manufacturer specific range (smallest value represents
            the lowest sound level) from 0 to 100.
        :type level: int
        """
        atCommandName = 'AT+CLVL=<level>'

        # XXX: call AT command

        # return AT command result
        return {}


    @commands.AlertSoundSelectTest.responder
    def alertSoundSelectTest(self):
        """
        Get range of supported alert sound modes.
        """
        atCommandName = 'AT+CALS=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CALS: (list of supported <n>s),(list of supported <switch>s)'

        # return AT command result
        return {
            'soundTypes': [0, 1, 2, 3],
            'playBackModes': [0, 1]
        }


    @commands.AlertSoundSelectRead.responder
    def alertSoundSelectRead(self):
        """
        Get current alert sound mode.
        """
        atCommandName = 'AT+CALS?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CALS: <n>,<switch>'

        # return AT command result
        return {
            'soundType': 1,
            'playbackMode': 1
        }


    @commands.AlertSoundSelectWrite.responder
    def alertSoundSelectWrite(self, soundType, playbackMode=None):
        """
        Change alert sound mode.

        :param soundType: Alert sound type.
        :type soundType: int
        :param playbackMode: Start/stop playing ring tone (optional).
        :type playbackMode: int
        """
        atCommandName = 'AT+CALS=<n>[,<switch>]'

        # XXX: call AT command

        # return AT command result
        return {}


    @commands.AlertSoundModeTest.responder
    def alertSoundModeTest(self):
        """
        Get range of supported alert sound modes.
        """
        atCommandName = 'AT+CALM=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CALM: (list of supported <mode>s)'

        # return AT command result
        return {
            'modeRange': [0, 1]
        }


    @commands.AlertSoundModeRead.responder
    def alertSoundModeRead(self):
        """
        Get current alert sound mode.
        """
        atCommandName = 'AT+CALM?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CALM: <mode>'

        # return AT command result
        return {
            'mode': 1
        }


    @commands.AlertSoundModeWrite.responder
    def alertSoundModeWrite(self, mode):
        """
        Change alert sound mode.

        :param mode: 
        :type mode: int
        """
        atCommandName = 'AT+CALM=<mode>'

        # XXX: call AT command

        # return AT command result
        return {}


    @commands.RingerSoundLevelTest.responder
    def ringerSoundLevelTest(self):
        """
        Get range of supported ringer sound levels.
        """
        atCommandName = 'AT+CRSL=?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CRSL: (list of supported <level>s)'

        # return AT command result
        return {
            'levelRange': [0, 100]
        }


    @commands.RingerSoundLevelRead.responder
    def ringerSoundLevelRead(self):
        """
        Get current loudspeaker volume level.
        """
        atCommandName = 'AT+CRSL?'

        # XXX: call AT command

        # XXX: parse AT command result
        response = '+CRSL: <level>'

        # return AT command result
        return {
            'level': 30
        }


    @commands.RingerSoundLevelWrite.responder
    def ringerSoundLevelWrite(self, level):
        """
        Change level of ringer sound.

        :param level: Manufacturer specific range (smallest value represents
            the lowest sound level) from 0 to 100.
        :type level: int
        """
        atCommandName = 'AT+CRSL=<level>'

        # XXX: call AT command

        # return AT command result
        return {}
