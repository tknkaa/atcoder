use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let n: u32 = buffer.trim().parse().unwrap();
    buffer.clear();
    let mut diameters: Vec<u32> = Vec::new();
    for _i in 0..n {
        io::stdin().read_line(&mut buffer).unwrap();
        let d: u32 = buffer.trim().parse().unwrap();
        diameters.push(d);
        buffer.clear();
    }
    diameters.sort();
    diameters.dedup();
    println!("{}", diameters.len());
}
