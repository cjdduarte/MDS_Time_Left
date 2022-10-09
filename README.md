<b>Bug Report:</b> https://github.com/cjdduarte/MDS_Time_Left/issues

<b>#### New Change:</b>

<b>+ dayCutoff deprecated</b>

<b>#### About:</b>

This addon shows extra information of the due cards and returns the expected time to finalize (Due+New).

<b>Before:</b>

<img src="https://i.ibb.co/C2yGtsn/before.png" alt="Before">

<b>After:</b>

<img src="https://i.ibb.co/QffdL8s/after.png" alt="After">

<b>#### Configuration option:</b>

The default steps for "New" Anki cards are 1min and 10min meaning that you see New cards actually a minimum of <b>TWO</b> times that day.
You can now configure how many times new cards will be counted.

<b>CountTimesNew [number]:</b>

CountTimesNew = 1 (old version)

Quantify '1' time the "new card" time | Example: Steps (10 1440)

CountTimesNew = 2 (default)

Quantify '2' times the "new card" time | Example: Steps (1 10)

CountTimesNew = n (replace "n" with the number of rotations of the same day)

Quantify 'n' times the "new card" time | Example: Steps (1 10 10 20 30...) => n=5

<b>Number colors [Name]:</b>

<a href="https://www.w3schools.com/colors/colors_groups.asp">Color Names Sorted by Color Groups</a>

All modern browsers support the following 140 color names (click on a color name, or a hex value, to view the color as the background-color along with different text colors):

Copyright(C)| Carlos Duarte

Based on | Dmitry Mikheev code, in add-on "More decks overview stats"

Based on | calumks code, in add-on https://github.com/calumks/anki-deck-stats

License | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

Source in | https://github.com/cjdduarte/MDS_Time_Left

<b> #### Change Log:</b>

v1.9 - 2022-10-09 + dayCutoff deprecated (Tanks @khonkhortisan)

v1.8 - 2022-05-20 + Night mode compatibility.

v1.7 - 2021-01-27 + Clean code (removed compatibility with Anki 2.0).

v1.6 - 2020-03-31 + Adjust Grammar and translation.

v1.5 - 2020-01-21 + Change the number colors in the configuration options.

v1.4 - 2019-12-26 + New configuration option (tanks @MedAnki)

v1.3 - 2019-12-09 - Easier to the user change the colors (tanks @renbosa)

v1.2 - 2019-02-27 - Indentation

v1.1 - 2019-02-21 - Color Correction and unified code

v1.0 - 2019-02-20 - Initial Release