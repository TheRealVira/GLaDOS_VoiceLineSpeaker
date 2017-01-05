# GladosVoiceLineSpeaker
This python program will generate a mp3 file containing a random quote of GLaDOS!

## Requirements
 - [Python](https://www.python.org/downloads/)
 - [gTTS](https://pypi.python.org/pypi/gTTS)
 - [An operating system that is able to play music files...](https://distrochooser.de/?l=2)
 
## How it works
It picks a random line from the _vl_ file (which does contain all the quotes; thx to [the wiki](http://theportalwiki.com/wiki/GLaDOS_voice_lines) and [Notepad++](https://notepad-plus-plus.org/download/)) and uses that line as parameter for gTTS, which than will save it as _speech.mp3_.
