
function generateArr(){
	var arr = [];
	for(var i = 0; i<1000; i++){
		arr.push(Math.floor(Math.random()*1000))
	}
	return arr;
}

var arr = generateArr()

for(var x = arr.length-1; x>0; x--) {
	for (var y = 0; y<x; y++){
		if (arr[y]>arr[y+1]){
			var temp = arr[y]
			arr[y] = arr[y+1]
			arr[y+1] = temp
		}
	}
}
console.log(arr);

// bubble sort's average and worst case is n squared time
// best case time is 2n when the array is nearly sorted

