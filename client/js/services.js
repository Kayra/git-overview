(function(){

    var gitStatsAppServices = angular.module('gitStatsApp.services', []);

    var domain = 'http://127.0.0.1:8000/';

    gitStatsAppServices.factory("GitService", ['$http', function($http){

        var gitStats = {};

        gitStats.getRepository = function(){
            return $http.get(domain + 'git/repository');
        };

        gitStats.getContributors = function(){
            return $http.get(domain + 'git/contributors');
        };

        gitStats.getPullRequests = function(){
            return $http.get(domain + 'git/pull-requests');
        };

        gitStats.getIssues = function(){
            return $http.get(domain + 'git/issues');
        };

        gitStats.getMostMergesUser = function(){
            return $http.get(domain + 'git/most-merges-user');
        };

        return gitStats;

    }]);

})();
