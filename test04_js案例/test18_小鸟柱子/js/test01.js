var canvas = document.getElementById("canvas")
var context = canvas.getContext("2d")
var img = new Image()
img.src="img/bird0_1.png"
var birdX = 10;
var birdY =10;
var birdTimer = null;

img.onload=function(){
	if(birdTimer==null){
		
		context.drawImage(img,birdX,birdY)
		birdTimer = setInterval(function(){
			if(birdY>=110){
				birdY--
			}
			birdY++
			context.clearRect(0,0,800,400)
			context.drawImage(img,birdX,birdY)
		drawColumn()
		},10)
	}
}

document.onmousedown= function(){
	img.src="img/bird0_0.png"
	birdY = birdY-30
}

document.onmouseup= function(){
	img.src="img/bird0_1.png"
}


var columnArr = [];
var columnTimer = null;

function createColumn(){
	setInterval(function(){
		var column ={};
		column.positionX= 400;
		column.positionY = -Math.round(Math.random()*70+200)
		column.imgA = new Image()
		column.imgB  = new Image()
		column.imgA.src = "img/pipe_down.png"
		column.imgB.src = "img/pipe_up.png"
		column.id = new Date().getTime();
		columnArr.push(column)	
		// console.log(columnArr)
	},1000)
}

createColumn()

var same = null;
var mark = 0;

function drawColumn(){
	for(var i =0;i<columnArr.length;i++){
		columnArr[i].positionX--
		context.drawImage(columnArr[i].imgA,columnArr[i].positionX,columnArr[i].positionY)
		context.drawImage(columnArr[i].imgB,columnArr[i].positionX,columnArr[i].positionY+350)
	
		if (columnArr[i].positionX<-1000){
			columnArr.splice(i)
		}
		
		if(birdX+40>=columnArr[i].positionX&&birdX-50<=columnArr[i].positionX){
			if (columnArr[i].id!=same){
				mark++;
				same=columnArr[i].id
			}
			document.getElementById("mark").innerHTML="得分:"+mark
			console.log(mark)
		}
		 
		 
	}
}