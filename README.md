# Weight Tracker v1.4.2
### Created by [Aaron Ramos](https://aar0m.github.io/portfolio/) 
A tool to log calories, protein, and track weight using Python.  
Based on [Expense Tracking App Project](https://youtu.be/HTD86h69PtE?t=0) by [pixegami](https://www.youtube.com/@pixegami)  

## How to Use
Download the repository and execute `weight-tracker.py` on some terminal. Doing this will prompt you to a *"home screen"* with mutliple options. Entering the value associated with each prompt will lead to a series of other instructions related to that prompt.

1. **Log Calories** - *gets and stores `Snack`/`Meal` calories and protein to `calorie_XX-20XX.csv` and `weight20XX.csv`*
2. **View Calories** - *shows average calories and protein based on chosen option (day, week, month)*
3. **Log Weight** - *gets and stores user's `Weight` to `weight20XX.csv`*
4. **View Weight** - *shows average weight based on chosen option (day, week, month)*
5. **View 20XX Food Log** - *lists all `Snack`/`Meal` entries*
6. **Exit** - *exits the program*

For convenience, all calorie and weight sheets are stored in the `/tracker-sheets` directory.

## v1.4.3 Header Update
- Fix print statements of headers

## v1.4.2 String Bugfix
- Fixed bug from incompatible character inputs for `getCal` and `getWeight` functions
- Fixed exception handling for `UnboundLocalError` when logging calories and weights

## v1.4.1 Critical Bugfix
- Fixed bug due to missing directories

## v1.4.0 Calorie Update
- Moved formatting, calorie, and weight functions to dedicated Python files
- Moved yearly calorie `.csv` files into months under a year directory
- Updated naming conventions for calorie and weight functions as a result
- Fixed exception handling for `IndexError` when getting logging food
- Added month separators when listing yearly food log
- Added feature to view total calories and protein consumed on the day (`cal.summToday()`)
- Added feature to view total and average calories and protein consumed over a week (`cal.summWeek()`)
- Added feature to view total and average calories and protein consumed over a month (`cal.summMonth()`)

## v1.3.2 Bugfix
- Fixed f-string `SyntaxError` by replacing double block quotes

## v1.3.1 Bugfix
- Added exception to `FileNotFoundError`
- Added exception handling for instances where `weight20XX.csv` doesn't exist
- Moved sheets to new folder `/tracker-sheets`

## v1.3.0 Update
- Added feature to view average weight for the current month (`summWeighMonth()`)
- Added feature to view average weight over the year and average monthly weight (`summWeightYear()`)
- Added calendar weight (`summWeightCalendar()`)
- Monthly now provides average difference

## v1.2.0 Update
- Added **View Weight** interface so user can now choose to view day-of weight (`summWeightToday()`) or average weight over the week (`summWeightWeek()`)

## v1.1.1 Bugfix
- Fixed instance where `summWeightToday()` prints incorrect date if no weight is logged for that day (now shows most recent weight entry and reminds user to log their weight today)
- Moved `calorie_XX-20XX.csv` and `weight20XX.csv` to folder `calorie-sheets` and `weight-sheets`

## v1.1.0 Update
- Added function to calculate average weight over a week/7 day period (`summWeightWeek()`)

## v1.0.0 Release
- Added functions for `Snack`/`Meal` logging and tracking (`getCal()`, `saveCal()`, `readCalList()`, `summCal()`, `summCalDetails()`)
- Added functions for `Weight` logging and tracking (`getWeight()`, `saveWeight()`, `readWeightList()`, `summWeightToday()`)

## Classes
### `Snack`
- Date logged
- Type (`Snack`/`Meal`)
- Name of `Snack`
- Servings of `Snack` consumed
- Calories and protein per serving
- Total calories and protein consumed from servings of `Snack` eaten

### `Meal`
- Date logged
- Type (`Snack`/`Meal`)
- Description of `Meal`
- Calories and protein in `Meal`

### `Weight`
- Date weight logged
- Weight value (lbs)
