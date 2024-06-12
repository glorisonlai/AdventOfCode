use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    println!("AoC 2021 Day 7!");
    part_1("input.txt");
}

fn part_1(input: &str) {
    if let Ok(buffer) = read_lines(input) {
        let turts = buffer
            .lines()
            .next()
            .unwrap()
            .unwrap()
            .split(',')
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();

        println!("{:?}", turts);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::BufReader<File>>
where
    P: AsRef<Path>,
{
    let f = File::open(filename)?;
    return Ok(io::BufReader::new(f));
}
