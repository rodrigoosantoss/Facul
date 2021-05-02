import React from 'react'
import ReactDOM from 'react-dom'

import AppComponent from './app'

ReactDOM.hydrate(
    <AppComponent comentarios={[]}/>,
    document.querySelector('#app')
)