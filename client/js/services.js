(function(){

    var tangentSnowballAppServices = angular.module('tangentSnowballApp.services', []);

    var domain = 'http://127.0.0.1:8000/';

    tangentSnowballAppServices.factory("GitService", ['$http', function($http){

        var gitStats = {};

        return gitStats;

    }]);

})();
