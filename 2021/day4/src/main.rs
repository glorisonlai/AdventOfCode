use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    println!("AoC 2021 Day 4");
    part_2();
}

fn part_2() -> i32 {
    struct Tile {
        val: i32,
        visited: bool,
    }

    struct BoardState {
        win: bool,
        board: Vec<Vec<Tile>>,
    }

    if let Ok(mut buffer) = read_lines("input.txt") {
        let mut locations: HashMap<i32, Vec<(usize, usize, usize)>> = HashMap::new();
        let mut line_buf = String::new();
        let _ = buffer.read_line(&mut line_buf);
        let draws = line_buf
            .trim()
            .split(",")
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();

        let mut boards = buffer.lines().fold(Vec::new(), |mut acc, line| {
            let line = line.unwrap();
            if line.len() == 0 {
                acc.push(BoardState {
                    win: false,
                    board: Vec::new(),
                });
            } else {
                let tiles = line
                    .split_whitespace()
                    .map(|x| x.parse::<i32>().unwrap())
                    .collect::<Vec<i32>>();

                let mut board_line = Vec::new();
                for tile in tiles {
                    if !locations.get(&tile).is_some() {
                        locations.insert(tile, Vec::new());
                    }
                    locations.get_mut(&tile).unwrap().push((
                        acc.len() - 1,
                        acc.last().unwrap().board.len(),
                        board_line.len(),
                    ));
                    board_line.push(Tile {
                        val: tile,
                        visited: false,
                    });
                }
                let curr_board = acc.last_mut().unwrap();
                curr_board.board.push(board_line);
            }
            acc
        });

        let mut last_win: usize = 0;
        for draw in &draws {
            match locations.get(draw) {
                None => continue,
                Some(coords) => {
                    for (table, row, col) in coords {
                        let board = boards.get_mut(*table).unwrap();
                        if board.win {
                            continue;
                        }
                        board
                            .board
                            .get_mut(*row)
                            .unwrap()
                            .get_mut(*col)
                            .unwrap()
                            .visited = true;

                        // Check win condition
                        if board
                            .board
                            .get(*row)
                            .unwrap()
                            .iter()
                            .all(|row_tile| row_tile.visited)
                            || board
                                .board
                                .iter()
                                .all(|col_tile| col_tile.get(*col).unwrap().visited)
                        {
                            board.win = true;
                            last_win = *table;
                        }
                    }
                }
            }
            let all_wins = boards.iter().all(|board| board.win);
            if all_wins {
                let unpicked =
                    boards
                        .get(last_win)
                        .unwrap()
                        .board
                        .iter()
                        .fold(0, |mut acc, row| {
                            acc += row.iter().fold(0, |mut acc, tile| {
                                if !tile.visited {
                                    acc += tile.val;
                                }
                                acc
                            });
                            acc
                        });
                println!("{}", unpicked * draw);
                return unpicked * draw;
            }
        }
    }
    return 0;
}

fn read_lines<P>(filename: P) -> io::Result<io::BufReader<File>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file))
}
