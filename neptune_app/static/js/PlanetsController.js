app.controller("PlanetsController", [ '$scope', '$http', '$routeParams', function($scope,$http,$routeParams){
  
  var planet_id = $routeParams.planet_id;
  uri = '/planets/api/'+planet_id;

  $http.get(uri).success(function(data){
    $scope.returned_string = "Planet name is: "+ data.name + " with radius: " + data.radius;
  });

}]);