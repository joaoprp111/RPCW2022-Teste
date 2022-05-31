var express = require('express');
var router = express.Router();
var Cidade = require('../controllers/cidades')
var Ligacao = require('../controllers/ligacoes')
var url = require('url')

function reunirNomes(cidades){
  var l = []
  cidades.forEach(c => {
    var nome = c.nome
    l.push(nome)
  })

  l.sort()
  return l 
}

function gerarInfoDistritos(cidades){
  var lista = []
  var tempObj = {}
  cidades.forEach(c => {
    var d = c.distrito 
    if (tempObj[d] == undefined){
      tempObj[d] = []
    } else {
      tempObj[d].push({'id': c.id, 'nome': c.nome})
    }
  })
  
  var distritos = Object.keys(tempObj)
  distritos.forEach(d => {
    lista.push({'nome': d, 'cidadesPertencentes': tempObj[d]})
  })

  return lista
}

function copiarCidades(cidades){
  var cs = []
  cidades.forEach(c => {
    cs.push(c)
  })

  return cs
}

function encontrarDest(cidades, id){
  var resultado = undefined
  cidades.forEach(c => {
    if(c.id == id)
      resultado = c.nome 
  })

  return resultado
}

/* GET cidades */
router.get('/api/cidades', function(req, res, next) {
  var q = url.parse(req.url,true).query
  if (q.distrito != undefined){
    var d = q.distrito
    Cidade.listarPorDistrito(d)
    .then(cidades => {
      res.status(200).jsonp(cidades)
    })
    .catch(error => {
      res.status(500).jsonp(error)
    })
  }
  else {
    Cidade.listar()
    .then(dados => {
      res.status(200).jsonp(dados)
    })
    .catch(error => {
      res.status(501).jsonp(error)
    })
  }
});

/* GET nomes das cidades */
router.get('/api/cidades/nomes', function(req, res, next) {
  Cidade.listar()
    .then(cidades => {
      var lista = reunirNomes(cidades)
      res.status(200).jsonp(lista)
    })
    .catch(error => {
      res.status(502).jsonp(error)
    })
});

/* GET cidade */
router.get('/api/cidades/:id', function(req, res, next) {
  var idCidade = req.params.id
  Cidade.listarCidade(idCidade)
    .then(dados => {
      res.status(200).jsonp(dados)
    })
    .catch(error => {
      res.status(503).jsonp(error)
    })
});

/* GET distritos */
router.get('/api/distritos', function(req, res, next) {
  Cidade.listar()
    .then(cidades => {
      var distritos = gerarInfoDistritos(cidades)
      res.status(200).jsonp(distritos)
    })
    .catch(error => {
      res.status(504).jsonp(error)
    })
});

/* GET ligações */
router.get('/api/ligacoes', function(req, res, next) {
  var q = url.parse(req.url,true).query
  if (q.origem != undefined){
    var o = q.origem
    Cidade.listar()
    .then(cidades => {
      var cidadesCopiadas = copiarCidades(cidades)
      Ligacao.listarPorOrigem(o)
      .then(ligacoes => {
        var lista = []
        ligacoes.forEach(l => {
          var idLigacao = l.id 
          var idDest = l.destino
          var nomeDest = encontrarDest(cidadesCopiadas, idDest)
          lista.push({'idLigacao': idLigacao, 'idCidadeDest': idDest, 'nomeCidadeDest': nomeDest})
        })
        res.status(200).jsonp(lista)
      })
      .catch(error => {
        res.status(505).jsonp(error)
      })
    })
    .catch(error => {
      res.status(506).jsonp(error)
    })
  } else if (q.dist != undefined){
    var distancia = q.dist
    Cidade.listar()
    .then(cidades => {
      var cidadesCopiadas = copiarCidades(cidades)
      Ligacao.listarPorDist(distancia)
      .then(ligacoes => {
        var lista = []
        ligacoes.forEach(l => {
          var idLigacao = l.id 
          var idOrig = l.origem 
          var idDest = l.destino
          var nomeDest = encontrarDest(cidadesCopiadas, idDest)
          var nomeOrig = encontrarDest(cidadesCopiadas, idOrig)
          lista.push({'idLigacao': idLigacao, 'idCidadeOrig': idOrig, 'nomeCidadeOrig': nomeOrig, 'idCidadeDest': idDest, 'nomeCidadeDest': nomeDest})
        })
        res.status(200).jsonp(lista)
      })
      .catch(error => {
        res.status(507).jsonp(error)
      })
    })
    .catch(error => {
      res.status(508).jsonp(error)
    })
  }
});


module.exports = router;
