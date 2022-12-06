static INPUT1: &str = "input1.txt";

fn main() -> std::io::Result<()> {
    println!("Part 1");
    let res = part1();
    println!("{}", res);

    Ok(())
}

fn part1() -> std::io::Result<u32> {
    let mut reader = my_reader::BufReader::open(INPUT1);
    let mut buffer = String::new();

    while let Some(line_) = reader.read_line(&mut buffer) {}

    Ok(1)
}

mod game {}

#[derive(Debug, Clone)]
pub enum Symbol {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

#[derive(Debug, Clone)]
pub enum Result {
    Win = 6,
    Draw = 3,
    Lose = 0,
}

mod my_reader {
    use std::{
        fs::File,
        io::{self, prelude::*},
    };

    pub struct BufReader {
        reader: io::BufReader<File>,
    }

    impl BufReader {
        pub fn open(path: impl AsRef<std::path::Path>) -> io::Result<Self> {
            let file = File::open(path)?;
            let reader = io::BufReader::new(file);

            Ok(Self { reader })
        }

        pub fn read_line<'buf>(
            &mut self,
            buffer: &'buf mut String,
        ) -> Option<io::Result<&'buf mut String>> {
            buffer.clear();

            self.reader
                .read_line(buffer)
                .map(|u| if u == 0 { None } else { Some(buffer) })
                .transpose()
        }
    }
}
