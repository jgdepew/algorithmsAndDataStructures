// quick sort

function generateArr(){
	var arr = [];
	for(var i = 0; i<10; i++){
		arr.push(Math.floor(Math.random()*100))
	}
	return arr;
}

// var arr = generateArr()


function swap(arr, a, b) {
	var temp = arr[a];
	arr[a] = arr[b];
	arr[b] = temp;
}

var arr = [12,14,27,8,13,22,5,7,30]

function partition(arr, lo, hi) {
	var i = lo+1;
	var j = hi;
	// swap hi and lo
	while (true){
		// find item on right to swap (less than pivot)
		while (arr[j]>arr[lo]){
			j--;
			if(j == lo) {
				break;
			}
		}
		// find item on left to swap (greater than pivot)
		while (arr[i]<arr[lo]){
			i++;
			if(i == hi){
				break;
			}
		}
		if (i >= j){
			break;
		}
		swap(arr, i, j);
	}
	swap(arr, lo, j)
	return j;
}

function quick(arr, lo, hi) {
	if(arr.length>1) {
		var j = partition(arr, lo, hi);
		console.log(arr)
		if (lo < j - 1){
			swap(arr, lo, j-1)
		}

		if (hi > j) {
			swap(arr, j, hi);
		}
	}
	return arr;
}



console.log(arr)
arr = quick(arr, 0, arr.length-1)
console.log(arr)










// end