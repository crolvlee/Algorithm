function solution(A,B){

    A.sort((x, y) => x-y)
    B.sort((x, y) => y-x)
    
    let num = 0
    
    for (let i = 0; i < A.length; i++) {
        num += (A[i] * B[i])
    }
    
    return num;
}