var Portfolio = angular.module('portfolio', ['portfolioServices','ngSanitize']);

Portfolio.directive('projectEvent', function($location) {
  return function(scope, element, attrs) {
    element.bind('click', function(e){
      scope.$apply($location.path('/project/'+attrs.projectEvent));
    })
  }
});

Portfolio.directive('postEvent', function($location) {
  return function(scope, element, attrs) {
    element.bind('click', function(e){
      scope.$apply($location.path('/blog/'+attrs.postEvent));
    })
  }
});


Portfolio.directive('homeEvent', function($location) {
  return function(scope, element, attrs) {
    element.bind('click', function(e){
      scope.$apply($location.path('/'));
    })
  }
});

Portfolio.directive('panelEvent', function() {
  return function(scope, element, attrs) {
    scope.$watch('projectTitle', function(newValue, oldValue) {
      alert("change");
    }, true);
  }
});

Portfolio.directive('sliderEvent', function() {
  
});

Portfolio.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
      when('/', {templateUrl: '/static/views/project-list.html',   controller: ProjectList}).
      when('/project/:projectSlug', {templateUrl: '/static/views/project-detail.html', controller: ProjectDetail}).
      when('/blog', {templateUrl: '/static/views/post-list.html',   controller: BlogList}).
      when('/blog/:postSlug', {templateUrl: '/static/views/post-detail.html',   controller: BlogPost}).
      otherwise({redirectTo: '/'});
}]);