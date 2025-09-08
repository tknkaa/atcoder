use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let b_c: Vec<u32> = buffer
        .split_whitespace()
        .map(|c| c.parse().unwrap())
        .collect();
    let b = b_c[0];
    let c = b_c[1];
    if b * c % 2 == 0 {
        println!("Even");
    } else {
        println!("Odd");
    }
}
