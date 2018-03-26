function homerMeta(obj){
clickX = window.event.x-obj.offsetLeft;
clickY = window.event.y-obj.offsetTop;
    if((clickX>=100&&clickX<=200)&&(clickY>=100&&clickY<=200))
    {
    alert(" You are between (100,100) And (200,200) of the Image");
    }
}

console.log('Hi')
