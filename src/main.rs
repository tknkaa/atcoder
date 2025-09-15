use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let length: u32 = buffer.trim().parse().unwrap();
    let patterns = (2 as u32).pow(length);
    for i in 0..patterns {
        let exp = binary_expression(i, length);
        if validate_binary(&exp) {
            print_par(&exp);
        }
    }
}

fn binary_expression(mut n: u32, length: u32) -> Vec<u32> {
    let mut exp = vec![0; length as usize];
    for i in 0..length {
        let remainder = n % 2;
        exp[(length - 1 - i) as usize] = remainder;
        n = n / 2;
    }
    exp
}

fn validate_binary(bin: &Vec<u32>) -> bool {
    let count_0 = bin.iter().filter(|&n| *n == 0).count();
    let count_1 = bin.iter().filter(|&n| *n == 1).count();
    if count_0 != count_1 {
        return false;
    }
    let mut tmp_count_0 = 0;
    let mut tmp_count_1 = 0;
    for item in bin {
        if *item == 0 {
            tmp_count_0 += 1;
        } else {
            tmp_count_1 += 1;
        }
        if tmp_count_0 < tmp_count_1 {
            return false;
        }
    }
    return true;
}

fn print_par(bin: &Vec<u32>) {
    for item in bin {
        if *item == 0 { print!("(") } else { print!(")") }
    }
    print!("\n");
}
