// script = document.createElement('script')
// script.src = "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"
// document.body.appendChild(script)
window.addEventListener('load', (event) => {
    load()
});
let selectedElem, postcontent, privacydecision, gl = "false";
function load() {
    postcontent = document.getElementsByClassName("posttxt")
    for (x = 0; x < postcontent.length; x++) {
        postcontent[x].addEventListener('click', function (evt) {
            selectedElem = evt
            text = document.getElementById(evt.srcElement.id).innerHTML;
            openDialog(text, selectedElem.srcElement.parentElement.children[1].children[1].children[0].value)
        })

        temp = postcontent[x].innerHTML
        temp = temp.replaceAll("&lt;","<")
        temp = temp.replaceAll ("&gt;",">")
        postcontent[x].innerHTML = temp
    }

    privacydecision = document.getElementsByClassName('privacy')
    for (x = 0; x < privacydecision.length; x++) {
        privacydecision[x].addEventListener('click', function (evt) {
            if (evt.srcElement.value == '1') {
                evt.srcElement.value = "0"
                $(evt.srcElement).attr("checked", false)
            }
            else {
                evt.srcElement.value = "1"
                $(evt.srcElement).attr("checked", true)
            }
            email = document.getElementById("state")
            obj = evt.srcElement.parentElement.parentElement.parentElement.children[0]
            idd = obj.id
            idd = idd.substring(idd.lastIndexOf('$') + 1)
            obj = obj.innerHTML

            upload(obj, idd, email.innerHTML, false, evt.srcElement.value)
        })
    }


}


add = document.getElementById("icon-add");
add.addEventListener('click', openDialog)
topmost = document.getElementById("topmost")
topmost.addEventListener('click', function (evt) {
    sendBack(evt)
})
let New = true
let newelem, newelemvalue, content;
function sendBack(event) {

    topmost.setAttribute("style", "background-color: transparent; z-index: -1")
    email = document.getElementById("state")
    if (New) {

        txt = document.getElementById("writeTxt").innerText;
        txt1 = document.getElementById("writeTxt").innerHTML;
        // txt = txt.replaceAll("<br>","\n")
        if (txt.length > 0) {
            upload(txt1, len, email.innerHTML, true, newelemvalue)

            createNewpost(txt)
            load()
        }
        newelem.remove()
    }
    else {
        txt = document.getElementById("writeTxt").innerText;
        // txt = txt.replaceAll("<br>","\n")
        txt1 = document.getElementById("writeTxt").innerHTML;
        document.getElementById(selectedElem.srcElement.id).innerText = txt
        if (txt.length == 0) {
            document.getElementById(selectedElem.srcElement.id).remove()
        }
        else {
            idd = selectedElem.srcElement.id
            idd = idd.substring(idd.lastIndexOf('$') + 1)
            modelem = selectedElem.srcElement.parentElement.lastElementChild.children[1].children[0]
            if (newelemvalue == 1) {
                $(modelem).attr("checked", true)
            }
            else {
                $(modelem).attr("checked", false)
            }
            upload(txt, idd, email.innerHTML, false, newelemvalue)
        }
        newelem.remove();
    }
}
function openDialog(txt, val = "1") {
    topmost.setAttribute("style", "background-color: rgba(84, 82, 82, 0.559); z-index: 4")
    newelem = document.createElement('div')
    newelem.setAttribute("name", "txtarD")
    newelem.setAttribute("id", "txtarD")
    newelem.setAttribute("cols", "30")
    newelem.setAttribute("rows", "30")

    if (gl == "false") {
        newoptsB = document.createElement("div")
        newoptsB.setAttribute("class", "optsB")
        newelem.appendChild(newoptsB)
    }
    newpara = document.createElement("p")
    if (gl == "false")
        newpara.setAttribute("contenteditable", "true")
    newpara.setAttribute("id", "writeTxt")
    newelem.appendChild(newpara)

    if (gl == "false") {
        newbeforeoptsB = document.createElement("div")
        newbeforeoptsB.setAttribute("class", "beforeoptsB")

        newoptsB.appendChild(newbeforeoptsB)


        newswitchB = document.createElement('label')
        newswitchB.setAttribute("class", "switchB")
        newswitchB.setAttribute("id", "switB")

        newoptsB.appendChild(newswitchB)

        newinputprivacy = document.createElement("input")
        newinputprivacy.setAttribute("type", "checkbox")
        newinputprivacy.setAttribute("name", "privacyB")
        newinputprivacy.setAttribute("class", "privacyB")
        if (val == 1)
            newinputprivacy.setAttribute("checked", "checked")
        newinputprivacy.setAttribute("value", val)
        newelemvalue = val
        newswitchB.appendChild(newinputprivacy)

        newsliderB = document.createElement("span")
        newsliderB.setAttribute("class", "sliderB")
        newswitchB.appendChild(newsliderB)
    }

    if (txt.length > 0) {
        New = false
        newpara.innerHTML = txt
    }
    else {
        New = true
    }

    document.body.appendChild(newelem)
    newelem.children[0].children[1].children[0].addEventListener('click', () => {
        val = newelem.children[0].children[1].children[0].value
        if (val == "1") {
            newelemvalue = 0;
            newelem.children[0].children[1].children[0].value = "0"
        }
        else {
            newelemvalue = 1;
            newelem.children[0].children[1].children[0].value = "1"
        }

    })
}


function createNewpost(txt) {
    if (txt.length > 0) {
        content = document.getElementsByClassName("content-Handler")

        newcontenHolder = document.createElement("div")

        newcontenHolder.setAttribute("class", "content-holder")
        newcontenHolder.setAttribute("id", "contH")

        newcontenHolderP = document.createElement('p')

        newTxt = document.createTextNode(txt)
        newcontenHolderP.setAttribute("class", "posttxt")
        email = document.getElementById("state").innerHTML
        newcontenHolderP.setAttribute("id", "posttxt $" + email + "_" + len)
        len++
        newcontenHolderP.appendChild(newTxt)

        newcontenHolder.appendChild(newcontenHolderP)

        newopts = document.createElement('div')
        newopts.setAttribute("class", "opts")
        newcontenHolder.appendChild(newopts)

        newbeforeopts = document.createElement("div")
        newbeforeopts.setAttribute("class", "beforeopts")
        newopts.appendChild(newbeforeopts)

        newswitch = document.createElement("label")
        newswitch.setAttribute("class", "switch")
        newswitch.setAttribute("id", "swit")

        newopts.appendChild(newswitch)

        newinput = document.createElement("input")
        newinput.setAttribute("type", "checkbox")
        newinput.setAttribute("class", "privacy")
        newinput.setAttribute("name", "privacy")

        if (newelemvalue == 1) {
            newinput.setAttribute("checked", "checked")
        }
        newinput.setAttribute("value", newelemvalue)

        newswitch.appendChild(newinput)

        newslider = document.createElement("span")
        newslider.setAttribute("class", "slider")
        newswitch.appendChild(newslider)
        /*newcontenHolder.addEventListener('click', function (evt) {
            text = newcontenHolder.children[0].innerText
            openDialog(text)
        })*/

        newdeletebutton = document.createElement('button')
        newdeletebutton.setAttribute("class","del");
        newdeletebutton.setAttribute("onclick","del(this)");
        newdeletebutton.innerHTML = "Delete"
        newdeletebutton.setAttribute("id","del$"+email + "_" + (len-1));
        newopts.appendChild(newdeletebutton)

        for (let x = 0; x < content.length; x++) {
            content[x].append(newcontenHolder)
        }
    }
}

icong = document.getElementById("icon-global")
icong.addEventListener('click', () => {
    globe("?global=g")
    //heartInitial()
    gl = "true"
    document.getElementById("icon-add").setAttribute("style", "display:none")
})
iconh = document.getElementById("icon-home")
iconh.addEventListener('click', () => {
    globe("?global=home")
    gl = "false"
    document.getElementById("icon-add").setAttribute("style", "display:inline-flex")
})
function globe(url) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("conH").innerHTML = this.responseText;
            load()
            heartInitial()

        }
    };
    xhttp.open("GET", "./" + url, true);
    xhttp.send();
}

function heartInitial() {
    heart = document.getElementsByClassName("heart")
    let liked;
    for (x = 0; x < heart.length; x++) {
        heart[x].addEventListener('click', (evt) => {
            event1 = evt
            like = evt.srcElement.parentElement.parentElement.children[1]
            likecount = parseInt(like.innerHTML)
            if (evt.srcElement.getAttribute("style") == null || evt.srcElement.getAttribute("style") == "fill:transparent") {
                evt.srcElement.setAttribute("style", "fill:red")
                likecount++;
                like.innerHTML = likecount
                liked = "true"
            }
            else {
                evt.srcElement.setAttribute("style", "fill:transparent")
                likecount--;
                like.innerHTML = likecount
                liked = "false"
            }
            like = evt.srcElement.parentElement.parentElement.children[1]
            likecount = parseInt(like.innerHTML)
            id = event1.srcElement.parentElement.parentElement.parentElement.parentElement.children[0]
            id = id.id
            id = id.substring(id.lastIndexOf("$") + 1);
            email = document.getElementById("state").innerHTML
            uploadg(id, email, likecount, liked)
        })
    }
}