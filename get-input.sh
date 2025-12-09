SESSION_TOKEN=''
YEAR=$1
DAY=$2

curl https://adventofcode.com/$YEAR/day/$DAY/input -b "session=$SESSION_TOKEN" -o input.txt


