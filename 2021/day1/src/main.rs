use std::cmp;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

static IN_FILE: &str = "input/input.txt";

struct IteratorCounter {
    count: u32,
    prev: i32,
}

struct IteratorCounter2 {
    count: u32,
    prev: Vec<i32>,
    index: usize,
}

fn main() {
    println!("Advent of Code 2021, Day 1!\n");
    println!("Part 1: {}\n", part_1(IN_FILE));
    println!("Part 2: {}\n", part_2(IN_FILE));
}

fn part_1(in_file: &str) -> u32 {
    if let Ok(lines) = read_lines(in_file) {
        let counter = lines.fold(IteratorCounter { count: 0, prev: 0 }, |mut acc, line| {
            let line = line.unwrap();
            let num = line.parse::<i32>().unwrap();
            if num > acc.prev {
                acc.count += 1;
            }
            acc.prev = num;
            acc
        });
        return cmp::max(counter.count - 1, 0);
    }
    return 0;
}

fn part_2(in_file: &str) -> u32 {
    if let Ok(lines) = read_lines(in_file) {
        let counter = lines.fold(
            IteratorCounter2 {
                count: 0,
                prev: Vec::new(),
                index: 0,
            },
            |mut acc, line| {
                let line = line.unwrap();
                let num = line.parse::<i32>().unwrap();
                if acc.prev.len() < 3 {
                    acc.prev.push(num);
                    return acc;
                }
                if acc.prev[acc.index] < num {
                    acc.count += 1;
                }
                acc.prev[acc.index] = num;
                acc.index = (acc.index + 1) % 3;
                return acc;
            },
        );
        return counter.count;
    }
    return 0;
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
