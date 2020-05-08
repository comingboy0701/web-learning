var jsBox = document.getElementById("box")
var jsPic = document.getElementById("pic")
var jsLeft = document.getElementById("left")
var jsRight = document.getElementById("right")
var jsListArr = document.getElementsByTagName("li")

//  第一个li 是红色
jsListArr[0].style.backgroundColor="red"

// 启动一个定时器定时轮播图片
var currentPage = 1
var timer = setInterval(startLoop,1000)

function startLoop(){
	currentPage++
	changePage()
}



function changePage(){
	if (currentPage==9){
		currentPage=1
	}
	if(currentPage==0){
		currentPage=8
	}
	jsPic.src="img/"+currentPage+".jpg"
	for(var i =0;i<jsListArr.length;i++){
		jsListArr[i].style.backgroundColor="#aaa"
	}
	jsListArr[currentPage-1].style.backgroundColor="red"
	
}

// 鼠标进入box
jsBox.addEventListener("mouseover",overFunc,false)
function overFunc(){
	clearInterval(timer)
	jsLeft.style.display="block"
	jsRight.style.display="block"
}

// 鼠标离开box
jsBox.addEventListener("mouseout",outFunc,false)
function outFunc(){
	timer = setInterval(startLoop,1000)
	jsLeft.style.display="none"
	jsRight.style.display="none"
}

jsLeft.addEventListener("mouseover",deep,false)
jsRight.addEventListener("mouseover",deep,false)
function deep(){
	this.style.backgroundColor="rgba(255,255,255,0.5)"
}

jsLeft.addEventListener("click",function(){
	currentPage--
	changePage()
},false)
jsRight.addEventListener("click",function(){
	currentPage++
	changePage()
},false)

for(var i =0;i<jsListArr.length;i++){
	jsListArr[i].index = i+1
	jsListArr[i].addEventListener("mouseover",function(){
		// currentPage = parseInt(this.innerHTML)
		currentPage = parseInt(this.index)
		changePage();
	},false)
}
