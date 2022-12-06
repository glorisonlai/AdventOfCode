use std::cmp;

static INPUT1: &str = "input1.txt";

fn main() -> std::io::Result<()> {
    println!("Part 1");
    let res1 = part1();
    println!("{}", res1?);

    println!("Part 2");
    let res2 = part2();
    println!("{}", res2?);

    Ok(())
}

fn part1() -> std::io::Result<u32> {
    let mut reader = my_reader::BufReader::open(INPUT1)?;
    let mut buffer = String::new();

    let mut max_cal = 0;
    let mut curr_cal = 0;

    while let Some(line_) = reader.read_line(&mut buffer) {
        let line = line_?.as_str();

        match line {
            "\n" => {
                max_cal = cmp::max(max_cal, curr_cal);
                curr_cal = 0;
            }
            _ => curr_cal += line.trim().parse::<u32>().unwrap(),
        }
    }

    Ok(max_cal)
}

fn part2() -> std::io::Result<u32> {
    let mut reader = my_reader::BufReader::open(INPUT1)?;
    let mut buffer = String::new();

    let mut top3cals: [u32; 3] = [0, 0, 0];
    let mut curr_cal: u32 = 0;

    while let Some(line_) = reader.read_line(&mut buffer) {
        let line = line_?.as_str();

        match line {
            "\n" => {
                let min_cal = top3cals.iter().min().unwrap();

                if min_cal < &curr_cal {
                    let min_cal_pos = top3cals.iter().position(|x| x == min_cal);
                    top3cals[min_cal_pos.unwrap()] = curr_cal;
                }
                curr_cal = 0;
            }
            _ => curr_cal += line.trim().parse::<u32>().unwrap(),
        }
    }

    Ok(top3cals.iter().sum())
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
