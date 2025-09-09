use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let a: u32 = buffer.trim().parse().unwrap();
    buffer.clear();
    io::stdin().read_line(&mut buffer).unwrap();
    let b: u32 = buffer.trim().parse().unwrap();
    buffer.clear();
    io::stdin().read_line(&mut buffer).unwrap();
    let c: u32 = buffer.trim().parse().unwrap();
    buffer.clear();
    io::stdin().read_line(&mut buffer).unwrap();
    let x: u32 = buffer.trim().parse().unwrap();
    buffer.clear();
    let mut count = 0;
    for a_count in 0..(a + 1) {
        for b_count in 0..(b + 1) {
            for c_count in 0..(c + 1) {
                let total = a_count * 500 + b_count * 100 + c_count * 50;
                if total == x {
                    count += 1;
                }
            }
        }
    }
    println!("{}", count);
}
