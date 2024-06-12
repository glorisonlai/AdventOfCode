use std::str;

fn main() -> std::io::Result<()> {
    println!("Part 1");
    let res1 = part1();
    println!("{}", res1?);

    Ok(())
}

// fn part1() -> std::io::Result<u32> {
//     let vec: Vec<u32> = vec![];
//     let thing = vec.iter().last();
//     println!("{:?}", thing);

//     println!("{:?}", thing.or(Some(&2)));
//     Ok(1)
// }

fn parse_digits(line_utf8: &str) -> Option<u32> {
    let digit_range = ['0', '9'];

    let mut digits = line_utf8.chars().filter(|x| x >= &digit_range[0] && x <= &digit_range[1]);

    let first_digit = digits.next();
    let last_digit = digits.last().or(first_digit);

    Some(first_digit?.to_digit(10)? * 10 + last_digit?.to_digit(10)?)
}

fn part1() -> std::io::Result<u32> {
    let mut reader = my_reader::BufReader::open("input/input.txt")?;
    let mut buf = String::new();

    let mut accum: u32 = 0;

    while let Some(line_utf8_) = reader.read_line(&mut buf) {
        let line_utf8 = line_utf8_?.as_str();

        let line_calib = parse_digits(&line_utf8);

        accum = accum + line_calib.unwrap_or(0);
    }

    Ok(accum)
}

fn part2() -> std::io::Result<u32> {
    // Create suffix tree

    // Parse line thru suffix tree
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
