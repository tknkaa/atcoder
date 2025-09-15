use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let n: u32 = buffer.trim().parse().unwrap();
    buffer.clear();
    let mut roads: Vec<Vec<u32>> = Vec::new();
    for _i in 0..n {
        io::stdin().read_line(&mut buffer).unwrap();
        let road: Vec<u32> = buffer
            .trim()
            .split_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();
        roads.push(road);
    }
    let u = min_dists(1, &roads, n)
        .into_iter()
        .max_by_key(|&val| val)
        .unwrap()
        .to_owned();
    let tree_diameter = min_dists(u as u32, &roads, n).into_iter().max().unwrap();
    println!("{}", tree_diameter + 1);
}

fn min_dists(v: u32, roads: &Vec<Vec<u32>>, n: u32) -> Vec<u32> {
    let mut min_dists = vec![u32::MAX; n as usize];
    min_dists[v as usize] = 0;
    for v in 0..n {
        for road in roads {
            let start = road[0];
            let end = road[1];
            if min_dists[start as usize] + 1 < min_dists[end as usize] {
                min_dists[end as usize] = min_dists[start as usize] + 1;
            }
        }
        if v == n - 1 {
            break;
        }
    }
    min_dists
}
