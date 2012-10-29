function makeButtonFunction()
{
	document.getElementsByClassName("makeButton")[0].innerHTML="Make2!";
	// save which recipe was clicked as default for making recipe
}

function mustHaveFunction(e)
{
	if (e.keyCode == 13) {
		alert("you hit return!");
	}
}

function cantHaveFunction(e)
{
	if (e.keyCode == 13) {
		alert("you hit return!");
	}
}

function checkBox()
{
	if (checkbox.checked) {
        alert("Checked");
    }
    else if (!checkbox.checked) {
		alert("Unchecked");
    }     
}