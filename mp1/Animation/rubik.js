// element: a jQuery object containing the DOM element to use
// dimensions: the number of cubes per row/column (default 3)
// background: the scene background colour
function Rubik(element, dimensions, background) {
  
  color_r = 0xFF0000;
  color_b = 0x0000FF;
  color_g = 0x00FF00;
  color_o = 0xFF9900;
  color_y = 0xFFFF00;
  color_p = 0x9900FF;
  color_a = 0x969696;

  face = []
  face[0]= color_r
  face[1]= color_r
  face[2]= color_b
  face[3]= color_b
  face[4]= color_g
  face[5]= color_g
  face[6]= color_r
  face[7]= color_r
  face[8]= color_b
  face[9]= color_b
  face[10] = color_g
  face[11] = color_g
  face[12] = color_o
  face[13] = color_o
  face[14] = color_o
  face[15] = color_o
  face[16] = color_y
  face[17] = color_y
  face[18] = color_y
  face[19] = color_y
  face[20] = color_p
  face[21] = color_p
  face[22] = color_p
  face[23] = color_p

  dimensions = dimensions || 2;
  background = background || 0x303030;

  var width = element.innerWidth(),
      height = element.innerHeight();

  var debug = false;

  /*** three.js boilerplate ***/
  var scene = new THREE.Scene(),
      camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000),
      renderer = new THREE.WebGLRenderer({ antialias: true });

  renderer.setClearColor(background, 1.0);
  renderer.setSize(width, height);
  renderer.shadowMapEnabled = true;
  element.append(renderer.domElement);

  camera.position = new THREE.Vector3(-20, 20, 30);
  camera.lookAt(scene.position);
  THREE.Object3D._threexDomEvent.camera(camera);

  /*** Lights ***/
  scene.add(new THREE.AmbientLight(0xffffff));
  //TODO: add a spotlight that takes the orbitcontrols into account to stay "static"

  /*** Camera controls ***/
  var orbitControl = new THREE.OrbitControls(camera, renderer.domElement);

  function enableCameraControl() {
    orbitControl.noRotate = false;
  }

  function disableCameraControl() {
    orbitControl.noRotate = true;
  }

  /*** Debug aids ***/  
  if(debug) {
    scene.add(new THREE.AxisHelper( 20 ));
  }

  /*** Click handling ***/

  //Do the given coordinates intersect with any cubes?
  var SCREEN_HEIGHT = window.innerHeight;
  var SCREEN_WIDTH = window.innerWidth;

  var raycaster = new THREE.Raycaster(),
      projector = new THREE.Projector();

  //Return the axis which has the greatest maginitude for the vector v
  function principalComponent(v) {
    var maxAxis = 'x',
        max = Math.abs(v.x);
    if(Math.abs(v.y) > max) {
      maxAxis = 'y';
      max = Math.abs(v.y);
    }
    if(Math.abs(v.z) > max) {
      maxAxis = 'z';
      max = Math.abs(v.z);
    }
    return maxAxis;
  }

  //For each mouse down, track the position of the cube that
  // we clicked (clickVector) and the face object that we clicked on 
  // (clickFace)
  var clickVector, clickFace;

  //Keep track of the last cube that the user's drag exited, so we can make
  // valid movements that end outside of the Rubik's cube
  var lastCube;

  //Matrix of the axis that we should rotate for 
  // each face-drag action
  //    F a c e
  // D    X Y Z
  // r  X - Z Y
  // a  Y Z - X
  // g  Z Y X -
  var transitions = {
    'x': {'y': 'z', 'z': 'y'},
    'y': {'x': 'z', 'z': 'x'},
    'z': {'x': 'y', 'y': 'x'}
  }


  /*** Build 27 cubes ***/
  //TODO: colour the insides of all of the faces black
  // (probably colour all faces black to begin with, then "whitelist" exterior faces)
  var colours = [0x00FF00, 0xFF0000, 0x0000FF, 0xFFFF00, 0xFF9900, 0x9900FF],
      faceMaterials = colours.map(function(c) {
        return new THREE.MeshLambertMaterial({ color: c , ambient: c });
      }),
      cubeMaterials = new THREE.MeshFaceMaterial(faceMaterials);

  var cubeSize =3,
      spacing = 0.5;

  var increment = cubeSize + spacing,
      maxExtent = (cubeSize * dimensions + spacing * (dimensions - 1)) / 2, 
      allCubes = [];

  function newCube(x, y, z, cubeColor) {
    var cubeGeometry = new THREE.CubeGeometry(cubeSize, cubeSize, cubeSize);
    var cube = new THREE.Mesh(cubeGeometry, cubeColor);
    cube.castShadow = true;

    cube.position = new THREE.Vector3(x, y, z);
    cube.rubikPosition = cube.position.clone();

    scene.add(cube);
    allCubes.push(cube);
  }

  function newRubik(face) {
    while (allCubes.length > 0) {
        scene.remove(allCubes.pop())  
      }

      //             right      left      top    bottom    front      back
      var colours = [color_a, face[0], color_a, face[18], color_a, face[20]],
      faceMaterials = colours.map(function(c) {
        return new THREE.MeshLambertMaterial({ color: c , ambient: c });
      }),
      cubeMaterials = new THREE.MeshFaceMaterial(faceMaterials);
      newCube(-1.75, -1.75, -1.75, cubeMaterials);
      
      //             right      left      top    bottom    front      back
      var colours = [color_a, face[6], color_a, face[16], face[14], color_a],
      faceMaterials = colours.map(function(c) {
        return new THREE.MeshLambertMaterial({ color: c , ambient: c });
      }),
      cubeMaterials = new THREE.MeshFaceMaterial(faceMaterials);
      newCube(-1.75, -1.75,  1.75, cubeMaterials);

      //             right      left      top    bottom    front      back
      var colours = [color_a, face[1], face[2], color_a, color_a, face[22]],
      faceMaterials = colours.map(function(c) {
        return new THREE.MeshLambertMaterial({ color: c , ambient: c });
      }),
      cubeMaterials = new THREE.MeshFaceMaterial(faceMaterials);
      newCube(-1.75,  1.75, -1.75, cubeMaterials);

      //             right      left      top    bottom    front      back
      var colours = [color_a, face[7], face[8], color_a, face[12], color_a],
      faceMaterials = colours.map(function(c) {
        return new THREE.MeshLambertMaterial({ color: c , ambient: c });
      }),
      cubeMaterials = new THREE.MeshFaceMaterial(faceMaterials);
      newCube(-1.75,  1.75,  1.75, cubeMaterials);

      //             right      left      top    bottom    front      back
      var colours = [face[5], color_a, color_a, face[19], color_a, face[21]],
      faceMaterials = colours.map(function(c) {
        return new THREE.MeshLambertMaterial({ color: c , ambient: c });
      }),
      cubeMaterials = new THREE.MeshFaceMaterial(faceMaterials);
      newCube( 1.75, -1.75, -1.75, cubeMaterials);

      //             right      left      top    bottom    front      back
      var colours = [face[11], color_a, color_a, face[17], face[15], color_a],
      faceMaterials = colours.map(function(c) {
        return new THREE.MeshLambertMaterial({ color: c , ambient: c });
      }),
      cubeMaterials = new THREE.MeshFaceMaterial(faceMaterials);
      newCube( 1.75, -1.75,  1.75, cubeMaterials);

      //             right      left      top    bottom    front      back
      var colours = [face[4], color_a, face[3], color_a, color_a, face[23]],
      faceMaterials = colours.map(function(c) {
        return new THREE.MeshLambertMaterial({ color: c , ambient: c });
      }),
      cubeMaterials = new THREE.MeshFaceMaterial(faceMaterials);
      newCube( 1.75,  1.75, -1.75, cubeMaterials);

      //             right      left      top    bottom    front      back
      var colours = [face[10], color_a, face[9], color_a, face[13], color_a],
      faceMaterials = colours.map(function(c) {
        return new THREE.MeshLambertMaterial({ color: c , ambient: c });
      }),
      cubeMaterials = new THREE.MeshFaceMaterial(faceMaterials);
      newCube( 1.75,  1.75,  1.75, cubeMaterials);

      /*** Manage transition states ***/

      //TODO: encapsulate each transition into a "Move" object, and keep a stack of moves
      // - that will allow us to easily generalise to other states like a "hello" state which
      // could animate the cube, or a "complete" state which could do an animation to celebrate
      // solving.
      var moveEvents = $({});

      //Maintain a queue of moves so we can perform compound actions like shuffle and solve
      var moveQueue = [],
          completedMoveStack = [],
          currentMove;

      //Are we in the middle of a transition?
      var isMoving = false,
          moveAxis, moveN, moveDirection,
          rotationSpeed = 0.2;

      render();
  }

  var positionOffset = 0.5;
  for(var i = 0; i < dimensions; i ++) {
    for(var j = 0; j < dimensions; j ++) {
      for(var k = 0; k < dimensions; k ++) {

        var x = (i - positionOffset) * increment,
            y = (j - positionOffset) * increment,
            z = (k - positionOffset) * increment;

        newCube(x, y, z, cubeMaterials);
      }
    }
  }

  /*** Manage transition states ***/

  //TODO: encapsulate each transition into a "Move" object, and keep a stack of moves
  // - that will allow us to easily generalise to other states like a "hello" state which
  // could animate the cube, or a "complete" state which could do an animation to celebrate
  // solving.
  var moveEvents = $({});

  //Maintain a queue of moves so we can perform compound actions like shuffle and solve
  var moveQueue = [],
      completedMoveStack = [],
      currentMove;

  //Are we in the middle of a transition?
  var isMoving = false,
      moveAxis, moveN, moveDirection,
      rotationSpeed = 0.2;

  //http://stackoverflow.com/questions/20089098/three-js-adding-and-removing-children-of-rotated-objects
  var pivot = new THREE.Object3D(),
      activeGroup = [];

  function nearlyEqual(a, b, d) {
    d = d || 0.001;
    return Math.abs(a - b) <= d;
  }

  //Select the plane of cubes that aligns with clickVector
  // on the given axis
  function setActiveGroup(axis) {
    if(clickVector) {
      activeGroup = [];

      allCubes.forEach(function(cube) {
        if(nearlyEqual(cube.rubikPosition[axis], clickVector[axis])) { 
          activeGroup.push(cube);
        }
      });
    } else {
      console.log("Nothing to move!");
    }
  }

  var pushMove = function(cube, clickVector, axis, direction) {
    moveQueue.push({ cube: cube, vector: clickVector, axis: axis, direction: direction });
  }

  var startNextMove = function() {
    var nextMove = moveQueue.pop();

    if(nextMove) {
      clickVector = nextMove.vector;
      
      var direction = nextMove.direction || 1,
          axis = nextMove.axis;

      if(clickVector) {

        if(!isMoving) {
          isMoving = true;
          moveAxis = axis;
          moveDirection = direction;

          setActiveGroup(axis);

          pivot.rotation.set(0,0,0);
          pivot.updateMatrixWorld();
          scene.add(pivot);

          activeGroup.forEach(function(e) {
            console.log(e)
            THREE.SceneUtils.attach(e, scene, pivot);
          });

          currentMove = nextMove;
        } else {
          console.log("Already moving!");
        }
      } else {
        console.log("Nothing to move!");
      }
    } else {
      moveEvents.trigger('deplete');
    }
  }

  function doMove() {
    //Move a quarter turn then stop
    if(pivot.rotation[moveAxis] >= Math.PI / 2) {
      //Compensate for overshoot. TODO: use a tweening library
      pivot.rotation[moveAxis] = Math.PI / 2;
      moveComplete();
    } else if(pivot.rotation[moveAxis] <= Math.PI / -2) {
      pivot.rotation[moveAxis] = Math.PI / -2;
      moveComplete()
    } else {
      pivot.rotation[moveAxis] += (moveDirection * rotationSpeed);
    }
  }

  var moveComplete = function() {
    isMoving = false;
    moveAxis, moveN, moveDirection = undefined;
    clickVector = undefined;

    pivot.updateMatrixWorld();
    scene.remove(pivot);
    activeGroup.forEach(function(cube) {
      cube.updateMatrixWorld();

      cube.rubikPosition = cube.position.clone();
      cube.rubikPosition.applyMatrix4(pivot.matrixWorld);

      THREE.SceneUtils.detach(cube, pivot, scene);
    });

    completedMoveStack.push(currentMove);

    moveEvents.trigger('complete');

    //Are there any more queued moves?
    startNextMove();
  }


  function render() {

    //States
    //TODO: generalise to something like "activeState.tick()" - see comments 
    // on encapsulation above
    if(isMoving) {
      doMove();
    } 

    renderer.render(scene, camera);
    requestAnimationFrame(render);
  }

  /*** Util ***/
  function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  }

  //Go!
  render();

  //Public API
  return {
    input11: function() {
      face = [];
      face[0]= color_y;
      face[1]= color_o;
      face[2]= color_r;
      face[3]= color_r;

      face[4]= color_p;
      face[5]= color_b;
      face[6]= color_y;
      face[7]= color_g;
      
      face[8]= color_o;
      face[9]= color_o;
      face[10] = color_r;
      face[11] = color_b;

      face[12] = color_b;
      face[13] = color_b;
      face[14] = color_o;
      face[15] = color_g;
      
      face[16] = color_g;
      face[17] = color_p;
      face[18] = color_g;
      face[19] = color_p;
      
      face[20] = color_p;
      face[21] = color_r;
      face[22] = color_y;
      face[23] = color_y;
      newRubik(face);

      setTimeout(function(){
        pushMove(allCubes[3], allCubes[3].position.clone(), 'y', 1);
        startNextMove();
        setTimeout(function(){
          pushMove(allCubes[5], allCubes[5].position.clone(), 'x', 1);
          startNextMove();
          setTimeout(function(){
            pushMove(allCubes[0], allCubes[0].position.clone(), 'z', 1);
            startNextMove();
            setTimeout(function(){
              pushMove(allCubes[1], allCubes[1].position.clone(), 'z', 1);
              startNextMove();
            },1000);
          },1000);
        },1000);
      },3000);
    },

    input12: function() {
      face = [];
      face[0]= color_o;
      face[1]= color_y;
      face[2]= color_g;
      face[3]= color_b;

      face[4]= color_p;
      face[5]= color_g;
      face[6]= color_g;
      face[7]= color_r;
      
      face[8]= color_o;
      face[9]= color_r;
      face[10] = color_y;
      face[11] = color_b;

      face[12] = color_y;
      face[13] = color_p;
      face[14] = color_o;
      face[15] = color_g;
      
      face[16] = color_b;
      face[17] = color_p;
      face[18] = color_r;
      face[19] = color_y;
      
      face[20] = color_b;
      face[21] = color_p;
      face[22] = color_o;
      face[23] = color_r;
      newRubik(face);

      setTimeout(function(){
        pushMove(allCubes[1], allCubes[1].position.clone(), 'z', 1);
        startNextMove();
        setTimeout(function(){
          pushMove(allCubes[0], allCubes[0].position.clone(), 'x', -1);
          startNextMove();
          setTimeout(function(){
            pushMove(allCubes[0], allCubes[0].position.clone(), 'x', -1);
            startNextMove();
            setTimeout(function(){
              pushMove(allCubes[3], allCubes[3].position.clone(), 'y', 1);
              startNextMove();
              setTimeout(function(){
                pushMove(allCubes[1], allCubes[1].position.clone(), 'z', 1);
                startNextMove();
              },1000);
            },1000);
          },1000);
        },1000);
      },3000);
    },

    input13: function() {
      face = [];
      face[0]= color_o;
      face[1]= color_y;
      face[2]= color_o;
      face[3]= color_g;

      face[4]= color_o;
      face[5]= color_g;
      face[6]= color_g;
      face[7]= color_p;
      
      face[8]= color_r;
      face[9]= color_b;
      face[10] = color_r;
      face[11] = color_b;

      face[12] = color_y;
      face[13] = color_p;
      face[14] = color_o;
      face[15] = color_g;
      
      face[16] = color_b;
      face[17] = color_p;
      face[18] = color_r;
      face[19] = color_y;
      
      face[20] = color_b;
      face[21] = color_p;
      face[22] = color_r;
      face[23] = color_y;
      newRubik(face);

      setTimeout(function(){
        pushMove(allCubes[1], allCubes[1].position.clone(), 'z', 1);
        startNextMove();
        setTimeout(function(){
          pushMove(allCubes[2], allCubes[2].position.clone(), 'y', 1);
          startNextMove();
          setTimeout(function(){
            pushMove(allCubes[0], allCubes[0].position.clone(), 'x', 1);
            startNextMove();
            setTimeout(function(){
              pushMove(allCubes[5], allCubes[5].position.clone(), 'x', -1);
              startNextMove();
              setTimeout(function(){
                pushMove(allCubes[6], allCubes[6].position.clone(), 'y', 1);
                startNextMove();
                setTimeout(function(){
                  pushMove(allCubes[5], allCubes[5].position.clone(), 'x', 1);
                  startNextMove();
                },1000);
              },1000);
            },1000);
          },1000);
        },1000);
      },3000);
    },

    input21: function() {
      face = [];
      face[0]= color_y;
      face[1]= color_o;
      face[2]= color_r;
      face[3]= color_r;

      face[4]= color_p;
      face[5]= color_b;
      face[6]= color_y;
      face[7]= color_g;
      
      face[8]= color_o;
      face[9]= color_o;
      face[10] = color_r;
      face[11] = color_b;

      face[12] = color_b;
      face[13] = color_b;
      face[14] = color_o;
      face[15] = color_g;
      
      face[16] = color_g;
      face[17] = color_p;
      face[18] = color_g;
      face[19] = color_p;
      
      face[20] = color_p;
      face[21] = color_r;
      face[22] = color_y;
      face[23] = color_y;
      newRubik(face);

      setTimeout(function(){
        pushMove(allCubes[3], allCubes[3].position.clone(), 'y', 1);
        startNextMove();
        setTimeout(function(){
          pushMove(allCubes[5], allCubes[5].position.clone(), 'x', 1);
          startNextMove();
        },1000);
      },3000);
    },

    input22: function() {
      face = [];
      face[0]= color_o;
      face[1]= color_p;
      face[2]= color_g;
      face[3]= color_b;

      face[4]= color_o;
      face[5]= color_b;
      face[6]= color_b;
      face[7]= color_y;
      
      face[8]= color_o;
      face[9]= color_b;
      face[10] = color_r;
      face[11] = color_r;

      face[12] = color_g;
      face[13] = color_p;
      face[14] = color_o;
      face[15] = color_p;
      
      face[16] = color_r;
      face[17] = color_y;
      face[18] = color_y;
      face[19] = color_g;
      
      face[20] = color_r;
      face[21] = color_p;
      face[22] = color_y;
      face[23] = color_g;
      newRubik(face);

      setTimeout(function(){
        pushMove(allCubes[1], allCubes[1].position.clone(), 'z', 1);
        startNextMove();
        setTimeout(function(){
          pushMove(allCubes[2], allCubes[2].position.clone(), 'y', 1);
          startNextMove();
          setTimeout(function(){
            pushMove(allCubes[5], allCubes[5].position.clone(), 'x', -1);
            startNextMove();
            setTimeout(function(){
              pushMove(allCubes[5], allCubes[5].position.clone(), 'x', -1);
              startNextMove();
              setTimeout(function(){
                pushMove(allCubes[6], allCubes[6].position.clone(), 'y', 1);
                startNextMove();
                setTimeout(function(){
                  pushMove(allCubes[5], allCubes[5].position.clone(), 'x', 1);
                  startNextMove();
                },1000);
              },1000);
            },1000);
          },1000);
        },1000);
      },3000);
    },

    input23: function() {
      face = [];
      face[0]= color_y;
      face[1]= color_b;
      face[2]= color_o;
      face[3]= color_p;

      face[4]= color_y;
      face[5]= color_y;
      face[6]= color_r;
      face[7]= color_g;
      
      face[8]= color_y;
      face[9]= color_b;
      face[10] = color_o;
      face[11] = color_g;

      face[12] = color_o;
      face[13] = color_r;
      face[14] = color_p;
      face[15] = color_p;
      
      face[16] = color_b;
      face[17] = color_b;
      face[18] = color_g;
      face[19] = color_o;
      
      face[20] = color_p;
      face[21] = color_r;
      face[22] = color_g;
      face[23] = color_r;
      newRubik(face);

      setTimeout(function(){
        pushMove(allCubes[1], allCubes[1].position.clone(), 'z', 1);
        startNextMove();
        setTimeout(function(){
          pushMove(allCubes[5], allCubes[5].position.clone(), 'x', 1);
          startNextMove();
          setTimeout(function(){
            pushMove(allCubes[2], allCubes[2].position.clone(), 'y', -1);
            startNextMove();
            setTimeout(function(){
              pushMove(allCubes[2], allCubes[2].position.clone(), 'y', -1);
              startNextMove();
              setTimeout(function(){
                pushMove(allCubes[5], allCubes[5].position.clone(), 'x', 1);
                startNextMove();
              },1000);
            },1000);
          },1000);
        },1000);
      },3000);
    },

    input31: function() {
      face = [];
      face[0]= color_g;
      face[1]= color_o;
      face[2]= color_g;
      face[3]= color_g;

      face[4]= color_o;
      face[5]= color_p;
      face[6]= color_y;
      face[7]= color_y;
      
      face[8]= color_r;
      face[9]= color_p;
      face[10] = color_r;
      face[11] = color_b;

      face[12] = color_o;
      face[13] = color_y;
      face[14] = color_g;
      face[15] = color_r;
      
      face[16] = color_p;
      face[17] = color_o;
      face[18] = color_b;
      face[19] = color_r;
      
      face[20] = color_p;
      face[21] = color_b;
      face[22] = color_b;
      face[23] = color_y;
      newRubik(face);

      setTimeout(function(){
        pushMove(allCubes[1], allCubes[1].position.clone(), 'z', -1);
        startNextMove();
        setTimeout(function(){
          pushMove(allCubes[3], allCubes[3].position.clone(), 'x', 1);
          startNextMove();
          setTimeout(function(){
            pushMove(allCubes[2], allCubes[2].position.clone(), 'y', -1);
            startNextMove();
            setTimeout(function(){
              pushMove(allCubes[3], allCubes[3].position.clone(), 'x', -1);
              startNextMove();
              setTimeout(function(){
                pushMove(allCubes[5], allCubes[5].position.clone(), 'z', 1);
                startNextMove();
                setTimeout(function(){
                  pushMove(allCubes[5], allCubes[5].position.clone(), 'x', -1);
                  startNextMove();
                  setTimeout(function(){
                    pushMove(allCubes[5], allCubes[5].position.clone(), 'z', -1);
                    startNextMove();
                  },1000);
                },1000);
              },1000);
            },1000);
          },1000);
        },1000);
      },3000);
    }
  }
}

