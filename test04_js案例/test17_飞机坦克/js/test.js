// 背景动起来
var jsBg1 = document.getElementById('bg1')
var jsBg2 = document.getElementById('bg2')

var timerBg = setInterval(function(){
	jsBg1.style.top= jsBg1.offsetTop+1+"px"
	jsBg2.style.top= jsBg2.offsetTop+1+"px"
	if(jsBg1.offsetTop>=1300){
		jsBg1.style.top="-1300px"
	}
	
	if(jsBg2.offsetTop>=1300){
		jsBg2.style.top="-1300px"
	}
	
},10)

// 飞机动起来
var airplane = document.getElementById("airplane")
var mainScreen = document.getElementById("mainScreen")

airplane.addEventListener("mousedown",function(e){
	var ev = e|| window.event
	basex = ev.pageX
	basey = ev.pageY
	movx = 0
	movy = 0
	// 屏幕的事件
	mainScreen.addEventListener("mousemove",function(e){
		var en = e||window.event
		movx = en.pageX-basex
		basex = en.pageX
		movy = en.pageY-basey
		basey = en.pageY
		airplane.style.top= airplane.offsetTop+movy+"px"
		airplane.style.left= airplane.offsetLeft+movx+"px"
		
	},false)
},false)

// 创建子弹
var timerBullent = setInterval(function(){
	var bullent = document.createElement("div")
	mainScreen.appendChild(bullent)
	bullent.className = "bullent"
	bullent.style.left = airplane.offsetLeft+95+"px"
	bullent.style.top = airplane.offsetTop+10+"px"
	
	var timerBullentFly = setInterval(function(){
		bullent.style.top= bullent.offsetTop-10+"px"
		if(bullent.offsetTop<-20){
			clearInterval(timerBullentFly)
			mainScreen.removeChild(bullent)
		}
	},50)
	bullent.timer = timerBullentFly
},200)




// 创建坦克
var timerTank = setInterval(function(){
	var tank = document.createElement("div")
	mainScreen.appendChild(tank)
	tank.className = "tank"
	tank.style.left = randomNum(0,780)+"px"
	tank.style.top = 0+"px"
	
	var timerTankFly = setInterval(function(){
		tank.style.top= tank.offsetTop+5+"px"
		if(tank.offsetTop>1320){
			clearInterval(timerTankFly)
			mainScreen.removeChild(tank)
		}
	},50)
	tank.timer = timerTankFly
	
},1000)


var allBullents = document.getElementsByClassName("bullent")
console.log(allBullents)
var allTanks = document.getElementsByClassName("tank")
console.log(allTanks)

var timerPZJC = setInterval(function(){
	var allTanks = document.getElementsByClassName("tank")
	var allBullents = document.getElementsByClassName("bullent")
	// console.log(allTanks)
	for(var i =0;i<allBullents.length;i++){
		for(var j=0;j<allTanks.length;i++){
			var b = allBullents[i];
			var t = allTanks[j];
			if(pzjcFunc(b,t)){
				clearInterval(b.timer)
				clearInterval(t.timer)
				mainScreen.removeChild(t)
				mainScreen.removeChild(b)
				break
			}
		}
	}
	
},1000)

// 随机数
function randomNum(min,max){
	return parseInt(Math.random()*(max-min)+min);
}

// 碰撞检测
function pzjcFunc(obj1, obj2){
    var obj1Left = obj1.offsetLeft;
    var obj1Width = obj1Left + obj1.offsetWidth;
    var obj1Top = obj1.offsetTop;
    var obj1Height = obj1Top + obj1.offsetHeight;

    var obj2Left = obj2.offsetLeft;
    var obj2Width = obj2Left + obj2.offsetWidth;
    var obj2Top = obj2.offsetTop;
    var obj2Height = obj2Top + obj2.offsetHeight;

    if ( !(obj1Left > obj2Width || obj1Width < obj2Left || obj1Top > obj2Height || obj1Height < obj2Top) ) {
        return true;
    } 
    return false;
}