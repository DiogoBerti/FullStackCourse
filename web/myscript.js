var myheader = document.querySelector("h1");

var myPara = document.querySelector("#one");

function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function changeColor(){

  colorA = getRandomIntInclusive(0,255);
  console.log(colorA);
  colorB = getRandomIntInclusive(0,255);
  console.log(colorB);
  colorC = getRandomIntInclusive(0,255);
  console.log(colorC);
  myheader.style.color = "rgb("+colorA+","+colorB+","+colorC+")";

}

setInterval(changeColor, 700);

myPara.addEventListener('click',function(){
  alert("Clicado no paragrafo");
});

para_three = document.querySelector("#three");

var farol = false
para_three.addEventListener('dblclick',function(){
  if (farol === false){
      para_three.style.color = 'blue';
      farol = true;
  }else{
      para_three.style.color = 'red';
      farol = false;
  }


})

$('h1').click(function(){
  console.log('cliquei');
});

$('li').click(function(){
  $(this).text('New item');
})

$('#mover').keypress(function (event){
  if(event.which === 13){
    console.log(event);
    $(this).color = 'blue';
  }
})

$('#mover').on('dblclick', function(){
  function complete(){
    $('.container').eq(1).fadeIn(2000);
  }

  $(this).text('Clicked');
  $('.container').eq(0).fadeOut(2000, complete);

})
