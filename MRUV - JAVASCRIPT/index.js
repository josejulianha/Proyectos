//_______________ANTES DEL MOVIMIENTO_________________
var automovil = {
  x: 70,
  y: 200,
  velocidad: 0.2, //dividir al velocidad entre 10
  aceleracion: 0.001, //dividir la aceleracion entre 1000
  masa: 100,
  rozInterno: 0,
  podEnergComb: 100,
  rendimientoMotor: 10,
  avanza: false,
};

var canvas, context;

function initialize() {
  canvas = document.getElementById("mycanvas");
  context = canvas.getContext("2d");

  // -------------IMAGEN--------------
  dibujarImagen();

  // ------------------------------------
}

//___________________________________________

//_______________METODOS_____________________

var pista = {
  coef_friccion: 0,
};

var datosDerivados = {
  energiaConsumida: 0,
  cantidadCombustibe: 0,
};

// ------------------AMBIENTE-------------------
function dibujarImagen() {
  // context.drawImage(imgCar, 0, 0, 986, 390, 0, 0, 100, 50);

  context.fillRect(automovil.x, automovil.y, 30, 10);

  context.beginPath();

  //""""""""RUTA""""""""""""
  context.moveTo(0, 210);
  context.lineTo(800, 210);
  context.stroke();
  //""""""""""""""""""""""""

  //""""""""REGLA""""""""""""""""
  dibujarRegla();
  //""""""""""""""""""""""""

  //"""""""""BARRA EC"""""""""""
  dibujarBarraEc();
  //""""""""""""""""""""""""
}
function dibujarRegla() {
  let coordenateX = 100;
  context.font = "12px serif";
  context.fillStyle = "black";

  context.beginPath();
  for (let i = 0; i < 12; i++) {
    let posicion = 5 * i;

    context.moveTo(coordenateX, 220);
    context.lineTo(coordenateX, 230);
    context.fillText(posicion, coordenateX - 3, 245);
    context.moveTo(coordenateX, 225);
    context.lineTo(coordenateX + 50, 225);
    coordenateX += 50;

    if (coordenateX == 700) {
      context.moveTo(coordenateX, 220);
      context.lineTo(coordenateX, 230);
      context.fillText(posicion + 5, coordenateX - 4, 245);
    }
  }
  context.stroke();
}

var Ec = (automovil.masa * Math.pow(automovil.velocidad * 10, 2)) / 2;

function dibujarBarraEc() {
  let width = Ec * 0.05;
  
  if (width > 400) {
    width=400
  }
  

  context.fillStyle = "#808080";
  context.fillRect(270, 20, width, 20);
  context.strokeRect(270, 20, 400, 20);

  context.fillStyle = "#000000";
  context.font = "15px serif";
  context.fillText("Energía Cinética" + " : " + Ec + "J", 90, 35);
}

function movimiento() {
  automovil.avanza = true;
  automovil.velocidad = automovil.velocidad + automovil.aceleracion;
  automovil.x += automovil.velocidad;
  Ec = ((automovil.masa * Math.pow(automovil.velocidad * 10, 2)) / 2).toFixed(
    2
  );
}

function borrarCanvas() {
  canvas.width = 800;
  canvas.height = 400;
}

//___________________________________________

// ___________CONTROL DEL TIEMPO_______________

var interval;

var segundo = 0;
var milisegundos = 0;

//----------------------TIME-----------------------

function controlartiempo() {
  milisegundos++;
  if (milisegundos == 100) {
    milisegundos = 0;
    segundo++;
  }

  var format =
    segundo + "," + (milisegundos < 10 ? "0" + milisegundos : milisegundos);
  document.getElementById("time").innerText = format;
}

//------------------------------------------------

// ---------EMPEZAR MOVIMIENTO-----------
function start() {
  interval = setInterval(() => {
    principal();
  }, 10);
}

// -----------DURANTE EL MOVIMIENTO-------

function principal() {
  // console.log("Ya");
  movimiento();
  controlartiempo();
  dibujarImagen();
  borrarCanvas();
}

// -----------PARAR MOVIMIENTO------------
function stop() {
  clearInterval(interval);
}
// ___________________________________________

// -----------REINICIAR MOVIMIENTO------------
function restart() {
  clearInterval(interval);
}
// ___________________________________________
