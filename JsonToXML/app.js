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

var colors = require('colors');
var fs = require('fs');
checkArgs(process.argv);
var str = printObj(obj);
fs.writeFile(process.argv[2], str, function(err) {
	if (err) {
		throw err;
	}
	console.log('Save completed.'.yellow);
});

function checkArgs(args) {
	if (args.length != 3) {
		var msg = 'Usage: ' + args[0] + ' <output file>';
		console.log(msg.red);
		throw 'Invalid arguments';
	}
}

function printObj(p, level) {
	var sb = [];
	if (level == undefined) {
		level = 0;
	}
	if (!isObject(p)) {
		sb.push(p);
		return sb.join('');
	}
	for (var key in p) {
  		if (p.hasOwnProperty(key)) {
  			if (isObject(p[key])) {
  				sb.push('<' + key + '>');
  				sb.push(printObj(p[key], level+1));
  				sb.push('</' + key + '>');
  			} 
  			else if (Array.isArray(p[key])) {
  				for (var i in p[key]) {
  					sb.push('<' +  key + '>');
  					sb.push(printObj(p[key][i], level+1));
  					sb.push('</' + key + '>');
  				}
  			}
  			else {
    			sb.push('<' + key + '>' + p[key] + '</' + key + '>');
    		}
  		}
  	}
  	return sb.join('');
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