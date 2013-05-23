angular.module('portfolioServices', ['ngResource']).
    factory('Project', function($resource){
      return $resource('/project/:projectSlug', {}, {
        query: {method:'GET', params:{projectSlug:''}, isArray:true}
      });
    }).
    factory('Post', function($resource){
      return $resource('/post/:postSlug', {}, {
        query: {method:'GET', params:{postSlug:''}, isArray:true}
      });
    });