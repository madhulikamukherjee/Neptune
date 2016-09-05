var app=angular.module('NeptuneApp',['ngRoute']);





app.config(['$routeProvider','$locationProvider', function($routeProvider, $locationProvider) {
   $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    });

   $routeProvider.
   when('/planets/:planet_id', {
      templateUrl: '/static/templates/planets.html', controller: 'PlanetsController'
   }).
   
   when('/moons/:moon_id', {
      templateUrl: '/static/templates/moons.html', controller: 'MoonsController'
   })
  
}]);