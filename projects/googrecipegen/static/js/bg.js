/*
BACKGROUND
*/


(function () {
    'use strict';
    window.addEventListener('load', function () {
      var canvas = document.getElementById('canvas');

      if (!canvas || !canvas.getContext) {
        return false;
      }

      /********************
        Random Number
      ********************/

      function rand(min, max) {
        return Math.floor(Math.random() * (max - min + 1) + min);
      }

      /********************
        Var
      ********************/

      var ctx = canvas.getContext('2d');

      var root = document.querySelector(':root');
      var hue=rand(0,360);
      var sat=rand(30,50)+'%';
      var light=rand(80,90)+'%';
      console.log("this pretty palette is: hsl(", hue,sat,light,")")

      var X = canvas.width = window.innerWidth;
      var Y = canvas.height = window.innerHeight;
      var mouseX = null;
      var mouseY = null;
      var shapeNum = 40;
      var shapes = [];
      var style = {
        black: 'black',
        white: 'white',
        lineWidth: 2,
      };

      /********************
        Animation
      ********************/

      window.requestAnimationFrame =
        window.requestAnimationFrame ||
        window.mozRequestAnimationFrame ||
        window.webkitRequestAnimationFrame ||
        window.msRequestAnimationFrame ||
        function(cb) {
          setTimeout(cb, 17);
        };

      /********************
        Shape
      ********************/

      function Shape(ctx, x, y) {
        this.ctx = ctx;
        this.init(x, y);
      }

      Shape.prototype.init = function(x, y) {
        this.x = x;
        this.y = y;
        this.r = rand(500, 950);
        this.ga = Math.random() * Math.random() * Math.random() * Math.random()/5;
        this.v = {
          x: Math.random(),
          y: -1
        };
        this.l = rand(1, 15)*this.r; //lifetime param
        this.sl = this.l;
      };

      Shape.prototype.updateParams = function() {
        var ratio = this.l / this.sl;
        //this.r *= ratio;
        this.l -= 1;
        if (this.l < 0) {
          this.init(X * (Math.random() + Math.random()) / 2, rand(0, Y));
        }
      };

      Shape.prototype.updatePosition = function() {
        this.x += Math.random()*Math.random()*Math.sin(this.y)/this.r;
        this.y += 10*Math.cos(this.x)/this.r;
      };

      Shape.prototype.draw = function() {
        var ctx  = this.ctx;
        ctx.save();
        ctx.globalCompositeOperation = 'lighter';
        ctx.globalAlpha = this.ga;
        //ctx.fillStyle = 'rgb(123, 252, 100)';
        ctx.fillStyle = `hsl(${hue/1.4},${sat},40%)`;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.r/2, 0, Math.PI * 2, false);
        ctx.fill();
        ctx.restore();
        ctx.stroke;
      };

      Shape.prototype.render = function(i) {
        this.updatePosition();
        this.updateParams();
        this.draw();
      };
      var flag =0
      for (var i = 0; i < shapeNum; i++) {
        var s = new Shape(ctx, X * (Math.random() + Math.random()) / 2, rand(0, Y));
        var s2 = new Shape(ctx, X * (Math.random() + Math.random()) / 2, rand(0, Y));
        var s3 = new Shape(ctx, X / 2, Y/2)
        shapes.push(s,s2,s3);
        flag=0;
        shapeNum+=rand(-5,5)
      }

      /********************
        Render
      ********************/

      function render() {
        ctx.clearRect(0, 0, X, Y);

        for (var i = 0; i < shapes.length; i++) {
          shapes[i].render(i);
        }

        requestAnimationFrame(render);

      }

      render();

      /********************
        Event
      ********************/

      function onResize() {
        X = canvas.width = window.innerWidth;
        Y = canvas.height = window.innerHeight;
      }

      window.addEventListener('resize', function() {
        onResize();
      });

      window.addEventListener('mousemove', function(e) {
        mouseX = e.clientX;
        mouseY = e.clientY;
      }, false);

      /********************
        Palette
      ********************/
      function generatePalette(){

        root.style.setProperty('--palettehue',hue);
        root.style.setProperty('--palettesat',sat);
        root.style.setProperty('--palettelight',light);

      };
     generatePalette()
    });
  })();
