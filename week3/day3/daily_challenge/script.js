let input = document.getElementById('text');
let validate = document.createAttribute("onkeypress")
validate.value = "return /[a-z]/i.test(event.key)"
input.setAttributeNode(validate)