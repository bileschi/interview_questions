use std::collections::HashMap;
use std::collections::HashSet;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // Read file as list of words.
    let in_file = "/usr/share/dict/words";
    let mut n = 0;
    let mut words = Vec::new();
    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines(in_file) {
        // Consumes the iterator, returns an (Optional) String
        for line in lines {
            if let Ok(ip) = line {
                n = n + 1;
                words.push(ip);
                // println!("{}", ip);
            }
        }
    }
    // organize the words into a map
    // len_of_word -> word_idx -> set_of_letters_in_word
    // Get list of all lengths.  Assume that since we only have ASCII chars
    // that bytes is the same as word len.
    let mut lens = HashSet::new();
    let mut len_to_word_to_set = HashMap::new();
    for (i_word, word) in words.iter().enumerate() {
        let len = word.len();
        lens.insert(len);
        // If we don't have the key already, create a new empty hash
        if !len_to_word_to_set.contains_key(&len) {
            let word_to_charset: HashMap<usize, HashSet<char>> = HashMap::new();
            len_to_word_to_set.insert(len, word_to_charset);
        }
        let word_to_charset = len_to_word_to_set.get_mut(&len).unwrap();
        let mut chars_in_word = HashSet::new();
        for c in word.chars() {
            chars_in_word.insert(c);
        }
        word_to_charset.insert(i_word, chars_in_word);
    }

    // Create schedule of wordlen pairs (in desc order of product.
    let mut schedule = HashSet::new();
    for len1 in &lens {
        for len2 in &lens {
            if len2 > len1 {
                continue;
            }
            let prod = len1 * len2;
            schedule.insert((prod, len1, len2));
        }
    }
    // Transfer hash set to a Vector and sort it by prod (desc).
    let mut schedule_list = Vec::new();
    for o in schedule {
        schedule_list.push(o);
    }
    schedule_list.sort();
    schedule_list.reverse();

    for (prod, len1, len2) in schedule_list {
        let wix_to_chars1 = &len_to_word_to_set[len1];
        let wix_to_chars2 = &len_to_word_to_set[len2];
        for (i_w1, chars1) in wix_to_chars1 {
            for (i_w2, chars2) in wix_to_chars2 {
                if chars1.is_disjoint(&chars2) {
                    println!("prod {:?}", prod);
                    println!("len1 {:?}", len1);
                    println!("len2 {:?}", len2);
                    println!("word1 {:?}", words[*i_w1]);
                    println!("word2 {:?}", words[*i_w2]);
                    std::process::exit(0);
                }
            }
        }
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
