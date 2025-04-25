# -*- coding: utf-8 -*-
# Copyright(C)   | Carlos Duarte
# Based 1 on     | Dmitry Mikheev code, in add-on "More decks overview stats"
# Based 2 on     | calumkscode, in add-on https://github.com/calumks/anki-deck-stats
# License        | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Source in      | https://github.com/cjdduarte/MDS_Time_Left

import anki
# from anki.lang import _, ngettext
import aqt
from aqt import mw, theme
from aqt.utils import tooltip
from anki import version as anki_version
from aqt.utils import tr

#-------------Configuration------------------
config = mw.addonManager.getConfig(__name__)
CountTimesNew = config['CountTimesNew']
DaysToConsider = config['DaysToConsider']
#-------------Configuration------------------

def generate_style():
    """Generate the required CSS style based on the theme mode."""
    if theme.theme_manager.night_mode:
        color_config_keys = ['NewColorDark', 'ReviewColorDark', 'LearnColorDark', 'TotalDueColorDark', 'TotalColorDark']
    else:
        color_config_keys = ['NewColorLight', 'ReviewColorLight', 'LearnColorLight', 'TotalDueColorLight', 'TotalColorLight']

    style_elements = [
        ".new-color { color:" + config[color_config_keys[0]] + ";}",
        ".review-color { color:" + config[color_config_keys[1]] + ";}",
        ".learn-color { color:" + config[color_config_keys[2]] + ";}",
        ".totaldue-color { color:" + config[color_config_keys[3]] + ";}",
        ".total-color { color:" + config[color_config_keys[4]] + ";}"
    ]

    return "<style type=\"text/css\">" + ' '.join(style_elements) + "</style>"

def renderStats(self, _old):

    txtNew      = tr.statistics_counts_new_cards()
    txtLrn      = tr.card_stats_review_log_type_learn()
    txtDue      = tr.card_stats_review_count()
    txtLrnDue   = tr.statistics_due_count()
    txtTotal    = tr.statistics_total()
    txtAverage  = tr.statistics_average()
    txtMore     = tr.studying_more().lower()

    txtDaysCount = tr.statistics_in_time_span_days(DaysToConsider)  # Usando uma tradução existente para 'days'
    # txtToday = tr.statistics_today_title()

    if DaysToConsider > 1:
        txtAverage = f"{txtAverage} ({txtDaysCount})"

    # Get due and new cards
    new, lrn, due = 0, 0, 0
    for tree in self.mw.col.sched.deckDueTree():
        new += tree[4]
        lrn += tree[3]
        due += tree[2]

    total        = (CountTimesNew*new) + lrn + due
    totalDisplay = new + lrn + due

    # Get studied cards
    # anki_point_version = int(anki_version.split(".")[2])
    # query_time_param = (self.mw.col.sched.day_cutoff if anki_point_version > 49 else self.mw.col.sched.dayCutoff) - 86400
    # query_time_param = self.mw.col.sched.day_cutoff - 86400
    total_seconds = 86400 * (DaysToConsider)  # Calcula o total de segundos para os dias configurados
    query_time_param = self.mw.col.sched.day_cutoff - total_seconds
    cards, thetime   = self.mw.col.db.first("""select count(), sum(time)/1000 from revlog where id > ?""", query_time_param * 1000)

    cards           = cards or 0
    thetime         = thetime or 0
    speed           = cards * 60 / max(1, thetime)
    formatted_speed = "{:.01f}".format(speed)
    txtCardsMin     = tr.statistics_cards_per_min(formatted_speed)

    minutes         = int(total / max(1, speed))
    txtMinutes      = tr.studying_minute(minutes).replace('.', '')

    if config.get("ShowTimeLeft", True):
        timeLeftDisplay = f"{txtMinutes} {txtMore}"
    else:
        timeLeftDisplay = ""

    buf = generate_style() + """
        <div style='display:table;padding-top:1.5em;'>
            <div style='display:table-cell;'> 
                {} 
                <hr>
                &nbsp;{}:&nbsp; <b class='new-color'> {}</b>
                &nbsp;{}:&nbsp; <b class='learn-color'> {}</b>
                &nbsp;{}:&nbsp; <b class='review-color'> {}</b>
                &nbsp;{}:&nbsp; <b class='totaldue-color'> {}</b>
                &nbsp;{}:&nbsp; <b class='total-color'> {}</b>
            </div>
            <div style='display:table-cell;vertical-align:middle;padding-left:2em;'>
                {}: <br> {}
                <br><br>
                {}
            </div>
        </div>
    """.format(_old(self), txtNew, new, txtLrn, lrn, txtDue, due, txtLrnDue, lrn+due, txtTotal, totalDisplay, txtAverage, txtCardsMin, timeLeftDisplay)
    # """.format(_old(self), _("New"), new, _("Learn"), lrn, _("To Review"), due, _("Due"), lrn+due, _("Total"), totalDisplay, _("Average"), speed, _("Cards"), _("Minutes").replace("s", ""), str(ngettext("%s minute.", "%s minutes.", minutes) % minutes).replace(".", ""), _("More").lower())
    
    return buf

aqt.deckbrowser.DeckBrowser._renderStats = anki.hooks.wrap(
    aqt.deckbrowser.DeckBrowser._renderStats, renderStats, 'around')