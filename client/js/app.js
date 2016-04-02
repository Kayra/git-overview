(function(){

    var app = angular.module('gitOverviewApp', [
        'ui.router',
        'ngResource',
        'gitOverviewApp.services',
        'gitOverviewApp.controllers',
    ])

    .config(function($interpolateProvider, $httpProvider, $resourceProvider, $stateProvider, $locationProvider, $urlRouterProvider){

        // CSRF Support
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

        // Routing
        $locationProvider.html5Mode({
          enabled: true,
          requireBase: false
        });

        $stateProvider
            .state('display_git_overview', {
                url: '/',
                templateUrl: '/partials/display_git_overview.html',
                controller: 'DisplayController as display',
            });

        $urlRouterProvider.otherwise('/');

    });

})();

