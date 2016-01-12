(function(){

    var app = angular.module('tangentSnowballApp', [
        'ui.router',
        'ngResource',
        'ngMessages',
        'tangentSnowballApp.services',
        'tangentSnowballApp.controllers',
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
            .state('display_git_stats', {
                url: '/',
                templateUrl: '/partials/display_git_stats.html',
                controller: 'DisplayController as display',
            });

        $urlRouterProvider.otherwise('/');

    });

})();

