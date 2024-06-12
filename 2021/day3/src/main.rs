use std::cmp;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

static INPUT_FILE: &'static str = "input.txt";

fn main() {
    println!("Hello, world!");
    let file = read_lines(INPUT_FILE);
    println!("{:?}", file);
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
