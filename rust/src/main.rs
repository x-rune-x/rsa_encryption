fn main() {
    let prime1: u32 = 2;
    let prime2: u32 = 7;
    let n = prime1 * prime2;
    let r = (prime1 - 1) * (prime2 - 1);

    println!("n = {}", n);
    println!("r = {}", r);

    let e = find_e(r, n);
    let d = find_d(r, e);

    println!("e = {}", e);
    println!("d = {}", d);

    let m: u32 = 6;
    println!("m = {}", m);
    let c = u32::pow(m, e) % n;
    println!("c = {}", c);

    let message = u32::pow(c, d) % n;

    println!("message = {}", message)
}

fn gcd(a: u32, b: u32) -> u32 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn coprime(a: u32, b: u32) -> bool {
    gcd(a, b) == 1
}

fn find_e(r: u32, n: u32) -> u32 {
    for i in 2..r + 1 {
        if coprime(i, r) && coprime(i, n) {
            return i;
        }
    }

    panic!("There was a problem and no suitable number was found for e.")
}

fn find_d(r: u32, e: u32) -> u32 {
    for k in 1..r {
        if k * e % r == 1 {
            return k + r;
        }
    }

    panic!("There was a problem and no suitable number could be found for d.")
}
