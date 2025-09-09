use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let s = buffer.trim();
    let mut s: String = s.chars().rev().collect();
    let candidates = ["maerd", "remaerd", "esare", "resare"];
    loop {
        let mut count = 0;
        for candidate in candidates {
            if s.starts_with(candidate) {
                s = s[candidate.len()..].to_string();
                break;
            } else {
                count += 1;
            }
            if count == 4 {
                println!("NO");
                return;
            }
        }
        if s.len() == 0 {
            break;
        }
    }
    println!("YES")
}
