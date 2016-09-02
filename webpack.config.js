var webpack = require('webpack');
var path = require('path');

var BUILD_DIR = path.resolve(__dirname, 'wawhfd/static/dist');
var APP_DIR = path.resolve(__dirname, 'wawhfd/static/src');

module.exports = {
    entry: APP_DIR + '/js/index.js',
    output: {
        path: BUILD_DIR,
        filename: 'js/index.js'
    },
    module : {
        loaders : [{
            test : /\.jsx?/,
            include : APP_DIR + '/js',
            loader : 'babel'
        },{
            test: /\.scss/,
            loaders: ['style', 'css', 'sass']
        }]
    },
    sassLoader: {
        includePaths: [
            APP_DIR + '/scss'
        ]
    }
};
