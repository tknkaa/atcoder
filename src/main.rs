use std::{collections::HashSet, io};

#[derive(Debug)]
struct Road {
    start: u32,
    end: u32,
}

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    // number of cities: 1, 2, ... n
    let n: u32 = buffer.trim().parse().unwrap();
    buffer.clear();
    let mut roads: Vec<Road> = Vec::new();
    for _i in 0..(n - 1) {
        io::stdin().read_line(&mut buffer).unwrap();
        let info: Vec<u32> = buffer
            .trim()
            .split_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();
        let start = info.get(0).unwrap().to_owned();
        let end = info.get(1).unwrap().to_owned();
        roads.push(Road { start, end });
        buffer.clear();
    }

    let min_dists_from_one = min_dists(1, &roads, n);
    let (farthest_vertex, _farthest_dist) = min_dists_from_one
        .iter()
        .enumerate()
        .max_by_key(|&(i, &val)| if i == 0 { 0 } else { val })
        .unwrap();
    let (_, tree_diameter) = min_dists(farthest_vertex as u32, &roads, n)
        .into_iter()
        .enumerate()
        .max_by_key(|&(i, val)| if i == 0 { 0 } else { val })
        .unwrap();
    println!("{}", tree_diameter + 1);
}

fn min_dists(v: u32, roads: &Vec<Road>, n: u32) -> Vec<u32> {
    // indexes of min_dists are mapped to cities.
    let mut min_dists = vec![u32::MAX; (n + 1) as usize];
    // v is the start point.
    min_dists[v as usize] = 0;
    // Each element is an array of cities which are connected to the index city.
    let neighbor_list = convert_roads_to_neighbor_list(roads, n);
    // add all the cities to q
    let mut q = HashSet::new();
    for i in 1..=n {
        q.insert(i);
    }

    let mut count = 0;
    while q.len() >= 1 {
        count += 1;
        if count == 5 {
            break;
        }
        // Index 0 is not mapped to any city.
        let mut nearest_city = 0;
        for city in &q {
            if min_dists[*city as usize] < min_dists[nearest_city as usize] {
                nearest_city = *city;
            }
        }
        q.remove(&nearest_city);
        for neighbor in &neighbor_list[nearest_city as usize] {
            let alt = min_dists[nearest_city as usize] + 1;
            if min_dists[*neighbor as usize] > alt {
                min_dists[*neighbor as usize] = alt;
            }
        }
    }
    min_dists
}

fn convert_roads_to_neighbor_list(roads: &Vec<Road>, n: u32) -> Vec<Vec<u32>> {
    let mut neighbor_list: Vec<Vec<u32>> = vec![Vec::new(); (n + 1) as usize];
    for road in roads {
        neighbor_list[road.start as usize].push(road.end);
        neighbor_list[road.end as usize].push(road.start);
    }
    neighbor_list
}
