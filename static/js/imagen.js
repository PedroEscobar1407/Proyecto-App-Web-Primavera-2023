const imagenAjuste =(imagen) => {
    let imagenGrande = document.getElementById(imagen);
    let width = imagenGrande.width;
    let height = imagenGrande.height;
    if (width == 640 && height == 480){
        imagenGrande.width = '1280';
        imagenGrande.height = '1024';
    } else {
        imagenGrande.width = '640';
        imagenGrande.height = '480';
    }
}




        