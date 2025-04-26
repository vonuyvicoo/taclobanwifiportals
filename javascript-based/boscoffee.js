function generateNum(){
	var numArray = [];
	for(i = 0; i < 6; i++){
    	let num = Math.floor(Math.random()*10);
    	numArray.push(num);
	}
	return numArray.join("");
}

setInterval(function(){
	$("[name='voucherCode']").val(generateNum());
	$("#button-login").click();
	console.log(1);
}, 5);