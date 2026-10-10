# Week 3 Assignment: Grade Reporter & Bug Hunt

- `grade_reporter.py`: loops through a list of scores, prints a grade for each, and calculates the pass count, fail count, and average.
- `bug_hunt.py`: a broken program that adds up 1 to 5, fixed with three `# BUG:` comments explaining each fix.

The hardest bug to find in Part B was the third one, where the loop used `count < 5` instead of `count <= 5`. I knew something was wrong because the program printed 10 with no error message, but the correct answer is 15. I checked the loop by hand and saw that it stopped before adding the number 5.