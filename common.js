const getLoaded = (e) => e.target.plzCall(e.target.response, e.target.bonusArg);
function get(url, responseType, then, arg) {
	var xhr = new XMLHttpRequest();
	xhr.responseType = responseType;
	xhr.plzCall = then;
	xhr.bonusArg = arg;
	xhr.addEventListener("load", getLoaded);
	xhr.open("GET", url);
	xhr.send();
}

function el(props) {
	let e = document.createElement(props.tagName || 'div');
	for (let p in props) e[p] = props[p];
	return e;
}

function toggle(id, className, state) {
	let e = document.getElementById(id);
	if (state) e.classList.add(className);
	else e.classList.remove(className);
	return e;
}

function hide(className) {
	let elements = document.getElementsByClassName(className);
	for (let i = 0; i < elements.length; i++) {
		elements[i].classList.remove(className);
	}
}