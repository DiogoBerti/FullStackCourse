table_array = document.querySelectorAll("td");
new_arr = []
for (item of table_array){
  console.log(item.id);
  new_arr.push(document.querySelector("#"+item.id));
}


//Restart button cleans the board
restart = document.querySelector('#restart');

function restartGame(){
  for (var i = 0; i < table_array.length; i++) {
    table_array[i].textContent = '';
    player.textContent = "Comecou de novo";
    player.style.color = 'green';
  }
}

restart.addEventListener('click', restartGame);

//controller for the turns
var turn = 1;

// find Player
player = document.querySelector("#player");


var score1 = [['','',''],['','',''],['','','']];
var score2 = [['','',''],['','',''],['','','']];



// Playing the game!
function playGame(){
    if(this.textContent != ""){
      alert("Voce nao pode escolher essa celula")
    }else{
      if (turn === 1){
        console.log(this.cellIndex + "-" + this.parentElement.rowIndex);
        score1[this.parentElement.rowIndex][this.cellIndex] = 1;
        this.textContent = "X";
        player.textContent = "É a vez do Player 2!"
        player.style.color = 'red';


      }else{
        console.log(this.cellIndex + "-" + this.parentElement.rowIndex);
        score2[this.parentElement.rowIndex][this.cellIndex] = 1;
        this.textContent = "O";
        player.textContent = "É a vez do Player 1!"
        player.style.color = 'blue';
      }

      turn *= -1;

    }
  }

for (var i = 0; i < table_array.length; i++) {
  console.log(table_array[i]);
  table_array[i].addEventListener('click', playGame);
}

function checkWin(){
  combinations1 = [[0][0],[0][1],[0][2]];

}

//Every td has its own id...
// one_one = document.querySelector('#oneone');
// one_one.addEventListener('click',function(){
//
//   if(one_one.textContent != ""){
//     alert("Voce nao pode escolher essa celula")
//   }else{
//     if (turn === 1){
//       one_one.textContent = "X";
//
//     }else{
//       one_one.textContent = "O";
//     }
//
//     score[0][0] = turn;
//     turn *= -1;
//
//   }});
//
// one_two = document.querySelector('#onetwo');
// one_two.addEventListener('click',function(){
//   if (turn === 1){
//     one_two.textContent = "X";
//
//   }else{
//     one_two.textContent = "O";
//   }
//   turn *= -1;
//
// });
//
//   one_three = document.querySelector('#onethree');
//   one_three.addEventListener('click',function(){
//     if (turn === 1){
//       one_three.textContent = "X";
//
//     }else{
//       one_three.textContent = "O";
//     }
//     turn *= -1;
//
//   });
//
//   two_one = document.querySelector('#twoone');
//   two_one.addEventListener('click',function(){
//     if (turn === 1){
//       two_one.textContent = "X";
//
//     }else{
//       two_one.textContent = "O";
//     }
//     turn *= -1;
//
//   });
//
//   two_two = document.querySelector('#twotwo');
//   two_two.addEventListener('click',function(){
//     if (turn === 1){
//       two_two.textContent = "X";
//
//     }else{
//       two_two.textContent = "O";
//     }
//     turn *= -1;
//
//   });
//
//   two_three = document.querySelector('#twothree');
//   two_three.addEventListener('click',function(){
//     if (turn === 1){
//       two_three.textContent = "X";
//
//     }else{
//       two_three.textContent = "O";
//     }
//     turn *= -1;
//
//   });
//
//   three_one = document.querySelector('#threeone');
//   three_one.addEventListener('click',function(){
//     if (turn === 1){
//       three_one.textContent = "X";
//
//     }else{
//       three_one.textContent = "O";
//     }
//     turn *= -1;
//
//   });
//
//   three_two = document.querySelector('#threetwo');
//   three_two.addEventListener('click',function(){
//     if (turn === 1){
//       three_two.textContent = "X";
//
//     }else{
//       three_two.textContent = "O";
//     }
//     turn *= -1;
//
//   });
//
//   three_three = document.querySelector('#threethree');
//   three_three.addEventListener('click',function(){
//     if (turn === 1){
//       three_three.textContent = "X";
//
//     }else{
//       three_three.textContent = "O";
//     }
//     turn *= -1;
//
//   });

// console.log(score);
