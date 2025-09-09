use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let combi: Vec<u32> = buffer
        .trim()
        .split_whitespace()
        .map(|num| num.parse().unwrap())
        .collect();
    let n = combi[0];
    let y = combi[1];
    for i in 0..(n + 1) {
        for j in 0..(n + 1 - i) {
            let k = n - i - j;
            let total = 10000 * i + 5000 * j + 1000 * k;
            if total == y {
                println!("{} {} {}", i, j, k);
                return;
            }
        }
    }
    println!("-1 -1 -1");
}
