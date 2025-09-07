use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let a: u32 = buffer.trim().parse().unwrap();
    buffer.clear();
    io::stdin().read_line(&mut buffer).unwrap();
    let b_c: Vec<u32> = buffer
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();
    buffer.clear();
    io::stdin().read_line(&mut buffer).unwrap();
    let s = buffer.trim();
    println!("{}", a + b_c[0] + b_c[1]);
    println!("{}", s);
}
