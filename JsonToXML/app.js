var colors = require('colors');
var fs = require('fs');
checkArgs(process.argv);

fs.readFile(process.argv[2], function(err, data) {
	if (err) throw err;
	console.log('File read'.yellow);
	var str = printObj(JSON.parse(data));
	console.log('Data parsed.'.yellow);
	fs.writeFile(process.argv[3], str, function(err) {
		if (err) throw err;

		console.log('Save completed'.yellow);
	});
});

function checkArgs(args) {
	if (args.length != 4) {
		var msg = 'Usage: ' + args[0] + '<input file> <output file>';
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