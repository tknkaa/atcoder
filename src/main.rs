use std::io;

#[derive(Debug)]
struct Point {
    t: u32,
    x: u32,
    y: u32,
}

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).unwrap();
    let n: u32 = buffer.trim().parse().unwrap();
    buffer.clear();
    let mut plan: Vec<Point> = Vec::new();
    for _i in 0..n {
        io::stdin().read_line(&mut buffer).unwrap();
        let new_point: Vec<u32> = buffer
            .trim()
            .split_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();
        plan.push(Point {
            t: new_point[0],
            x: new_point[1],
            y: new_point[2],
        });
        buffer.clear();
    }
    plan.insert(0, Point { t: 0, x: 0, y: 0 });
    // if difference between t_k and t_{k+1} is odd, the distance should be odd?
    // also, the distance should be less than or equal to the time distance?
    for i in 0..n {
        let i = i as usize;
        let distance = measure_distance(&plan[i], &plan[i + 1]);
        let interval = plan[i + 1].t - plan[i].t;
        if distance > interval {
            println!("No");
            return;
        }
        if (plan[i + 1].t - plan[i].t) % 2 == 0 {
            if distance % 2 == 0 {
                continue;
            } else {
                println!("No");
                return;
            }
        } else {
            if distance % 2 == 1 {
                continue;
            } else {
                println!("No");
                return;
            }
        }
    }
    println!("Yes");
}

fn measure_distance(point1: &Point, point2: &Point) -> u32 {
    return point1.x.abs_diff(point2.x) + point1.y.abs_diff(point2.y);
}
