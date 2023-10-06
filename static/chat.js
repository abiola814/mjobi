var col = document.getElementsByClassName("collapse");


for (let i=0; i<col.length;i++){
    col[i].addEventListener("click",function(){
        console.log('click');
        this.classList.toggle("active");
        var contnet= this.nextElementSibling;
        console.log(contnet)
        if (contnet.style.maxHeight){
            contnet.style.maxHeight=null;
        }
        else{
            contnet.style.maxHeight=contnet.scrollHeight + "px";
        }
    });
}

function getTime() {
    let today = new Date();
    hours = today.getHours();
    minutes = today.getMinutes();

    if (hours < 10) {
        hours = "0" + hours;
    }

    if (minutes < 10) {
        minutes = "0" + minutes;
    }

    let time = hours + ":" + minutes;
    return time;
}

// Gets the first message
function firstBotMessage() {
    let firstMessage = `Hello Welcome to GBTECH
                            How can we help you`
    document.getElementById("chat-msg").innerHTML = '<p class="chat-bot"><span>' + firstMessage + '</span></p>';

    let time = getTime();

    $("#chat-time").append(time);
    document.getElementById("chat-input").scrollIntoView(false);
}

firstBotMessage();

// Retrieves the response
function getHardResponse(userText) {
    let botResponse = getBotResponse(userText);
    let botHtml = '<p class="chat-bot"><span>' + botResponse + '</span></p>';
    $("#chat-box").append(botHtml);

    document.getElementById("chat-bar-bottom").scrollIntoView(true);
}

//Gets the text text from the input box and processes it
function getResponse() {
    let userText = $("#textinput").val();

    if (userText == "") {
        return false;
    }

    let userHtml = `<p class="userText"><span> ${ userText }</span></p>`;

    $("#textinput").val("");
    $("#chat-box").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    setTimeout(() => {
        getHardResponse(userText);
    }, 3000)

}

// Handles sending text via button clicks
function buttonSendText(sampleText) {
    let userHtml = `<p class="userText"><span> ${ sampleText } </span></p>`;

    $("#textinput").val("");
    $("#chat-box").append(userHtml);
    document.getElementById("chat-bar-bottom").scrollIntoView(true);

    //Uncomment this if you want the bot to respond to this buttonSendText event
    // setTimeout(() => {
    //     getHardResponse(sampleText);
    // }, 1000)
}

function sendButton() {
    getResponse();
}

function heartButton() {
    buttonSendText("Heart clicked!")
}

// Press enter to send a message
$("#textInput").keydown(function (e) {
    console.log(e.charcode === 13)
    if (e.charcode === 13) {
        getResponse();
    }
});

function getBotResponse(input) {
    let userText = $('#textinput').val();    

    if (userText){
        return "A Developer will be with you shortly";
    }
    
}