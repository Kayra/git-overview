(function(){

    var tangentSnowballAppControllers = angular.module('tangentSnowballApp.controllers', []);

    tangentSnowballAppControllers.controller('DisplayController', ['GitService', function(GitService) {

        var vm = this;

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
                vm.user = response;
            })
            .error(function(){
                vm.error = "The server seems to be down."
            });
        };

        // vm.getContributors();
        // vm.getPullRequests();
        vm.getIssues();
        // vm.getMostMergesUser();

    }]);

})();
