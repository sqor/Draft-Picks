var page = require('webpage').create();
 var system = require('system');
var args = system.args;
console.log(args[0]);

var url = args[1];
var outputFile= args[2];

page.viewportSize = { width: 1200, height: 1600 };

page.open(url, function() {
  setTimeout(function(){
	  page.render(outputFile);
	  phantom.exit();
  }, 3000);
});
