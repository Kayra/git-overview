(function(){

    var gitOverviewAppControllers = angular.module('gitOverviewApp.controllers', []);

    gitOverviewAppControllers.controller('DisplayController', ['GitService', function(GitService) {

        var vm = this;

        vm.getRepository = function(){
            GitService.getRepository()
            .success(function(response){
                vm.repository = response[0];
            })
            .error(function(){
                vm.error = "The server seems to be down."
            });
        };

        vm.getContributors = function(){
            GitService.getContributors()
            .success(function(response){
                vm.contributors = response;
            })
            .error(function(){
                vm.error = "The server seems to be down."
            });
        };

        vm.getPullRequests = function(){
            GitService.getPullRequests()
            .success(function(response){
                vm.pullRequests = response;
            })
            .error(function(){
                vm.error = "The server seems to be down."
            });
        };

        vm.getIssues = function(){
            GitService.getIssues()
            .success(function(response){
                vm.issues = response;
            })
            .error(function(){
                vm.error = "The server seems to be down."
            });
        };

        vm.getMostMergesUser = function(){
            GitService.getMostMergesUser()
            .success(function(response){
                vm.user = response[0];
            })
            .error(function(){
                vm.error = "The server seems to be down."
            });
        };

        vm.getRepository();
        vm.getContributors();
        vm.getPullRequests();
        vm.getIssues();
        vm.getMostMergesUser();

    }]);

})();
