# jkl; will show answer or answer cards
# creds to faster-keys, handy keys, left hand reps because i either use them or scavenged code from them.
# (i don't actually know what i'm doing)

from aqt import mw
from aqt.reviewer import Reviewer

def leftHandKeys(self, evt):
    key = unicode(evt.text())


    if key in ["j","k","l",";"]:

        easeMap = { "j": 1, "k": 2, "l": 3, ";": 4}
        ease = min(easeMap[key], self.mw.col.sched.answerButtons(self.card))
        if self.state == "question":
            self._showAnswerHack()
        elif self.state == "answer":
            self._answerCard(ease)
    
    else:
        origKeyHandler(self, evt)    
        

origKeyHandler= Reviewer._keyHandler
Reviewer._keyHandler = leftHandKeys
