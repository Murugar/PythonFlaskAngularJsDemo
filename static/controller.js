'use strict';

angular.module('demoapp')
.controller('RestAPICtrl',  ['$scope', '$http', function($scope, $http) {

    $scope.message = null;
    $scope.name = 'test'

    $scope.greet = function(){
        $http
        .get('/rest/greet/' + $scope.name) // invoke backend API
        .then(function(response) {
            $scope.message = response.data['message'];
        });
    }

}]);
