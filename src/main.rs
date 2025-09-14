use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let n_l: Vec<u32> = buffer
        .trim()
        .split_whitespace()
        .map(|num| num.parse().unwrap())
        .collect();
    let _n = *n_l.get(0).unwrap();
    let l = *n_l.get(1).unwrap();
    buffer.clear();
    io::stdin().read_line(&mut buffer).unwrap();
    let k: u32 = buffer.trim().parse().unwrap();
    buffer.clear();
    io::stdin().read_line(&mut buffer).unwrap();
    let a: Vec<u32> = buffer
        .trim()
        .split_whitespace()
        .map(|num| num.parse().unwrap())
        .collect();
    let score = search_score(&a, l, k);
    println!("{score}");
}

fn divide_k_plus_one_pieces_longer_than_m(a: &Vec<u32>, l: u32, k: u32, m: u32) -> bool {
    let mut tmp: u32 = 0;
    let mut count: u32 = 0;
    for a_i in a {
        if a_i - tmp >= m {
            tmp = *a_i;
            count += 1;
        }
        if count == k {
            return l - tmp >= m;
        }
    }
    false
}

fn search_score(a: &Vec<u32>, l: u32, k: u32) -> u32 {
    let mut left: i32 = -1;
    let mut right = (l + 1) as i32;
    while right - left > 1 {
        let mid = (left + right) / 2;
        if divide_k_plus_one_pieces_longer_than_m(a, l, k, mid as u32) {
            left = mid;
        } else {
            right = mid;
        }
    }
    left as u32
}
