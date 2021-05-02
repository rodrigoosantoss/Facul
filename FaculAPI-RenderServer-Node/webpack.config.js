const path = require('path')
const { ExternalsPlugin } = require('webpack')

module.exports = {
    entry: '/src/index.js',
    output: {
        //aonde (caminho)que ele irá gerar o arquivo
        //path.RESOLVE - resolve trará o caminho absoluto
        path: path.resolve(__dirname, 'Dist'),
        filename: 'bundle_server.js',
    },
    module: {
        rules: [{
            test: /.js/,
            use: 'babel-loader'
        }]
    },
}   