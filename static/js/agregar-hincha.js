
new MultiSelectTag('deportes')
const validateEmail = (email) => {
    if (!email) return false;
    
    let lengthValid = email.length > 15;
  
    
    let re = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    let formatValid = re.test(email);
  
    
    return lengthValid && formatValid;
};

const validatePhoneNumber = (numero) => {
    if (!numero) return true;
    
    let lengthValid = numero.length >= 8;
  
    
    let re = /^[0-9]+$/;
    let formatValid = re.test(numero);
  
    
    return lengthValid && formatValid;
};

const validateName = (nombre) => {
    if (!nombre) return false;
    
    let lengthValid =  80 >= nombre.length && nombre.length >= 3;
  
    
    let re = /^[a-zA-Z\s]+$/;
    let formatValid = re.test(nombre);
  
    
    return lengthValid && formatValid;
};

const validateRegion = (regiones) => {
    if (regiones == "") return false;

    return true;
};

const validateComuna = (comunas) => {
    if (comunas == "") return false;

    return true;
};


const validateTransporte = (transportes) => {
    if (transportes == "") return false;

    return true;
}

const validateComentarios = (comentarios) => {
    let lengthValid = 80 >= comentarios.length;

    return lengthValid;
}

const validateDeportes = (deporte) => {
    let largo = deporte.selectedOptions;
    if (largo.length > 3 || largo.length == 0){
        return false;
    }
    return true;
}


const validateForm = () => {
    let myForm = document.getElementById("hinchaform");
    let email = document.getElementById("email").value;
    let phoneNumber = document.getElementById("numero").value;
    let name = document.getElementById("nombres").value;
    let region = document.getElementById("regiones").value;
    let comuna = document.getElementById("comunas").value;
    let transporte = document.getElementById("transportes").value;
    let comentarios = document.getElementById("comentarios").value;
    let deportes = document.getElementById("deportes");


    let invalidInputs = [];
    let isValid = true;
    const setInvalidInput = (inputName) => {
        invalidInputs.push(inputName);
        isValid &&= false;
    };

    if (!validateEmail(email)) {
        setInvalidInput("Email");
    }

    if (!validatePhoneNumber(phoneNumber)) {
        setInvalidInput("Numero");
    }
    if (!validateName(name)) {
        setInvalidInput("Nombre");
    }
    if (!validateRegion(region)) {
        setInvalidInput("Region");
    }
    if (!validateComuna(comuna)) {
        setInvalidInput("Comuna");
    }
    if (!validateTransporte(transporte)) {
        setInvalidInput("Transporte");
    }
    if (!validateComentarios(comentarios)) {
        setInvalidInput("Comentarios");
    }
    if (!validateDeportes(deportes)) {
        setInvalidInput("Debe seleccionar al menos 1 deporte y maximo 3");
    }

    let validationBox = document.getElementById("val-box");
    let validationMessageElem = document.getElementById("val-msg");
    let validationListElem = document.getElementById("val-list");

    if (!isValid) {
        validationListElem.textContent = "";
        
        for (input of invalidInputs) {
          let listElement = document.createElement("li");
          listElement.innerText = input;
          validationListElem.append(listElement);
        }
        
        validationMessageElem.innerText = "Los siguiente campos son invalidos:";
    
        
        validationBox.hidden = false;
    } else {
        
        validationBox.hidden = true;
        let modal = document.getElementById("myModal");
        modal.hidden = false;
        let final = document.getElementById("final");
        let confirmbtn = document.getElementById("confirmabtn");
        let denybtn = document.getElementById("no-confirmabtn");
        let volverbtn = document.getElementById("volver");
        confirmbtn.addEventListener("click", () => {
            final.hidden = false;
            modal.hidden = true;
            volverbtn.addEventListener("click", () => {window.location.href = "../HTML/index.html"});
        });
        denybtn.addEventListener("click", () => {
            modal.hidden = true;
            final.hidden = true;
        });
        

        
    }
};
    
let submitBtn = document.getElementById("envio");
submitBtn.addEventListener("click", validateForm);

