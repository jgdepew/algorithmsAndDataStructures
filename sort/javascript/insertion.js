function insertion(arr){
	for(var i = 1; i<arr.length; i++) {
		var index = i-1;
		var temp = i;
		while(arr[temp]<arr[index]){
			swap(arr, temp, index)
			temp--
			index--
		}
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
insertion(arr);
console.log(arr)