use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let s: u32 = buffer.trim().parse().unwrap();
    let s3 = s % 10;
    let s2 = (s % 100 - s3) / 10;
    let s1 = (s - 10 * s2 - s3) / 100;
    let sum = s1 + s2 + s3;
    println!("{}", sum);
}
