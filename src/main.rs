use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    buffer.clear();
    io::stdin().read_line(&mut buffer).unwrap();
    let mut a: Vec<u32> = buffer
        .trim()
        .split_whitespace()
        .map(|num| num.parse().unwrap())
        .collect();
    let mut count = 0;
    while judge_and_divide(&a) != Err(()) {
        a = judge_and_divide(&a).unwrap();
        count += 1;
    }
    println!("{}", count);
}

fn judge_and_divide(nums: &Vec<u32>) -> Result<Vec<u32>, ()> {
    let mut divided: Vec<u32> = Vec::new();
    for num in nums {
        if num % 2 == 0 {
            let divided_ref = &mut divided;
            divided_ref.push(num / 2);
        } else {
            return Err(());
        }
    }
    return Ok(divided);
}
