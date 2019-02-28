# -*- coding: utf-8 -*-
#Copyright(C)	| Carlos Duarte
#Based 1 on    	| Dmitry Mikheev code, in add-on "More decks overview stats"
#Based 2 on    	| calumkscode, in add-on https://github.com/calumks/anki-deck-stats
#License       	| GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
#Source in     	| https://github.com/cjdduarte/MDS_Time_Left

import anki
import aqt

def renderStats(self, _old):
    # Get due and new cards
    new = 0
    lrn = 0
    due = 0

    for tree in self.mw.col.sched.deckDueTree():
        new += tree[4]
        lrn += tree[3]
        due += tree[2]
    total = new + lrn + due

    # Get studdied cards
    cards, thetime = self.mw.col.db.first(
            """select count(), sum(time)/1000 from revlog where id > ?""",
            (self.mw.col.sched.dayCutoff - 86400) * 1000)

    cards 	= cards or 0
    thetime = thetime or 0

    speed 	= cards * 60 / max(1, thetime)
    minutes = int(total / max(1, speed))

    buf = "<div style='display:table;padding-top:1.5em;'>" \
        + "<div style='display:table-cell;'> " \
        + _old(self) + "<hr>" \
        + _("New Cards") \
        + ": &nbsp; <font color=#0000aa> %(d)s</font>" % dict(d=new) \
        + " &nbsp; " + _("Learn") \
        + ": &nbsp; <font color=#aa0000>%(c)s</font>" % dict(c=lrn) \
        + " &nbsp; <span style='white-space:nowrap;'>" + _("To Review") \
        + ": &nbsp; <font color=#aa0000>%(c)s</font>" % dict(c=due) \
        + "</span>" \
        + " &nbsp; <br><span style='white-space:nowrap;'>" + _("Due") \
        + ": &nbsp; <b style=color:#00aa00>%(c)s</b> " % dict(c=(lrn+due)) \
        + "</span> " \
        + " &nbsp; <span style='white-space:nowrap;'>" + _("Total") \
        + ": &nbsp; <b style=color:#888888>%(c)s</b>" % dict(c=(total)) \
        + "</span></div>" \
        + "<div style='display:table-cell;vertical-align:middle;" \
        + "padding-left:2em;'>" \
        + "<span style='white-space:nowrap;'>" + _("Average") \
        + ":<br> " + _("%.01f cards/minute") % (speed) \
        + "</span><br><br>" \
        + _("More") + "&nbsp;" + ngettext(
             "%s minute.", "%s minutes.", minutes) % (minutes) \
        + "</div></div>"
    return buf

aqt.deckbrowser.DeckBrowser._renderStats = anki.hooks.wrap(
    aqt.deckbrowser.DeckBrowser._renderStats, renderStats, 'around')