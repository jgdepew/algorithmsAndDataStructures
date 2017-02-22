function merge_sort(arr) {
    // Base case. A list of zero or one elements is sorted, by definition.
    if (arr.length <= 1) {
        return arr
    }

    // Recursive case. First, divide the list into equal-sized sublists
    // consisting of the first half and second half of the list.
    var left = []
    var right = []

    for(var i = 0; i<arr.length; i++) {
        if (i < arr.length/2 ) {
            left.push(arr[i])
        } else{
            right.push(arr[i])
        }
    }
    // console.log(left);
    // console.log(right);
    // Recursively sort both sublists.
    // console.log(left, right)
    left = merge_sort(left)
    right = merge_sort(right)
    // Then merge the now-sorted sublists.
    return merge(left, right)
}

function merge(left, right) {
    var result = [];

    while (left.length != 0 && right.length != 0) {
        if (left[0] <= right[0]) {
            result.push(left[0])
            // push first(left) to result
            left.splice(0,1)
        } else {
            result.push(right[0])
            // push first(right) to result
            right.splice(0,1)
        }
    }

    // Either left or right may have elements left; consume them.
    // (Only one of the following loops will actually be entered.)
    while (left.length != 0) {
        result.push(left[0])
        // push first(left) to result
        left.splice(0,1)

    }
    while (right.length != 0) {        
        result.push(right[0])
        // push first(right) to result
        right.splice(0,1)
    }
    return result
}

var arr = [5,0,4,8,2,6,3,9,1,7,10,11]
console.log(arr)
arr = merge_sort(arr);







