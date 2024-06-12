use std::str;

const INPUT1: &str = "input1";

fn main() -> std::io::Result<()> {
    println!("Part 1");
    let res1 = part1();
    println!("{}", res1?);
    
    
    Ok(())
}

fn part1() -> std::io::Result<u32> {
    let mut reader = my_reader::BufReader::open(INPUT1)?;
    let mut buffer = String::new();
    
    let height_buffer: [u32; 7] = [0; 7];
    
    let bar_shape: [u32; 4] = [1, 1, 1, 1];
    let cross_shape: [u32; 3] = [1, 3, 1];
    let l_shape: [u32; 3] = [1, 1, 3];
    let column_shape: [u32; 1] = [4];
    let box_shape: [u32; 2] = [2, 2];

    let rock_shapes: [&[u32]; 5] = [&bar_shape, &cross_shape, &l_shape, &column_shape, &box_shape];
    let mut rock_cycle = rock_shapes.iter().cycle();
    
    let sub_len = 5;
    
    let wind = reader.read_line(&mut buffer).unwrap().unwrap();
    
    let wind_len = wind.len();
    
    println!("{}", wind_len);
    
    Ok(1)
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
