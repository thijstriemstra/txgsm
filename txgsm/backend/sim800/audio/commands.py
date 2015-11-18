"""
Audio commands for SIM800.
"""

from twisted.protocols.amp import Command, Integer, ListOf


class MicrophoneGainLevelTest(Command):
    """
    Get ranges for microphone gain levels and channels.
    """
    response = [
        ('channels', ListOf(Integer())),
        ('gainLevels', ListOf(Integer()))
    ]


class MicrophoneGainLevelRead(Command):
    """
    Get microphone gain level for each channel.
    """
    response = [
        ('levels', ListOf(ListOf(Integer())))
    ]


class MicrophoneGainLevelWrite(Command):
    """
    Change microphone gain level for channel.
    """
    arguments = [
        ('channel', Integer()),
        ('gainLevel', Integer())
    ]
    requiresAnswer = False


class MuteControlTest(Command):
    """
    Get ranges and parameters for mute control.
    """
    response = [
        ('modes', ListOf(Integer()))
    ]


class MuteControlRead(Command):
    """
    Get mute mode.
    """
    response = [
        ('mode', Integer())
    ]


class MuteControlWrite(Command):
    """
    Change mute.
    """
    arguments = [
        ('mode', Integer())
    ]
    requiresAnswer = False


class OpenCloseMicrophoneTest(Command):
    """
    Get ranges and parameters to open or close the microphone.
    """
    response = [
        ('modes', ListOf(Integer()))
    ]


class OpenCloseMicrophoneRead(Command):
    """
    Get current microphone activity mode.
    """
    response = [
        ('mode', Integer())
    ]


class OpenCloseMicrophoneWrite(Command):
    """
    Open or close the microphone.
    """
    arguments = [
        ('mode', Integer())
    ]
    requiresAnswer = False


class MonitorSpeakerModeExecution(Command):
    """
    Set monitor speaker mode.
    """
    arguments = [
        ('mode', Integer())
    ]
    requiresAnswer = False


class MonitorSpeakerLoudnessExecution(Command):
    """
    Set monitor speaker loudness.
    """
    arguments = [
        ('volume', Integer())
    ]
    requiresAnswer = False


class LoudspeakerVolumeLevelTest(Command):
    """
    Get supported ranges and parameters for the loudspeaker volume level.
    """
    response = [
        ('levelRange', ListOf(Integer()))
    ]


class LoudspeakerVolumeLevelRead(Command):
    """
    Get loudspeaker volume level.
    """
    response = [
        ('level', Integer())
    ]


class LoudspeakerVolumeLevelWrite(Command):
    """
    Change the loudspeaker volume level.
    """
    arguments = [
        ('level', Integer())
    ]
    requiresAnswer = False


class RingerSoundLevelTest(Command):
    """
    Get supported ranges and parameters for the ringer sound level.
    """
    response = [
        ('levelRange', ListOf(Integer()))
    ]


class RingerSoundLevelRead(Command):
    """
    Get ringer sound level.
    """
    response = [
        ('level', Integer())
    ]


class RingerSoundLevelWrite(Command):
    """
    Change the ringer sound level.
    """
    arguments = [
        ('level', Integer())
    ]
    requiresAnswer = False


class AlertSoundModeTest(Command):
    """
    Get supported ranges and parameters for the alert sound mode.
    """
    response = [
        ('modeRange', ListOf(Integer()))
    ]


class AlertSoundModeRead(Command):
    """
    Get alert sound mode.
    """
    response = [
        ('mode', Integer())
    ]


class AlertSoundModeWrite(Command):
    """
    Change the alert sound mode.
    """
    arguments = [
        ('mode', Integer())
    ]
    requiresAnswer = False


class AlertSoundSelectTest(Command):
    """
    Get supported ranges and parameters for the alert sound selection.
    """
    response = [
        ('soundTypes', ListOf(Integer())),
        ('playBackModes', ListOf(Integer()))
    ]


class AlertSoundSelectRead(Command):
    """
    Get selected alert sound.
    """
    response = [
        ('soundType', Integer()),
        ('playbackMode', Integer())
    ]


class AlertSoundSelectWrite(Command):
    """
    Change the alert sound.
    """
    arguments = [
        ('soundType', Integer()),
        ('playbackMode', Integer(optional=True))
    ]
    requiresAnswer = False
