use rayon::prelude::*;
use std::fs::File;
use std::io::{self, BufRead};
use std::iter::Sum;
use std::path::Path;

fn main() {
    println!("AoC 2021 Day 6!");
    println!("{}", part_2());
}

fn blah(vec: Vec<u64>, day: usize) -> u64 {
    if day >= 0 {
        return vec[day] + blah(vec, day - 6);
    }
    return 0;
}

fn part_2() -> u64 {
    let start = read_lines("input.txt")
        .unwrap()
        .next()
        .unwrap()
        .unwrap()
        .split(',')
        .map(|x| x.parse::<usize>().unwrap())
        .collect::<Vec<usize>>();

    let mut max_fish: Vec<u64> = Vec::new();

    for day in 0..81 {
        max_fish.push(match day {
            0..=7 => 0,
            8..=13 => 1 + max_fish[day - 8],
            _ => 1 + max_fish[day - 8] + max_fish[day - 14],
        })
    }

    return start
        .iter()
        .map(|x| 1 + max_fish.get(80 - *x).unwrap())
        .sum();
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
