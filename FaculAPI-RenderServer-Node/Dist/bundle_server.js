(()=>{"use strict";var e={n:n=>{var t=n&&n.__esModule?()=>n.default:()=>n;return e.d(t,{a:t}),t},d:(n,t)=>{for(var r in t)e.o(t,r)&&!e.o(n,r)&&Object.defineProperty(n,r,{enumerable:!0,get:t[r]})},o:(e,n)=>Object.prototype.hasOwnProperty.call(e,n)};const n=require("express");var t=e.n(n);const r=require("react");var o=e.n(r);const a=require("react-dom/server");var i=e.n(a);const l=require("axios");var c=e.n(l);function s(e){return o().createElement(o().Fragment,null,o().createElement("h3",null,o().createElement("strong",null,"LISTA DE COMENTÁRIOS:")),o().createElement("hr",null),o().createElement("ul",null,e.comentarios.map((e=>o().createElement("li",{key:e.id},o().createElement("span",null,e.name," - ",e.message),o().createElement("button",{type:"button",onClick:()=>{return n=e.id,void console.log(n);var n}},"Excluir")))),o().createElement("li",null)))}const m=t()();m.get("/",(function(e,n){c().get("http://localhost:3030/comentarios").then((function(e){const t=`\n    <!DOCTYPE html>\n    <html lang="en">\n        <head>\n            <meta charset="UTF-8">\n            <meta http-equiv="X-UA-Compatible" content="IE=edge">\n            <meta name="viewport" content="width=device-width, initial-scale=1.0">\n            <title>React no servidor</title>\n        </head>\n        <body>\n            <div id="app">\n                ${i().renderToString(o().createElement(s,{comentarios:e.data}))}\n            </div>\n            <script src="bundle_cliente.js"><\/script>\n        </body>\n    </html> \n        `;n.send(t)}))})),m.get("/comentarios",(function(e,n){n.send([{id:"001",name:"Rodrigo",message:"Primeiro comentário"},{id:"002",name:"Rodrigo Caetano",message:"Segundo comentário"},{id:"003",name:"Rodrigo Caetano dos Santos",message:"Terceiro comentário"}])})),m.listen(3030,(function(){console.log("Servidor no ar -> na porta 3030")}))})();