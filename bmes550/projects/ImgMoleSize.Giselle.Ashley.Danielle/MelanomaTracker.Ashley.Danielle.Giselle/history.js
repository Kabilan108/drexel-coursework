

var pixelsPerCell = 35;

function Grapher() {
    const that = this;
    // implement your Grapher here

    this.build = function (elemID,max_height,max_width, xData, yData) {
        // Make canvas
        const canvas = document.getElementById("myCanvas");
        const ctx = canvas.getContext("2d");
        this.canvas1 = ctx;

        let yMax = max_width;
        let xMax = max_height;
        //ctx.transform(1, 0, 0, -1, 0, xMax)

        
        


        /**** Format date information ****/
        
        xData =xData.toString();
        const xArr = xData.split(",");

        const day = new Array(xArr.length);
        const month = new Array(xArr.length);
        const year = new Array(xArr.length);

        dateInfo = xArr;
     
        for (let k = 0; k<= dateInfo.length-1; k++){
            const date = dateInfo[k].split("-");
            year[k] =date[0];
            month[k] = date[1];
            day[k] = date[2];
        }

        const xArray = daysSince(day, month, year);
        
        const weekArr = weeksScale(day[0],month[0],year[0]);
        
        /**** Format mole size  ****/
        //Split the string input
        yData = yData.toString();
        
        const yArr = yData.split(",");
        
        
        for (let i = 0; i < yArr.length; i++) {
           yArr[i]= parseFloat(yArr[i]);
        } 
        
        
        const yArray = yArr;
        

        
        //print(yData);

        ctx.fillStyle = "red";
        const xPlx = new Array(xArray.length);
        const yPlx = new Array(xArray.length);
        for (let i = 0; i < xArray.length; i++) {
            let x = parseInt(xArray[i] * xMax/84)+30; //Divide the x axis out into 84 days (12 weeks)
            xPlx[i] = x;
            let y = ((parseInt((15-yArray[i]) * yMax/20))/2)-10;
            
            yPlx[i] = y;
            
            ctx.beginPath();
            ctx.ellipse(x, y, 3, 3, 0, 0, Math.PI * 2);
            ctx.fill();
            

        }
        
        // Draw the line between points
        ctx.strokeStyle = "red";
        for (let j =0; j < xArray.length; j++){
            ctx.beginPath();
            let x2 = parseInt(xPlx[j]);
            let y2 = parseInt(yPlx[j]);
            let xNext = parseInt(xPlx[j+1]);
            let yNext = parseInt(yPlx[j+1]);
            ctx.moveTo(x2, y2);
            ctx.lineTo(xNext, yNext);
            ctx.stroke();
        }

        this.drawAxis(xMax, yMax,weekArr);

    }

    daysSince = function(dayArr, monthArr, yearArr){
        firstDay = dayArr[0];
        firstMonth = monthArr[0];
        firstYear = yearArr[0];
       
        var firstDay = new Date(firstYear, firstMonth-1, firstDay);
        const daysSince = new Array(dayArr.length-1);
        for (let d=0; d<dayArr.length;d++){
            newDay = new Date(yearArr[d], monthArr[d]-1, dayArr[d] );
            var diff = (newDay-firstDay)/(1000*60*60*24); // days sincethe first day
            daysSince[d] = diff;
        }

        // Get the number of previous
        return daysSince
    }

    weeksScale = function(firstDay, firstMonth, firstYear){
       
        var week = new Date(firstYear, firstMonth-1, firstDay);
        const weeks = new Array(12);
        //var week = new Date();
        for (let d=1; d<12;d++){
            week.setDate((week.getDate()+7)); 
            var copyMs = week.getTime();
            var weekLater = new Date(copyMs);  
            weeks[d]= weekLater;
            
        }
        var firstDay = new Date(firstYear, firstMonth-1, firstDay)
        weeks[0] = firstDay;
        //=new Date(firstYear, firstMonth-1, firstDay);
        // Get the number of previous
        return weeks
    }

    this.drawAxis = function(xMax, yMax,weekArr){
        
        //Draw the axes
                //X-axis
        this.canvas1.strokeStyle = "black";
        this.canvas1.lineWidth = 2;
        this.canvas1.beginPath();
        this.canvas1.moveTo(0,(yMax/40)*(15)-10);
        this.canvas1.lineTo(xMax*10,(yMax/40)*(15)-10);
        this.canvas1.stroke();

                //Y-axis
        this.canvas1.beginPath();
        this.canvas1.moveTo(30,0);
        this.canvas1.lineTo(30,yMax);
        this.canvas1.stroke();

        //Add the axes labels
        this.canvas1.font = "12px Helvetica";
        this.canvas1.fillStyle = "black";
        //X-labels
       // for (var i = 0; i <= numXCells; i++){
       //     this.canvas.fillText(`${i-10}`, 46+i*pixelsPerCell, 62+(numYCells/2)*pixelsPerCell);
        //}
        //Y-labels and ticks
        for (var j = 15; j >= 0; j--){
            
            this.canvas1.fillText(`${j}`,10,(yMax/40)*(-j+15)-10 );
            this.canvas1.beginPath();
            this.canvas1.moveTo(25,(yMax/40)*(-j+15)-10);
            this.canvas1.lineTo(35,(yMax/40)*(-j+15)-10);
            this.canvas1.stroke();
            
        }
        
        //X-labels and ticks
        for (var j = 0; j <= weekArr.length-1; j++ ){
            var month = weekArr[j].getMonth()+1;
            var day = weekArr[j].getDate();
            var year = weekArr[j].getYear();
            this.canvas1.fillText(`${month}-${day}-${year-100+2000}`,((xMax/84)*7*j)+30,(yMax/40)*(15)+5 );
            
            this.canvas1.strokeStyle = "#d9d9d9";
            this.canvas1.lineWidth = 2;
            this.canvas1.beginPath();
            this.canvas1.moveTo(((xMax/84)*7*(j+1))+30,0);
            this.canvas1.lineTo(((xMax/84)*7*(j+1))+30,(yMax/40)*(15)-5);
            this.canvas1.stroke();

            this.canvas1.strokeStyle = "black";
            this.canvas1.lineWidth = 2;
            this.canvas1.beginPath();
            this.canvas1.moveTo(((xMax/84)*7*j)+30,(yMax/40)*(15)-5);
            this.canvas1.lineTo(((xMax/84)*7*j)+30,(yMax/40)*(15)-15);
            this.canvas1.stroke();

        }
    }
}

function Mole() {
    const that = this;

    this.populate = function(elemID,user, num_moles) {
        
        num_moles =num_moles.toString();
        const molArr = num_moles.split(",");
        for (let i = 0; i<=molArr.length-1; i++){
            var option = `<a href=\"history.php?username=${user}&mole_id=${molArr[i]}\">Mole ${molArr[i]}</a>`;
            $(`${elemID}`).append(option);
        }
        
    }
}
