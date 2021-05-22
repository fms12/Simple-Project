******* show time using javascript ************

function add_zero(number) {
    if (number < 10) {
        return '0' + number.tostring();
    } else {
        return number.toString();
    }
}

window.setInterval(function () {
    var currentTime = new Date();
    var hour = currentTime.getHours()
    var min = currentTime.getMinutes()
    var sec = currentTime.getSeconds()
    
    document.getElementById('hours').innerHTML=add_zero(hour)
    document.getElementById('minutes').innerHTML=add_zero(min)
    document.getElementById('seconds').innerHTML = add_zero(sec)
    
    
},1000)
