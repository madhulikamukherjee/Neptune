app.controller("MoonsController", [ '$scope', '$http', '$routeParams', function($scope,$http,$routeParams){
  
  var moon_id = $routeParams.moon_id;
  uri = '/moons/api/'+ moon_id;
  $http.get(uri).success(function(data){
    $scope.returned_string = "Moon is: "+ data.name + " which was discovered by: " + data.discoverer;
  });
  
}]);