(function(){

    var gitOverviewAppServices = angular.module('gitOverviewApp.services', []);

    var domain = 'http://127.0.0.1:8000/';

    gitOverviewAppServices.factory("GitService", ['$http', function($http){

        var gitOverview = {};

        gitOverview.getRepository = function(){
            return $http.get(domain + 'git/repository');
        };

        gitOverview.getContributors = function(){
            return $http.get(domain + 'git/contributors');
        };

        gitOverview.getPullRequests = function(){
            return $http.get(domain + 'git/pull-requests');
        };

        gitOverview.getIssues = function(){
            return $http.get(domain + 'git/issues');
        };

        gitOverview.getMostMergesUser = function(){
            return $http.get(domain + 'git/most-merges-user');
        };

        return gitOverview;

    }]);

})();
