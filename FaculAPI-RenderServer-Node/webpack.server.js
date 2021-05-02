const path = require('path')
const nodeExternals = require('webpack-node-Externals')
const { ExternalsPlugin } = require('webpack')

module.exports = {
    entry: '/server.js',
    output: {
        //aonde (caminho)que ele irá gerar o arquivo
        //path.RESOLVE - resolve trará o caminho absoluto
        path: path.resolve(__dirname, 'Dist'),
        filename: 'bundle_server.js',
    },
    target: 'node',
    module: {
        rules: [{
            test: /.js/,
            use: 'babel-loader'
        }]
    },
    externals: [nodeExternals()]
}   