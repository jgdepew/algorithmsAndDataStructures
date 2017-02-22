function selection(arr) {
	for(var i = 0; i<arr.length; i++){
		var min = i;
		for (var j=i+1; j<arr.length; j++){
			if (arr[j]<arr[min]){
				min = j;
			}
		}
		swap(arr, i, min)
	}
	return arr;
}

function swap(arr, a, b){
	var temp = arr[a];
	arr[a] = arr[b]
	arr[b] = temp;
}

function generateArr(){
	var arr = []
	for(var i = 0; i < 10; i++) {
		arr.push(Math.floor(Math.random()*100))
	}
	return arr;
}

var arr = generateArr();
console.log(arr)
selection(arr);
console.log(arr)