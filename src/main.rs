use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    buffer.clear();
    io::stdin().read_line(&mut buffer).unwrap();
    let mut cards: Vec<u32> = buffer
        .trim()
        .split_whitespace()
        .map(|card| card.parse().unwrap())
        .collect();
    cards.sort();
    let mut alice_score = 0;
    let mut bob_score = 0;
    let mut turn = 0;
    while cards.len() > 0 {
        if turn % 2 == 0 {
            alice_score += cards.pop().unwrap();
        } else {
            bob_score += cards.pop().unwrap();
        }
        turn += 1;
    }
    let ans = alice_score - bob_score;
    println!("{ans}");
}
