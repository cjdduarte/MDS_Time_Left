## Configuration

### CountTimesNew [number]
The default steps for "New" Anki cards are 1min and 10min, meaning that you see New cards actually a minimum of *TWO* times that day. This setting allows you to configure how many times new cards will be counted towards the total time estimate shown by the add-on.

**Values:**<br/>
- `"CountTimesNew" = 1`<br/>
  Quantify '1' time the "new card" time<br/>
  Example: Steps (10 1440)<br/>
- `"CountTimesNew" = 2` (default)<br/>
  Quantify '2' times the "new card" time<br/>
  Example: Steps (1 10)<br/>
- `"CountTimesNew" = n`<br/>
  Quantify 'n' times the "new card" time<br/>
  Example: Steps (1 10 10 20 30...)

### ShowTimeLeft [boolean]
This setting allows you to control whether the estimated time left to study is displayed. Some users may find this information motivating, while others may find it stressful.

**Values:**<br/>
- `"ShowTimeLeft" = true` (default)<br/>
  Display the time left to study.<br/>
- `"ShowTimeLeft" = false`<br/>
  Do not display the time left to study.<br/>
  When set to false, the add-on will not show the estimated time remaining in the current study session.

### Number colors [Name]
[Color Names Sorted by Color Groups](https://www.w3schools.com/colors/colors_groups.asp)<br/>
All modern browsers support the following 140 color names (click on a color name, or a hex value, to view the color as the background-color along with different text colors):
