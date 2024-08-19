<b>Bug Report:</b> <a href="https://github.com/cjdduarte/MDS_Time_Left/issues">https://github.com/cjdduarte/MDS_Time_Left/issues</a>

<b>#### New Change:</b>

<b>+ Added 'DaysToConsider' configuration for multi-day review statistics</b>

<b>#### About:</b>

This addon shows extra information of the due cards and returns the expected time to finalize (Due+New).

<b>Before:</b>

<p align="center">
  <img src="https://i.ibb.co/JKzqR6H/image.png" alt="Before">
</p>

<b>After:</b>

<p align="center">
  <img src="https://i.ibb.co/Ptk82k1/image.png" alt="After">
</p>

<b>#### Configuration option:</b>

The default steps for "New" Anki cards are 1min and 10min meaning that you see New cards actually a minimum of <b>TWO</b> times that day.
You can now configure how many times new cards will be counted.

<b>CountTimesNew [number]:</b>

<ul>
  <li>CountTimesNew = 1 (old version)</li>
  <li>Quantify '1' time the "new card" time | Example: Steps (10 1440)</li>
  <li>CountTimesNew = 2 (default)</li>
  <li>Quantify '2' times the "new card" time | Example: Steps (1 10)</li>
  <li>CountTimesNew = n (replace "n" with the number of rotations of the same day)</li>
  <li>Quantify 'n' times the "new card" time | Example: Steps (1 10 10 20 30...) => n=5</li>
</ul>

<b>DaysToConsider [number]:</b>

This setting allows you to configure how many days of review data should be considered when calculating the estimated time left to study. By default, only the current day's data is used.

<ul>
  <li>DaysToConsider = 1 (default) | Consider only the current day's review data.</li>
  <li>DaysToConsider = 2 | Consider the current day and the previous day's review data.</li>
  <li>DaysToConsider = n | Consider the current day and the previous n-1 days' review data.</li>
</ul>

<b>ShowTimeLeft [boolean]:</b>

This setting allows you to toggle the display of the estimated time left for studying. Some users may find this information motivating, while others might prefer not to see it to reduce stress.

<ul>
  <li>ShowTimeLeft = true (default) | Display the time left to study.</li>
  <li>ShowTimeLeft = false | Do not display the time left to study.</li>
</ul>

<b>Number colors [Name]:</b> <a href="https://www.w3schools.com/colors/colors_groups.asp">Color Names Sorted by Color Groups</a>

All modern browsers support the following 140 color names (click on a color name, or a hex value, to view the color as the background-color along with different text colors):

<ul>
  <li>Copyright(C)| Carlos Duarte</li>
  <li>Based on | Dmitry Mikheev code, in add-on "More decks overview stats"</li>
  <li>Based on | calumks code, in add-on <a href="https://github.com/calumks/anki-deck-stats">add-on</a></li>
  <li>License | <a href="http://www.gnu.org/licenses/agpl.html">GNU AGPL</a>, version 3 or later;</li>
  <li><a href="https://github.com/cjdduarte/MDS_Time_Left">Source in</a></li>
</ul>

<b> #### Change Log:</b>

<ul>
  <li>v2.5 - 2024-08-19 - Added 'DaysToConsider' configuration for multi-day review statistics.</li>
  <li>v2.4 - 2024-04-11 - Added 'ShowTimeLeft' toggle for study time visibility.</li>
  <li>v2.3 - 2023-09-24 - Bug with version 23.10</li>
  <li>v2.2 - 2023-08-21 + Minor visual adjustments (Tanks @Okosh50)</li>
  <li>v2.1 - 2023-08-17 + Fully translated</li>
  <li>v2.0 - 2023-08-15 + New code (Clean)</li>
  <li>v1.9 - 2022-10-09 + dayCutoff deprecated (Tanks @khonkhortisan)</li>
  <li>v1.8 - 2022-05-20 + Night mode compatibility.</li>
  <li>v1.7 - 2021-01-27 + Clean code (removed compatibility with Anki 2.0).</li>
  <li>v1.6 - 2020-03-31 + Adjust Grammar and translation.</li>
  <li>v1.5 - 2020-01-21 + Change the number colors in the configuration options.</li>
  <li>v1.4 - 2019-12-26 + New configuration option (tanks @MedAnki)</li>
  <li>v1.3 - 2019-12-09 - Easier to the user change the colors (tanks @renbosa)</li>
  <li>v1.2 - 2019-02-27 - Indentation</li>
  <li>v1.1 - 2019-02-21 - Color Correction and unified code</li>
  <li>v1.0 - 2019-02-20 - Initial Release</li>
</ul>
