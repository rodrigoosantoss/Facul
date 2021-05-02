//Utilizando recurso do babel transformando o import em require
//sem BABEL seria - const express = require('express')

import express from 'express'
import React from 'react'
import ReactDOM from 'react-dom/server'
import axios from 'axios'

import AppComponent from './src/app.js'

// const express = require('express')

//invocando o express e criamos o objeto APP
const app = express()

//com o objeto App criamos as rotas executando a função
app.get('/', function(req, res){
    axios.get('http://localhost:3030/comentarios').then(function(response){
        const html = `
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>React no servidor</title>
        </head>
        <body>
            <div id="app">
                ${ReactDOM.renderToString(<AppComponent comentarios={response.data}/>)}
            </div>
            <script src="bundle_cliente.js"></script>
        </body>
    </html> 
        `
        res.send(html)
    })
    })

app.get('/comentarios', function(req, res){
    res.send([
    {
        id: '001',
        name: 'Rodrigo',
        message: 'Primeiro comentário'
    },
    {
        id: '002',
        name: 'Rodrigo Caetano',
        message: 'Segundo comentário'
    },
    {
        id: '003',
        name: 'Rodrigo Caetano dos Santos',
        message: 'Terceiro comentário'
    }
])
})

//setamos a porta que o serviço sera executado
app.listen(3030, function(){
    console.log('Servidor no ar -> na porta 3030')
})