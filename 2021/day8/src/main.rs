use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    println!("AoC 2021 Day 8!");
    part_1("input.txt");
}

fn part_1(input: &str) {
    if let Ok(buffer) = read_lines(input) {
        let lines = buffer
            .lines
            .map(|line| parse_line(line))
            .map(|(input, output)| output);
        println!("{:?}", lines);
    }
}

fn parse_line(line: &str) -> Vec<Vec<String>> {
    return line
        .split('|')
        .map(|list| list.split().map(|string| string.clone()).collect::Vec<String>()).collect::Vec<Vec<String>>();
}

fn read_lines<P>(filename: P) -> io::Result<io::BufReader<File>>
where
    P: AsRef<Path>,
{
    let f = File::open(&filename)?;
    return Ok(io::BufReader::new(f));
}
