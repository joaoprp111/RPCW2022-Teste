var Cidade = require('../models/cidades')

//Listar cidades
module.exports.listar = function(){
    return Cidade
        .find({},{_id: 0, id: 1, nome: 1, distrito: 1})
        .exec()
}

//Listar cidades por distrito
module.exports.listarPorDistrito = function(distrito){
    var distritoI = new RegExp(distrito, 'i')
    return Cidade
        .find({distrito: distritoI},{_id: 0, id: 1, nome: 1})
        .exec()
}

//Listar cidade (info completa)
module.exports.listarCidade = function(idCidade){
    return Cidade
        .findOne({id:idCidade})
        .exec()
}