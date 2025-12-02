#!/bin/bash

OPT_STRING="y:d:"

min_year=2015
max_year=$(date +%Y)
min_day=1
max_day=12
year=0
day=0
help_function()
{
   echo ""
   echo "Usage: $0 -y YEAR -d DAY"
   echo -e "\t-y Four digit year between ${min_year} and ${max_year} (inclusive)"
   echo -e "\t-d One or two digit day between ${min_day} and ${max_day} (inclusive)"
   exit 1 # Exit script after printing help
}

while getopts ${OPT_STRING} opt; do
  case ${opt} in
    y)
      year=$((OPTARG))
      if [ "$((year))" -lt "$((min_year))" ]; then
        echo "year must be greater than or equal to ${min_year}"
        exit 1
      fi
      if [ "$((year))" -gt "$((max_year))" ]; then
        echo "year must be less than or equal to ${max_year}"
        exit 1
      fi
      ;;
    d)
      day=$((OPTARG))
      if [ "$((day))" -lt "$((min_day))" ]; then
        echo "day must be greater than or equal to ${min_day}"
        exit 1
      fi
      if [ "$((day))" -gt "$((max_day))" ]; then
        echo "day must be less than or equal to ${max_day}"
        exit 1
      fi
      ;;
    ?)
      echo "Invalid option: -${OPTARG}."
      help_function
      ex  it 1
      ;;
  esac
done

if [ ! -z "${year}" ] && [ ! -z "${day}" ]; then
  python_file_name="/Users/chris/PycharmProjects/adventofcode/python/${year}/aoc${year}day${day}.py"
  resource_file_name="/Users/chris/PycharmProjects/adventofcode/resources/${year}/inputd${day}.txt"
  resource_a_file_name="/Users/chris/PycharmProjects/adventofcode/resources/${year}/inputd${day}-a.txt"

  if ! test -f "${python_file_name}"; then
    template_value=$(cat /Users/chris/PycharmProjects/adventofcode/resources/python-template.txt)
    file_contents=${template_value//<<YEAR>>/$year}
    file_contents=${file_contents//<<DAY>>/$day}
    echo "$file_contents" > ${python_file_name}
  fi

  if ! test -f "${resource_file_name}"; then
    touch "${resource_file_name}"
  fi

  if ! test -f "${resource_a_file_name}"; then
    touch "${resource_a_file_name}"
  fi
fi