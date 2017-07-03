const casper = require('casper').create({
    verbose: true,
    logLevel: 'error',
    clientScripts: [],
    pageSettings: {
        loadImages:  false,        // The WebPage instance used by Casper will
        loadPlugins: false,         // use these settings
        userAgent : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    },
});

casper.on('resource.requested', function(requestData, request) {
  // List of URLs to skip. Entering part of a hostname or path is OK.
  var blackList = [
    'b3.mookie1.com',
    'googleads.g.doubleclick.net',
    'googlesyndication',
    'https://staticxx.facebook.com',
    'https://www.facebook.com',
    'http://platform.twitter.com',
    'https://apis.google.com'
  ];
  var blackListLength = blackList.length;
  // If a match is found, abort the request.
  for (var i = 0; i < blackListLength; i++) {
    if (requestData.url.indexOf(blackList[i]) > -1) {
      casper.log('Skipped: ' + requestData.url, 'info');
      request.abort();
    }
  }
});


casper.start('mylinkyo', function(){
  //do stuff
});

casper.run(function(){
    this.echo("I AM THE END").exit();
});
