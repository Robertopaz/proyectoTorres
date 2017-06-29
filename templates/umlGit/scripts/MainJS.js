var ruta = 'http://192.168.1.112:666/diagram/getnotification/238285/1/123/file1';
var nombreClase = new Array(); //array para guardar los nombres de las clases
var metodosClase = new Array(); //array para guardar los metodos de cada una de las clases
var atributosClase = new Array(); //array para guardar atributos de cada clase
var contenidosMetodos = new Array();//array para guardar los contenidos de los metodos
var relacionesClases = new Array();//array para guardar las relaciones entre las clases
var iJSON = 0;
var attrlbl = null;
var methodName = null;

var jsonMsg = [];
    ajaxJSON = new XMLHttpRequest();
    ajaxJSON.open('GET', ruta, true);
    ajaxJSON.send();
    ajaxJSON.onreadystatechange=function(){
        if(ajaxJSON.readyState==4){
            jsonMsg= JSON.parse(ajaxJSON.responseText);
            dibujar(jsonMsg);
            //console.log(jsonMsg);
        }
    };


function dibujar( arreglo) {
    jsonMsg = arreglo;
    

    //establecer el canvas
    var canvas = new draw2d.Canvas("gfx_holder");
    canvas.installEditPolicy(  new draw2d.policy.connection.DragConnectionCreatePolicy({
    createConnection: function(){
        var connection = new draw2d.Connection({
            stroke:3,
            outlineStroke:1,
            outlineColor:"#303030",
            color:"91B93E",
            router:new draw2d.layout.connection.CircuitConnectionRouter()
        });
        return connection;
    }
    }));
    
    canvas.installEditPolicy(new draw2d.policy.canvas.FadeoutDecorationPolicy());
    
    canvas.installEditPolicy(  new draw2d.policy.connection.DragConnectionCreatePolicy({
        createConnection: function(){
            return new MyConnection();
        }
    }));

    canvas.installEditPolicy(new draw2d.policy.canvas.BoundingboxSelectionPolicy);

    this.inputLocator  = new CollapsibleInputLocator();
    this.outputLocator = new CollapsibleOutputLocator();
    
    //timeOut necesario para la vista previa. Hack :v la documentación dice que no saben
    //porque lo necesita
    setTimeout(function() {
        updatePreview(canvas);
    },1);

    var clases = []
    
    //recorrer el json y crear las clases en el canvas
    jsonMsg.forEach(function(element) {
        nombreClase[iJSON] = element.nombre;
        element.atributos.push(" ");
        //atributosClase[iJSON] = jsonMsg[iJSON].atributos;
        relacionesClases[iJSON] = element.relaciones;
        var clase = new CollapsibleShape({x: 150 + (iJSON*100), y:150+(iJSON*100)});
        clase.NAME = nombreClase[iJSON];
        clases.push(clase);
        iJSON++;
    });


    for(i = 0; i < clases.length; i++)
    {
        canvas.add(clases[i]);
    }

    for(i = 0; i < clases.length; i++){
        for(j = 0; j < relacionesClases.length; j++){
            for(k = 0; k < clases.length; k++){
                if(relacionesClases[i][j] == clases[k].NAME){
                    //console.log("Clase: " + clases[i].NAME + " rel: " + relacionesClases[i][j]);
                    var c = new MyConnection({
                        targetDecorator: new draw2d.decoration.connection.ArrowDecorator(),
                        source:clases[i].getOutputPort(0),
                        target:clases[k].getInputPort(0)
                    });
                    canvas.add(c);
                }
            }
        }
    }

    canvas.getFigures().each(function(i,f){
        f.getPorts().each(function(i,port){
            port.setConnectionAnchor(new draw2d.layout.anchor.FanConnectionAnchor(port));
        });
    });

    //informacion adicional en el canvas
    var info = new draw2d.shape.note.PostIt({text:"-Clic sobre las clases para expandir/contraer \n -Seleccion multiple de figuras con el raton \n -Clic derecho sobre viste previa para guardar diagrama"});
    canvas.add(info, 20,20);


    //Vista previa 
    $("body").scrollTop(0).scrollLeft(0);
    canvas.getCommandStack().addEventListener(function(e){
        if(e.isPostChangeEvent()){
          updatePreview(canvas);
        }
    }); 

}

function updatePreview(canvas){
    var xCoords = [];
    var yCoords = [];
    canvas.getFigures().each(function(i,f){
        var b = f.getBoundingBox();
        xCoords.push(b.x, b.x+b.w);
        yCoords.push(b.y, b.y+b.h);
    });
    var minX   = Math.min.apply(Math, xCoords);
    var minY   = Math.min.apply(Math, yCoords);
    var width  = Math.max.apply(Math, xCoords)-minX;
    var height = Math.max.apply(Math, yCoords)-minY;
    
    var writer = new draw2d.io.png.Writer();
    writer.marshal(canvas,function(png){
       $("#preview").attr("src",png);
    }, new draw2d.geo.Rectangle(minX,minY,width,height));
};
