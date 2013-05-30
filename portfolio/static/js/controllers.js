function ProjectList($scope, Project) {
  $scope.projects = Project.query();
  $scope.orderProp = 'name';
}

function BlogList($scope, Post) {
  $scope.posts = Post.query();
  $scope.orderProp = '-posted';
}

function ProjectDetail($scope, $routeParams, Project) {
  $scope.project = Project.get({projectSlug:$routeParams.projectSlug});
}

function BlogPost($scope, $routeParams, Post) {
  $scope.post = Post.get({postSlug:$routeParams.postSlug}, function(post) {
    $scope.prevPost = ($scope.post.previous != false) ? true : false;
    $scope.nextPost = ($scope.post.next != false) ? true : false;
  });
}

function SideBarCtrl($scope) {
  $scope.projectTitle = "Bryan Turek";
  var panelOpened = false;
  $scope.togglePanel = function() {
    if(!panelOpened) {
      $(".sidePanel").addClass("openPanel");
      panelOpened = true;
    } else {
      $(".sidePanel").removeClass("openPanel");
      panelOpened = false;
    }
  }
}