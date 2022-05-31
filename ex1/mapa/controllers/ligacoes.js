var Ligacao = require('../models/ligacoes')

//Listar ligações por origem
module.exports.listarPorOrigem = function(o){
    return Ligacao
        .find({origem: o})
        .exec()
}

//Listar ligações por dist
module.exports.listarPorDist = function(distancia){
    return Ligacao
        .find({distância: {$gte: distancia}})
        .exec()
}