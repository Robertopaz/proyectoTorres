var CollapsibleShape = draw2d.shape.layout.VerticalLayout.extend({

	NAME: "ClaseSimple",
	
    init : function(attr)
    {
        this.inputLocator  = new CollapsibleInputLocator();
        this.outputLocator = new CollapsibleOutputLocator();
        
        this._super($.extend({bgColor:"#FFFFFF", color:"#39b2e5", stroke:1, radius:2, gap:5},attr));

        //Nombre de la clase
        this.header = new draw2d.shape.layout.HorizontalLayout({
            stroke: 0,
            radius: 0,
            bgColor: "#0AA4C9"
        });
        var label = null;
        var nombreClase1 = nombreClase[iJSON];
        this.header.add(label =new draw2d.shape.basic.Label({
            text: nombreClase1,
            fontColor:"#ffffff",
            stroke:0, 
            fontSize:18, 
            fontFamily:"Oswald",
            padding:{left:20, right:20}
        }));   

        //Icono expandir/contraer
        var img1 = new draw2d.shape.icon.Contract({ minWidth:20, minHeight:20, width:20, height:20});
        var img2 = new draw2d.shape.icon.Expand({  minWidth:20, minHeight:20, width:20, height:20, visible:false });
        img1.setVisible(false);
        img2.setVisible(false);

        //funcion para expandir/contraer
        var toggle=function(){
            this.row1.portRelayoutRequired=true;
            this.row2.portRelayoutRequired=true;

            this.row1.setVisible(!this.row1.isVisible());
            this.row2.setVisible(!this.row2.isVisible());
            
            this.row1.portRelayoutRequired=true;
            this.row1.layoutPorts();

            this.row2.portRelayoutRequired=true;
            this.row2.layoutPorts();
            //img1.setVisible(!img1.isVisible());
            //img2.setVisible(!img2.isVisible());
        }.bind(this);
        //img1.on("click",toggle);
        //img2.on("click",toggle);
        //label.on("click",toggle);
        img1.addCssClass("pointer");
        img2.addCssClass("pointer");
        this.header.add(img1);
        this.header.add(img2);

        //Atributos
        var atribsLabel = null;

        this.row1 = new draw2d.shape.layout.VerticalLayout({
            stroke: 0, 
            radius: 0,
            bgColor: "#A0DAE7"
        });
        this.row1.add(atribsLabel = new draw2d.shape.basic.Label({
            text: "Atributos",
            fontColor: "#000000",
            stroke: 0,
            fontSize: 16,
            fontFamily: "Oswald",
            padding: {left:20, right: 20}
        }));


        if (jsonMsg[iJSON].atributos.length == ""){
            attrlbl = "\n";
            //console.log( nombreClase[iJSON]+"===attr======"+attrlbl);
            this.row1.add(new draw2d.shape.basic.Label({
                    text: attrlbl,
                    fontColor: "#02647B",
                    stroke: 0,
                    fontSize: 14,
                    fontFamily: "Oswald",
                    padding: {left:20, right: 20}
                }));
        }else{
            for(var eAttr=0; eAttr<jsonMsg[iJSON].atributos.length; eAttr++){
                attrlbl = jsonMsg[iJSON].atributos[eAttr];

                //console.log( nombreClase[iJSON]+"===attr======"+attrlbl);
                this.row1.add(new draw2d.shape.basic.Label({
                    text: "- "+attrlbl,
                    fontColor: "#02647B",
                    stroke: 0,
                    fontSize: 14,
                    fontFamily: "Oswald",
                    padding: {left:20, right: 20}
                }));
            }
        }
        
        
        //Metodos
        var methodsLabel = null; //etiqueda para indicar que ahi estan los metodos(encabezado)
        //contenedor de las etiquetas de metodos
        this.row2 = new draw2d.shape.layout.VerticalLayout({ 
            stroke: 0, 
            radius: 0,
            bgColor: "#64AEE6"
        });
        //crear la etiqueta para el encabezado
        this.row2.add(methodsLabel = new draw2d.shape.basic.Label({ //
            text: "Metodos",
            fontColor: "#000000",
            stroke: 0,
            fontSize: 16,
            fontFamily: "Oswald",
            padding: {left:20, right: 20}
        }));

        var obtenerMet= [];

        for(var cMetodos=0; cMetodos<jsonMsg[iJSON].metodos.length; cMetodos++){
            var mName = jsonMsg[iJSON].metodos[cMetodos];
            console.log( nombreClase[iJSON]+"====metd===="+mName);
            this.lblMetodo= null;
            this.lblMetodo = new draw2d.shape.basic.Label({
                stroke: 2,
                padding: {left: 20, right: 20}
            });
            this.lblMetodo.setText(mName);
            this.lblMetodo.setColor("#64AEE6");
            this.lblMetodo.setFontColor("#DEDFE0");
            this.lblMetodo.setFontSize(14);
            obtenerMet = this.lblMetodo.getText();
            this.lblMetodo.onClick= function(){
               alert(obtenerMet);
            };
            this.row2.add(this.lblMetodo);
        }
        
        var inputNode = this.createPort("input",  this.inputLocator);
        var outputNode = this.createPort("output", this.outputLocator);

        var show=function(){this.setVisible(false);};
        var hide=function(){this.setVisible(false);};

        inputNode.on("connect",hide,inputNode);
        inputNode.on("disconnect",show,inputNode);

        outputNode.on("connect",hide,outputNode);
        outputNode.on("disconnect",show,outputNode);

        this.add(this.header);
        this.add(this.row1);
        this.add(this.row2);
    }
});
