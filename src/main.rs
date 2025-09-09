use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let conds: Vec<u32> = buffer
        .trim()
        .split_whitespace()
        .map(|num| num.parse().unwrap())
        .collect();
    let n = conds[0];
    let a = conds[1];
    let b = conds[2];
    let mut total = 0;
    for num in 1..(n + 1) {
        if a <= sum_digits(num) && sum_digits(num) <= b {
            total += num;
        }
    }
    println!("{total}");
}

fn sum_digits(x: u32) -> u32 {
    let mut sum = 0;
    let mut y = x;
    while y != 0 {
        let digit = y - (y / 10) * 10;
        sum += digit;
        y = y / 10;
    }
    return sum;
}

#[cfg(test)]
mod test {
    use super::*;
    #[test]
    fn check_sum_digits() {
        assert_eq!(6, sum_digits(123));
        assert_eq!(8, sum_digits(2222));
    }
}
