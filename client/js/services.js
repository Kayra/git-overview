(function(){

    var tangentSnowballAppServices = angular.module('tangentSnowballApp.services', []);

    var domain = 'http://127.0.0.1:8000/';

    tangentSnowballAppServices.factory("GitService", ['$http', function($http){

        var gitStats = {};

        gitStats.getContributors = function(){
            return $http.get(domain + 'git/get-contributors');
        };

        gitStats.getPullRequests = function(){
            return $http.get(domain + 'git/get-pull-requests');
        };

        gitStats.getIssues = function(){
            return $http.get(domain + 'git/get-issues');
        };

        gitStats.getMostMergesUser = function(){
            return $http.get(domain + 'git/get-most-merges-user');
        };

        return gitStats;

    }]);

})();
