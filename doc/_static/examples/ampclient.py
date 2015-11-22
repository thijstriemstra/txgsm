import logging
from pprint import pprint

from twisted.internet import reactor
from twisted.internet.defer import DeferredList
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.protocols.amp import AMP

from txgsm.backend.sim800.tts import commands as ttscommands
from txgsm.backend.sim800.audio import commands as audiocommands

level = logging.DEBUG
logging.basicConfig(level=level)
logging.getLogger('rfc2217').setLevel(level)


def doOperations():
    destination = TCP4ClientEndpoint(reactor, '127.0.0.1', 1234)

    # operation read
    operationRead = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(ttscommands.OperationRead)
    operationRead.addCallback(connected)
    def summed(result):
        return result['status']
    operationRead.addCallback(summed)

    # operation write
    operationWrite = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(ttscommands.OperationWrite,
            mode=0, text="hello world")
    operationWrite.addCallback(connected)

    # playbacksettings test
    playbackSettingsTest = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(ttscommands.PlaybackSettingsTest)
    playbackSettingsTest.addCallback(connected)

    # playbacksettings read
    playbackSettingsRead = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(ttscommands.PlaybackSettingsRead)
    playbackSettingsRead.addCallback(connected)

    # playbacksettings write
    playbackSettingsWrite = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(ttscommands.PlaybackSettingsWrite,
            volume=5, mode=2, pitch=5, speed=5, channel=1)
    playbackSettingsWrite.addCallback(connected)

    # enableDuringIncomingCallRing test
    enableDuringIncomingCallRingTest = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(ttscommands.EnableDuringIncomingCallRingTest)
    enableDuringIncomingCallRingTest.addCallback(connected)

    # enableDuringIncomingCallRing read
    enableDuringIncomingCallRingRead = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(ttscommands.EnableDuringIncomingCallRingRead)
    enableDuringIncomingCallRingRead.addCallback(connected)

    # enableDuringIncomingCallRing write
    enableDuringIncomingCallRingWrite = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(ttscommands.EnableDuringIncomingCallRingWrite,
            mode=1)
    enableDuringIncomingCallRingWrite.addCallback(connected)


    # microphoneGainLevel test
    microphoneGainLevelTest = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.MicrophoneGainLevelTest)
    microphoneGainLevelTest.addCallback(connected)

    # microphoneGainLevel read
    microphoneGainLevelRead = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.MicrophoneGainLevelRead)
    microphoneGainLevelRead.addCallback(connected)

    # microphoneGainLevel write
    microphoneGainLevelWrite = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.MicrophoneGainLevelWrite,
            channel=0, gainLevel=5)
    microphoneGainLevelWrite.addCallback(connected)

    # muteControl test
    muteControlTest = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.MuteControlTest)
    muteControlTest.addCallback(connected)

    # muteControl read
    muteControlRead = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.MuteControlRead)
    muteControlRead.addCallback(connected)

    # muteControl write
    muteControlWrite = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.MuteControlWrite,
            mode=0)
    muteControlWrite.addCallback(connected)

    # OpenCloseMicrophone test
    openCloseMicrophoneTest = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.OpenCloseMicrophoneTest)
    openCloseMicrophoneTest.addCallback(connected)

    # OpenCloseMicrophone read
    openCloseMicrophoneRead = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.OpenCloseMicrophoneRead)
    openCloseMicrophoneRead.addCallback(connected)

    # OpenCloseMicrophone write
    openCloseMicrophoneWrite = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.OpenCloseMicrophoneWrite,
            mode=0)
    openCloseMicrophoneWrite.addCallback(connected)

    # MonitorSpeakerMode execution
    monitorSpeakerModeExecution = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.MonitorSpeakerModeExecution,
            mode=0)
    monitorSpeakerModeExecution.addCallback(connected)

    # MonitorSpeakerLoudness execution
    monitorSpeakerLoudnessExecution = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.MonitorSpeakerLoudnessExecution,
            volume=5)
    monitorSpeakerLoudnessExecution.addCallback(connected)

    # LoudspeakerVolumeLevel test
    loudspeakerVolumeLevelTest = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.LoudspeakerVolumeLevelTest)
    loudspeakerVolumeLevelTest.addCallback(connected)

    # loudspeakerVolumeLevel read
    loudspeakerVolumeLevelRead = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.LoudspeakerVolumeLevelRead)
    loudspeakerVolumeLevelRead.addCallback(connected)

    # loudspeakerVolumeLevel write
    loudspeakerVolumeLevelWrite = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.LoudspeakerVolumeLevelWrite,
            level=40)
    loudspeakerVolumeLevelWrite.addCallback(connected)

    # RingerSoundLevel test
    ringerSoundLevelTest = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.RingerSoundLevelTest)
    ringerSoundLevelTest.addCallback(connected)

    # RingerSoundLevel read
    ringerSoundLevelRead = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.RingerSoundLevelRead)
    ringerSoundLevelRead.addCallback(connected)

    # RingerSoundLevel write
    ringerSoundLevelWrite = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.RingerSoundLevelWrite,
            level=40)
    ringerSoundLevelWrite.addCallback(connected)

    # AlertSoundMode test
    alertSoundModeTest = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.AlertSoundModeTest)
    alertSoundModeTest.addCallback(connected)

    # AlertSoundMode read
    alertSoundModeRead = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.AlertSoundModeRead)
    alertSoundModeRead.addCallback(connected)

    # AlertSoundMode write
    alertSoundModeWrite = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.AlertSoundModeWrite,
            mode=1)
    alertSoundModeWrite.addCallback(connected)

    # AlertSoundSelect test
    alertSoundSelectTest = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.AlertSoundSelectTest)
    alertSoundSelectTest.addCallback(connected)

    # AlertSoundSelect read
    alertSoundSelectRead = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.AlertSoundSelectRead)
    alertSoundSelectRead.addCallback(connected)

    # AlertSoundSelect write
    alertSoundSelectWrite = connectProtocol(destination, AMP())
    def connected(ampProto):
        return ampProto.callRemote(audiocommands.AlertSoundSelectWrite,
            soundType=1, playbackMode=1)
    alertSoundSelectWrite.addCallback(connected)

    def done(result):
        print('Operation result:')
        pprint(result)
        reactor.stop()

    operations = [operationRead, operationWrite, playbackSettingsTest,
        playbackSettingsRead, playbackSettingsWrite,
        enableDuringIncomingCallRingTest, enableDuringIncomingCallRingRead,
        enableDuringIncomingCallRingWrite, microphoneGainLevelTest,
        microphoneGainLevelRead, microphoneGainLevelWrite, muteControlTest,
        muteControlRead, muteControlWrite, openCloseMicrophoneTest,
        openCloseMicrophoneRead, openCloseMicrophoneWrite,
        monitorSpeakerModeExecution, monitorSpeakerLoudnessExecution,
        loudspeakerVolumeLevelTest, loudspeakerVolumeLevelRead,
        loudspeakerVolumeLevelWrite, ringerSoundLevelTest,
        ringerSoundLevelRead, ringerSoundLevelWrite, alertSoundModeTest,
        alertSoundModeRead, alertSoundModeWrite, alertSoundSelectTest,
        alertSoundSelectRead, alertSoundSelectWrite
    ]

    DeferredList(operations).addCallback(done)


if __name__ == '__main__':
    doOperations()
    reactor.run()
