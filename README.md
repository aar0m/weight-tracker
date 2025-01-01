# Weight Tracker v1.2.0 
A tool to log calories, protein, and track weight using Python.
### Created by [Aaron Ramos](https://aar0m.github.io/portfolio/) 
Based on [Expense Tracking App Project](https://youtu.be/HTD86h69PtE?t=0) by [pixegami](https://www.youtube.com/@pixegami)  

## How to Use
Download the repository and execute `weight-tracker.py` on some terminal. Doing this will prompt you to a *"home screen"* with mutliple options. Entering the value associated with each prompt will lead to a series of other instructions related to that prompt.

1. **Log Calories** - *gets and stores `Snack`/`Meal` calories and protein to `calorie20XX.csv` and `weight20XX.csv`*
2. **Log Weight** - *gets and stores user's `Weight` to `weight20XX.csv`*
3. **View 20XX Food Log** - *lists all `Snack`/`Meal` entries*
4. **View Daily Calories/Protein** - *lists all calories and protein(g) consumed each day*
5. **View Weight** - *shows average weight based on chosen option (day, week, month)*
6. **Exit** - *exits the program*

For convenience, all calorie and weight sheets are stored in directories `/calorie-sheets` and `/weight-sheets`

## v1.2.0 Update
- Added **View Weight** interface so user can now choose to view day-of weight (`summWeightToday()`) or average weight over the week (`summWeightWeek()`)

## v1.1.1 Bugfix
- Fixed instance where `summWeightToday()` prints incorrect date if no weight is logged for that day (now shows most recent weight entry and reminds user to log their weight today)
- Moved `calorie20XX.csv` and `weight20XX.csv` to folder `calorie-sheets` and `weight-sheets`

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
- Type (Snack/Meal)
- Description of `Meal`
- Calories and protein in `Meal`

### `Weight`
- Date weight logged
- Weight value (lbs)
