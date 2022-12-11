# Import the readr library
setwd("~/github/advent_of_code/2022/day_01")

verbose = FALSE

# read_lines() to read one line at a time
myData = readLines("input.txt", n = -1)

this_elf <- 0
max_calories <- 0

for (x in myData) {

  if (x == "") {

    if (verbose) {
      print(this_elf)
    }

    max_calories = max(c(max_calories, this_elf))
    this_elf <- 0

  } else {

    calories <- strtoi(x)
    this_elf <- this_elf + calories

  }

}

print(sprintf("max calories is %i", max_calories))
