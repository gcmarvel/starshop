// First js

var navModal = document.getElementById("nav-mobile");
var navBtn = document.getElementById("nav-menu");
var navClose = document.getElementById("nav-close");

navBtn.onclick = function() {
  navModal.style.display = "block";};

navClose.onclick = function() {
  navModal.style.display = "none";};

window.onclick = function(event) {
  if (event.target === navModal) {
    navModal.style.display = "none";
  }
};


//Catalogue js

const tableRows = document.querySelectorAll('.table-row');

for (var x=0; x<tableRows.length; x+=1) {
    var magnitude = tableRows[x].children[3];
    var value = parseFloat(magnitude.innerHTML);
    if (value < 7){
        tableRows[x].style.background = '#ffb50f'
    }
}

function addHD(input) {
    if (input.value === '') {
        input.value = 'HD ';
    }
}

// Bundle js

const bundleMenu = document.querySelectorAll('.bundle-listbutton-img');
const bundleContent = document.querySelectorAll('.bundle-card');
const bundleWrapper = document.querySelectorAll('.bundle-content')[0];
var bundleOld = '';
var bundleFlag = true;

function showBundle(bundle) {

    var content = document.getElementById(bundle.id+'-cn');

    for (var x=0;x<bundleMenu.length;x+=1) {
        bundleMenu[x].src = "static/img/" + bundleMenu[x].id + '.jpg';
        bundleContent[x].style.display = 'none';
    }

    if (screen.width < 481) {
        bundleWrapper.style.display = 'block';
        bundle.insertAdjacentElement('afterend', bundleWrapper);
        bundle.scrollIntoView();
        if (bundleOld === bundle) {

            if (bundleFlag===true) {
                bundleFlag = false;
                bundleWrapper.style.animationName = 'slipRev';
                setTimeout(hideContent, 1000)
            } else {
                bundleWrapper.style.animationName = 'slip';
                bundleFlag = true;
            }
        } else {
            bundleWrapper.style.animationName = 'slip';
            bundleFlag = true;
        }
        bundleOld = bundle;
    }

    bundle.src = "static/img/" + bundle.id + 'active.jpg';
    content.style.display = 'grid';
}

window.onload = bundleMobile()
function bundleMobile (){
    if (screen.width < 481) {
        bundleWrapper.style.display = 'none';
    }
}

function hideContent(){
    bundleWrapper.style.display = 'none';
}


// Constellations js

const constellationsimg = document.querySelectorAll('.constellationimg');

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function scaleConstellations(con) {
    document.getElementById('constellation-wrapper').style.opacity = 1;
    fadeOut(document.getElementById('constellation-wrapper'));
    async function fadeOut (conint){
        for (var x=0;x<20;x+=1) {
            conint.style.opacity -= 0.05;
            await sleep(20);
            if (conint.style.opacity <= 0.1) {
                conint.style.display = "none";
                var fullcon = con + "-full";
                document.getElementById(fullcon).style.display = "block";
                fadeIn(document.getElementById(fullcon));

                async function fadeIn(conint) {
                    for (var x = 0; x < 20; x += 1) {
                        conint.style.opacity -= -0.05;
                        await sleep(20);
                        if (conint.style.opacity >= 0.9) {
                            conint.style.opacity = 1;
                        }
                    }
                }

            }
        }
    }
}

async function unscaleConstellations(con) {
    let fullcon = con + "-full";
    document.getElementById(fullcon).style.opacity = 1;
    fadeOut(document.getElementById(fullcon));
    async function fadeOut (conint){
        for (var x=0;x<20;x+=1) {
            conint.style.opacity -= 0.05;
            await sleep(20);
            if (conint.style.opacity <= 0.1){
                conint.style.display = "none";
                document.getElementById('constellation-wrapper').style.opacity = 0.1;
                document.getElementById('constellation-wrapper').style.display = "block";
                fadeIn(document.getElementById('constellation-wrapper'));

                async function fadeIn(conint) {
                    for (var x = 0; x < 20; x += 1) {
                        conint.style.opacity -= -0.05;
                        await sleep(20);
                        if (conint.style.opacity >= 0.9) {
                            conint.style.opacity = 1;
                        }
                    }
                }
            }
        }
    }
}

function animateConstellation(con){
	document.getElementById(con).src = "static/img/" + con + "-anim.gif";
}

function animateConstellationRev(con){
	document.getElementById(con).src = "static/img/" +  con + "-anim-rev.gif";
}

var starlinks = document.getElementsByClassName('star-link');

if (screen.width < 801) {
    for (var i=0;i<starlinks.length;i+=1){
        starlinks[i].removeAttribute('href');
    }

    async function randomConShine() {
        var number = Math.floor(Math.random() * constellationsimg.length);
        var con = constellationsimg[number];
        con.src= "static/img/" + con.id + "-anim.gif";
        await sleep(2000);
        con.src= "static/img/" + con.id + "-anim-rev.gif";
        await sleep(2000);
        randomConShine();
    }

    randomConShine();
}


// Constructor js


var constructorModal = document.getElementById("ConstructorModal");
var constructorBtn = document.getElementById("ConsctructorBtn");
var constructorSpan = document.getElementsByClassName("constructor-modal-close")[0];

constructorBtn.onclick = function() {
  constructorModal.style.display = "block";};

constructorSpan.onclick = function() {
  constructorModal.style.display = "none";};

window.onclick = function(event) {
  if (event.target === constructorModal) {
    constructorModal.style.display = "none";
  }
};

var constellationSelect = document.getElementsByClassName("constellation-select")[0];
var constellationDescription = document.querySelectorAll('.constructor-constellation-description');

constellationSelect.onchange = function showConstellationDescription() {

    for (var i = 0; i < constellationDescription.length; i += 1) {
        constellationDescription[i].style.display = "none";
    }

    document.getElementById(constellationSelect.value).style.display = "block";

}

var starclassSelect = document.getElementsByClassName("starclass-select")[0];
var starclassDescription = document.querySelectorAll('.constructor-starclass-description');

starclassSelect.onchange = function showStarclassDescription() {

    for (var i = 0; i < starclassDescription.length; i += 1) {
        starclassDescription[i].style.display = "none";
    }

    document.getElementById(starclassSelect.value).style.display = "block";

}

var presentSelect = document.getElementsByClassName("present-select")[0];
var presentDescription = document.querySelectorAll('.constructor-present-description');

presentSelect.onchange = function showPresentDescription() {

    for (var i = 0; i < presentDescription.length; i += 1) {
        presentDescription[i].style.display = "none";
    }

    document.getElementById(presentSelect.value).style.display = "block";

}

var currentTab = 0;
showTab(currentTab);

function showTab(n) {
    var x = document.getElementsByClassName("constructor-main");
    x[n].style.display = "flex";
    if (n === 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n === (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "Добавить в корзину";
    } else {
        document.getElementById("nextBtn").innerHTML = "Следующий Шаг";
    }
        fixStepIndicator(n);
}

function nextPrev(n) {
    var x = document.getElementsByClassName("constructor-main");
    if (n === 1 && !validateForm()) return false;
    x[currentTab].style.display = "none";
    currentTab = currentTab + n;
    if (currentTab >= x.length) {
        document.getElementById("constructor-form").submit();
        return false;
    }
        showTab(currentTab);
}

function validateForm() {
    var x, y, i, valid = true;
    x = document.getElementsByClassName("constructor-main");
    y = x[currentTab].getElementsByTagName("select");
    for (i = 0; i < y.length; i++) {
        if (y[i].value === "") {
            valid = false;
        }
    }
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid;
}

function fixStepIndicator(n) {
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    x[n].className += " active";
}



function AdaptConstructor() {
    if (screen.width / screen.height < 1) {
        var allSelectors = document.getElementsByClassName("mobile-selector");
        var constructorTabs = document.getElementsByClassName("constructor-main");
        for (i = 0; i < constructorTabs.length; i++) {
            var options = constructorTabs[i].getElementsByTagName('select')[0].getElementsByTagName('option');
            for (x = 0; x < options.length; x++) {
                allSelectors[i].appendChild(document.createElement("div"));
                allSelectors[i].getElementsByTagName('div')[x].appendChild(document.createElement("p"));
                allSelectors[i].getElementsByTagName('div')[x].className = "mobile-selector-option";
                allSelectors[i].getElementsByTagName('div')[x].getElementsByTagName('p')[0].innerHTML = options[x].value;
                allSelectors[i].getElementsByTagName('div')[x].onclick = function() {setMobileDescription (this.getElementsByTagName('p')[0].innerHTML)};
            }
        }
    }

    var presentSelect = document.getElementsByClassName("present-select")[0];
    if (screen.height <= 480 && screen.height < screen.width) {
        presentSelect.style.maxWidth = '20vw'
    }
    else {
        presentSelect.style.maxWidth = 'auto';
    }
}

function setMobileDescription(n){

    var show = document.getElementById(n);
    var closest = show.closest(".constructor-description");
    var closestDiv = closest.getElementsByTagName('div');
    for (var i = 0; i < closestDiv.length; i += 1) {
        if (closestDiv[i].className !== "constructor-present-row" && closestDiv[i].className !== "constructor-present-row-image" && closestDiv[i].className !== "constructor-present-row-text" && closestDiv[i].className !== "constructor-image-holder") {
            closestDiv[i].style.display = "none";
        }
    }
    show.style.display = 'block';
    var allSelects = document.getElementsByTagName('select');

    for (var i = 0; i < allSelects.length; i += 1) {
        var allOptions = allSelects[i].getElementsByTagName('option');
        for (var x = 0; x < allOptions.length; x += 1) {
            if (allOptions[x].value === n) {
                var selectClosest = allOptions[x].closest("select");
                selectClosest.value = n;
            }
        }
    }

}


window.onresize = window.onload = AdaptConstructor;

//Stories JS

var storymn = document.querySelectorAll('.stories-menu > p');
var storycn = document.querySelectorAll('.storycn');
var storywr = document.querySelector('.stories-content');
var storymb = document.querySelector('.story-mobile-bg img');
var mobilestory = 0;


function getStyle(element, name)
{
    return element.currentStyle ? element.currentStyle[name] : window.getComputedStyle ? window.getComputedStyle(element, null).getPropertyValue(name) : null;
}

var choosestoryflag = true;
async function chooseStory(story) {
    if (choosestoryflag === true) {
        choosestoryflag = false;
        storywr.style.background = 'url(/static/img/ist_pod_' + story + '.jpg)';
        storywr.style.backgroundPositionX = '-18vw';
        storywr.style.backgroundSize = 'cover';
        for (var i = 0; i < storymn.length; i += 1) {
            storymn[i].style.background = "none";
            storymn[i].style.color = "black";
        }
        var cur_story = document.getElementById(story);
        cur_story.style.background = "rgb(25, 52, 167)";
        cur_story.style.color = "white";

        var storycnid = "cn-" + story;
        var cur_storycn = document.getElementById(storycnid);
        var cur_display = getStyle(cur_storycn, 'display');

        if (cur_display !== 'block') {

            for (var i = 0; i < storycn.length; i += 1) {
                var display = getStyle(storycn[i], 'display');
                if (display !== 'none') {
                    fadeOut(storycn[i]);

                    async function fadeOut(storyout) {
                        storyout.style.opacity = 1;
                        for (var x = 0; x < 20; x += 1) {
                            storyout.style.opacity -= 0.05;
                            await sleep(20);
                            if (storyout.style.opacity <= 0.1) {
                                storyout.style.display = "none";
                                fadeIn(cur_storycn);

                                async function fadeIn(cur_storycn) {
                                    cur_storycn.style.display = 'block';
                                    cur_storycn.style.opacity = 0;
                                    for (var x = 0; x < 20; x += 1) {
                                        cur_storycn.style.opacity -= -0.05;
                                        await sleep(20);
                                        if (cur_storycn.style.opacity >= 0.9) {
                                            cur_storycn.style.opacity = 1;
                                            choosestoryflag = true;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        } else {
            choosestoryflag = true;
        }
    }
}

var movestoryflag = true;

function prevstory(){
    if (movestoryflag === true) {
        movestoryflag = false;
        if (mobilestory !== 0) {
            prevMove(storycn[mobilestory]);

            function prevMove(story) {
                var prevstorycn = storycn[mobilestory - 1];
                var pos = 0;
                var id = setInterval(frame, 5);

                function frame() {
                    if (pos === 100) {
                        clearInterval(id);
                        prevstorycn.style.left = 'inherit';
                        mobilestory--;
                        movestoryflag = true;
                    } else if (pos === 50) {
                        pos++;
                        story.style.display = 'none';
                        story.style.left = 'inherit';
                        prevstorycn.style.left = (-200 + (pos * 2)) + "vw";
                        prevstorycn.style.display = 'block';
                        storymb.src = '/static/img/ist_pod_story-' + mobilestory + '_MOB.jpg';
                    } else if (pos > 50 && pos < 100) {
                        pos++;
                        prevstorycn.style.left = (-200 + (pos * 2)) + "vw";
                    } else if (pos < 50) {
                        pos++;
                        story.style.left = (pos * 2) + "vw";
                    }
                }
            }
        } else {
        movestoryflag = true;
        }
    } else {
    movestoryflag = true;
    }
}

function nextstory(){
    if (movestoryflag === true) {
        movestoryflag = false;
        if (mobilestory < (storycn.length - 1)) {
            nextMove(storycn[mobilestory]);

            function nextMove(story) {
                var nextstorycn = storycn[mobilestory + 1];
                var pos = 0;
                var id = setInterval(frame, 5);

                function frame() {
                    if (pos === 100) {
                        clearInterval(id);
                        nextstorycn.style.right = 'inherit';
                        mobilestory++;
                        movestoryflag = true;
                    } else if (pos === 50) {
                        pos++;
                        story.style.display = 'none';
                        story.style.right = 'inherit';
                        nextstorycn.style.right = (-200 + (pos*2)) + "vw";
                        nextstorycn.style.display = "block";
                        storymb.src = '/static/img/ist_pod_story-' + (mobilestory + 2) + '_MOB.jpg';
                    } else if (pos > 50 && pos < 100) {
                        pos++;
                        nextstorycn.style.right = (-200 + (pos *2)) + "vw";
                    } else if (pos < 50) {
                        pos++;
                        story.style.right = (pos * 2) + "vw";
                    }
                }
            }
        } else {
        movestoryflag = true;
        }
    } else {
        movestoryflag = true;
    }
}

storywr.addEventListener('touchstart', handleTouchStart, false);
storywr.addEventListener('touchmove', handleTouchMove, false);

var xDown = null;
var yDown = null;

function getTouches(evt) {
  return evt.touches
}

function handleTouchStart(evt) {
    const firstTouch = getTouches(evt)[0];
    xDown = firstTouch.clientX;
    yDown = firstTouch.clientY;
};

function handleTouchMove(evt) {
    if ( ! xDown || ! yDown ) {
        return;
    }

    var xUp = evt.touches[0].clientX;
    var yUp = evt.touches[0].clientY;

    var xDiff = xDown - xUp;
    var yDiff = yDown - yUp;

    if ( Math.abs( xDiff ) > Math.abs( yDiff ) ) {
        if ( xDiff > 0 ) {
            if (movestoryflag === true) {
                nextstory()
            }
        } else {
            if (movestoryflag === true) {
                prevstory()
            }
        }
    }
    /* reset values */
    xDown = null;
    yDown = null;
};

var SendStoryModal = document.getElementById("SendStoryModal");
var SendStoryBtn = document.getElementById("SendStoryBtn");
var SendStorySpan = document.getElementById("SendStoryClose");

SendStoryBtn.onclick = function() {
  SendStoryModal.style.display = "block";};

SendStorySpan.onclick = function() {
  SendStoryModal.style.display = "none";};

window.onclick = function(event) {
  if (event.target === SendStoryModal) {
    SendStoryModal.style.display = "none";
  }
};

/*Preloader*/

function preloader() {
	if (document.images) {
	    for (var i=0;i<constellationsimg.length;i+=1) {
	        var conid = constellationsimg[i].id;
	        var img1 = new Image();
		    var img2 = new Image();
            img1.src = "static/img/" + conid + "-anim.gif";
		    img2.src = "static/img/" +  conid + "-anim-rev.gif";
        }

        var img1 = new Image();
        img1.src = "static/img/bg-choosestar-rotated.jpg";

        for (var i=0;i<storymn.length;i+=1) {
            var storid = storymn[i].id;
            var img1 = new Image();
            var img2 = new Image();
            img1.src = 'static/img/ist_pod_' + storid + '.jpg';
            img2.src = 'static/img/ist_pod_' + storid + '_MOB.jpg';
        }

	}
}

function addLoadEvent(func) {
	var oldonload = window.onload;
	if (typeof window.onload != 'function') {
		window.onload = func;
	} else {
		window.onload = function() {
			if (oldonload) {
				oldonload();
			}
			func();
		}
	}
}

addLoadEvent(preloader);