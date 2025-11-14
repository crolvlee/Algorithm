function solution(sizes) {
    
    let big_size_arr = [];
    let small_size_arr = [];
    
    for (let i = 0; i < sizes.length; i++) {
        let min_size = Math.min(sizes[i][0], sizes[i][1]);
        let max_size = Math.max(sizes[i][0], sizes[i][1]);
        
        small_size_arr.push(min_size);
        big_size_arr.push(max_size);
    }
    
    let answer = Math.max(...big_size_arr) * Math.max(...small_size_arr);
    return answer;
}