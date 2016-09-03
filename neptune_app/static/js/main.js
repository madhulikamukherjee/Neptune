var app=angular.module('NeptuneApp',['ngRoute']);

app.controller("PlanetsController", [ '$scope', '$http', '$routeParams', function($scope,$http,$routeParams){
  
  var planet_id = $routeParams.planet_id;
  uri = '/planets/api/'+planet_id;

  $http.get(uri).success(function(data){
    $scope.returned_string = "Planet name is: "+ data.name + " with radius: " + data.radius;
  });

}]);

app.controller("MoonsController", [ '$scope', '$http', '$routeParams', function($scope,$http,$routeParams){
  
  var moon_id = $routeParams.moon_id;
  uri = '/moons/api/'+ moon_id;
  $http.get(uri).success(function(data){
    $scope.returned_string = "Moon is: "+ data.name + " which was discovered by: " + data.discoverer;
  });
  
}]);

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