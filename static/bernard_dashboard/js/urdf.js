   function init(){

      function render_controls(urdfModel){
         $.get('/controls',{"joints" : JSON.stringify(urdfModel.joints)}, function(data, jqXHR){

         });
      }

       var ros = new ROSLIB.Ros({
         url : 'ws://localhost:9090'
       });
    var param = new ROSLIB.Param({
     ros : ros,
     name : 'robot_description'
    });

    param.get(function(param) {
     var urdfModel = new ROSLIB.UrdfModel({
       string : param
     });
      render_controls(urdfModel)

    });
 }



