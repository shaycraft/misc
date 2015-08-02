var obj = {
	field1: "blah",
	field2: [1,2,3],
	field3: {
		subfield1: "blahblah",
		subfield2: 42,
		subfield3: {
			supersub: "aaaah!"
		}
	},
	field4: "tots brah"
};

printObj(obj);

function printObj(p, level) {
	if (level == undefined) {
		level = 0;
		console.log(level);
	}
	if (!isObject(p)) {
		console.log(getLeading(level) + p);
		return;
	}
	for (var key in p) {
  		if (p.hasOwnProperty(key)) {
  			if (isObject(p[key])) {
  				console.log(getLeading(level) + '<' + key + '>');
  				printObj(p[key], level+1);
  				console.log(getLeading(level) + '</' + key + '>');
  			} 
  			else if (Array.isArray(p[key])) {
  				for (var i in p[key]) {
  					console.log(getLeading(level) + '<' +  key + '>');
  					printObj(p[key][i], level+1);
  					console.log(getLeading(level) + '</' + key + '>');

  				}
  			}
  			else {
    			console.log(getLeading(level) + '<' + key + '>' + p[key] + '</' + key + '>');
    		}
  		}
  	}
}

function getLeading(level) {
	var sb = [];
	for (var i=0; i < level; i++) {
		sb.push('    ');
	}
	return sb.join('');
}

function isObject (item) {
  return (typeof item === "object" && !Array.isArray(item) && item !== null);
}