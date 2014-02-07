var page = require('webpage').create();
 var system = require('system');
var args = system.args;
console.log(args[0]);


page.viewportSize = { width: 1200, height: 1600 };

page.open('http://sqor.com/sport/nfl', function() {
  setTimeout(function(){
	  page.render('example2.png');
	  phantom.exit();
  }, 3000);
});
