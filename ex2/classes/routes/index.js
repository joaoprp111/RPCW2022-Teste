var express = require('express');
var router = express.Router();
var axios = require('axios');
var url = require('url');

//Proveniente do aquecimento (pedido feito com o postman já explicado em aquecimento.py)
const token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyOTRlY2VhNmI1ZDVjMjQ3NmNmMDhiMSIsImxldmVsIjozLjUsImVudGlkYWRlIjoiZW50X0EzRVMiLCJlbWFpbCI6InJwY3cyMDIyQGdtYWlsLmNvbSIsImlhdCI6MTY1NDAxMzQzOCwiZXhwIjoxNjU0MDQyMjM4fQ.ywPwGgXaLqUpreD3xumGfHSEwWHVr00N1dvxEAcoig-mMYwdVdbYiJBUs_IhPV3zBxzgbin0l6VyxKzXLbjGTVPmTWOCmHe5CttV5QhiF5oXNIl7Mprxdg37j0C70JQ-G1hTSG9x9-TiaqZOMFFWd90WiFDnRwmmSycUGLj5qCfr8zbr4g5oqsO-SqcehSSVhWtl1IOVhMlIgMufbe6bKC8Sbxf7lcCZSZlhVCC_6wCHNdiiN2tTGT8wAqmmYjw1eRFXDpB29XEPINKaTJRds3WL3ta4Cd6rzlnIa2YlYD3ZzawvKnLtTYVA2nM00zukOj_qkxL5nR7l_niuDX8Arw"

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Processos e termos de índice do CLAV' });
});

router.get('/classes', function(req, res, next) {
  axios.get('http://clav-api.di.uminho.pt/v2/classes?token=' + token)
    .then(dados => {
      res.render('classes', { title: 'Classes (nível 1)', classes: dados.data});
    })
    .catch(error => {
      res.render('error', {error: error})
    })
});

router.get('/classes/:codigo', function(req, res, next) {
  var q = url.parse(req.url,true).query
  if (q.origem != undefined && q.idOrigem != undefined){
    var codigo = req.params.codigo
    var o = q.origem 
    var idO = q.idOrigem
    axios.get('http://clav-api.di.uminho.pt/v2/classes/' + codigo + '?token=' + token)
      .then(dados => {
        var classe = dados.data
        console.log(classe)
        res.render('classe', { title: 'Classe ' + classe.codigo, classe: classe, origem: o, idOrigem: idO});
      })
      .catch(error => {
        res.render('error', {error: error})
      })
  }
  else{
    var codigo = req.params.codigo
    axios.get('http://clav-api.di.uminho.pt/v2/classes/' + codigo + '?token=' + token)
      .then(dados => {
        var classe = dados.data
        console.log(classe)
        res.render('classe', { title: 'Classe ' + classe.codigo, classe: classe});
      })
      .catch(error => {
        res.render('error', {error: error})
      })
  }
});

router.get('/termos', function(req, res, next) {
  axios.get('http://clav-api.di.uminho.pt/v2/termosIndice?token=' + token)
    .then(dados => {
      var termos = dados.data
      res.render('termos', { title: 'Termos de índice', termos: termos});
    })
    .catch(error => {
      res.render('error', {error: error})
    })
});

module.exports = router;
