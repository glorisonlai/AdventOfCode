use regex::Regex;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

struct Target {
    x: (i32, i32),
    y: (i32, i32),
}

fn main() {
    println!("AoC 2021 Day 17!");
    println!("Part 1: {:?}", part_1("input.txt"));
}

fn part_1(filename: &str) -> (i32, i32) {
    let buffer = read_lines(filename);
    if buffer.is_err() {
        return (0, 0);
    }
    let target: Target = parse_target(&buffer.unwrap().next().unwrap().unwrap());
    println!("{:?}", target.y);
    return (0, 0);
}

fn parse_target(line: &str) -> Target {
    let re = Regex::new(r"^target area: x=(-?\d*)..(-?\d*), y=(-?\d*)..(-?\d*)$").unwrap();
    let caps = re.captures(line).unwrap();
    return Target {
        x: (
            caps[1].parse::<i32>().unwrap(),
            caps[2].parse::<i32>().unwrap(),
        ),
        y: (
            caps[3].parse::<i32>().unwrap(),
            caps[4].parse::<i32>().unwrap(),
        ),
    };
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
