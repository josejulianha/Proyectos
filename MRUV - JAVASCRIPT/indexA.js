class CanvasFisicaControl {
  constructor() {
    this.canvas = document.getElementById("mycanvas");
    this.context = this.canvas.getContext("2d");
    this.interval;
    this.seconds = 0;
    this.milliseconds = 0;
    this.automovil = {
      x: 70,
      y: 200,
      velocidad: document.getElementById("input_speed").value / 10,
      aceleracion: document.getElementById("input_speed_up").value / 1000,
      masa: 100,
      avanza: false,
    };
    this.drawIntoContext();
    this.changeButton();
  }

  drawIntoContext() {
    this.context.fillRect(this.automovil.x, this.automovil.y, 30, 10);
    this.drawRoad();
    this.drawRule();
    this.drawBar();
  }

  drawRoad() {
    this.context.beginPath();
    this.context.moveTo(0, 210);
    this.context.lineTo(800, 210);
    this.context.stroke();
  }

  drawRule() {
    let coordenateX = 100;
    this.context.font = "12px serif";
    this.context.fillStyle = "black";

    this.context.beginPath();
    for (let i = 0; i < 12; i++) {
      let posicion = 5 * i;

      this.context.moveTo(coordenateX, 220);
      this.context.lineTo(coordenateX, 230);
      this.context.fillText(posicion, coordenateX - 3, 245);
      this.context.moveTo(coordenateX, 225);
      this.context.lineTo(coordenateX + 50, 225);
      coordenateX += 50;

      if (coordenateX == 700) {
        this.context.moveTo(coordenateX, 220);
        this.context.lineTo(coordenateX, 230);
        this.context.fillText(posicion + 5, coordenateX - 4, 245);
      }
    }
    this.context.stroke();
  }
  getValuesInput() {
    this.automovil = {
      ...this.automovil,
      velocidad: document.getElementById("input_speed").value / 10,
      aceleracion: document.getElementById("input_speed_up").value / 1000,
    };
  }
  drawBar() {
    return null;
  }
  deleteCanvas() {
    this.canvas.width = 800;
    this.canvas.height = 400;
    this.drawIntoContext();
  }

  changeTime() {
    this.milliseconds++;
    if (this.milliseconds == 100) {
      this.milliseconds = 0;
      this.seconds++;
    }
    var format =
      this.seconds +
      "," +
      (this.milliseconds < 10 ? "0" + this.milliseconds : this.milliseconds);
    document.getElementById("time").innerText = format;
  }

  changeButton() {
    let btn_container = document.getElementById("btn_container");
    btn_container.innerHTML = "";
    let button = document.createElement("button");
    if (this.automovil.avanza == false) {
      button.innerText = "Empezar";
      button.onclick = () => {
        console.log("empieza");
        this.startMovement();
      };
    } else {
      button.innerText = "Pausar";
      button.onclick = () => {
        console.log("pausa");
        this.stopMovement();
      };
    }
    btn_container.appendChild(button);
  }

  onChangePosition() {
    this.automovil.avanza = true;
    this.automovil.velocidad += this.automovil.aceleracion;
    this.automovil.x += this.automovil.velocidad;
  }
  duringMovement() {
    this.changeTime();
    this.onChangePosition();
    this.drawIntoContext();
    this.deleteCanvas();
  }

  startMovement() {
    this.automovil.avanza = true;
    this.getValuesInput()
    this.changeButton();
    console.log(this.automovil);
    this.interval = setInterval(() => {
      this.duringMovement();
    }, 10);
  }

  stopMovement() {
    this.automovil.avanza = false;
    clearInterval(this.interval);
    this.changeButton();
  }

  restartMovement() {
    this.automovil = {
      ...this.automovil,
      x: 70,
      y: 200,
      velocidad: document.getElementById("input_speed").value / 10,
      avanza: false,
    };
    this.seconds = 0;
    this.milliseconds = 0;

    clearInterval(this.interval);

    document.getElementById("time").innerText = "0,00";
    this.changeButton();
    this.drawIntoContext();
    this.deleteCanvas();
  }
}

let _CanvasFisicaControl = new CanvasFisicaControl();
