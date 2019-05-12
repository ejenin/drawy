$(document).ready(function() {
			$(".coolButton").click(function() {
				$(".mainMenu").fadeOut(function() {
					$(".playground").fadeIn(start);
				});
			});

			generateTask();

			$("#clr").click(function() {
				clearCanvas();
			});
			//todo: ubrat
			//start();
		});

		function generateTask() {
			pickedWord = getRandomWord();
			console.log(pickedWord);
			$(".task").html("Нарисуйте: " + pickedWord);
			$("#guess").text("");
		}

		function getRandomWord() {
			const word = $.ajax({
				url: "getRandom",
				type: "GET",
				async: false
			}).responseText;
			return word;
		}

		function sendCanvasToBackend() {
			var canvasData = document.getElementById("canv").toDataURL();
			$.ajax({
				type: "POST",
				url: "guessImage",
				data: canvasData,
				success: function(data) {
					console.log(data);
					checkWinning(data);
				}
			});
		}

		function checkWinning(serverResult) {
		    var win = false;
		    var guesses = "";

			if (serverResult && serverResult.length > 0) {
				for (var i = 0; i < serverResult.length; i++) {
					guesses += serverResult[i] + "? ";
					if (serverResult[i] == pickedWord) {
						generateTask();
						clearCanvas();
						win = true;
						time = 40;
					}
				}
			} else {
			    guesses = "..?";
			}

			if (!win) {
				$("#guess").text($("#guess").text() + guesses);
		    }
		}

		function clearCanvas() {
			var canvas = document.getElementById("canv");
			canvas.width = $(".cnvs").outerWidth();
			canvas.height = $(".cnvs").outerHeight();
			ctx = canvas.getContext("2d");
			ctx.fillStyle = "#FFFFFF";
    		ctx.fillRect(0,0,canvas.width,canvas.height);
    		ctx.fillStyle = "#000000";
    		ctx.lineJoin = "round";
			ctx.lineWidth = 10;
			ctx.lineJoin = "round";
		}

		var pickedWord = "";

		var time = 40;
		var timer = null;
		var checkerTimer = null;
		var drawing = false;
		var ctx;
		var lastX, lastY;

		function start() {
			var canvas = document.getElementById("canv");
			<!-- console.log($(".cnvs").outerWidth()); -->
			canvas.width = $(".cnvs").outerWidth();
			canvas.height = $(".cnvs").outerHeight();
			ctx = canvas.getContext("2d");

			ctx.fillStyle = "#FFFFFF";
    		ctx.fillRect(0,0,canvas.width,canvas.height);

			ctx.fillStyle = "#000000";
			ctx.lineJoin = "round";
			<!-- ctx.strokeStyle = $('#selColor').val(); -->
			ctx.lineWidth = 10;
			ctx.lineJoin = "round";
			<!-- ctx.fillRect(0, 0, 150, 75); -->

			canvas.onmousedown = function (e) {
				<!-- console.log(e); -->
				<!-- var dy = e.screenY - e.clientY; -->
				<!-- ctx.fillRect(e.clientX, e.clientY - dy - 20, 5, 5); -->
				var dy = e.screenY - e.clientY;
				Draw(e.clientX, e.clientY - dy - 25, drawing);
				drawing = true;
			}

			canvas.onmouseup = function (e) {
				drawing = false;
			}

			canvas.onmousemove = function (e) {
				if (drawing == true) {
					<!-- var dy = e.screenY - e.clientY; -->
					<!-- ctx.fillRect(e.clientX, e.clientY - dy - 20, 5, 5); -->
					var dy = e.screenY - e.clientY;
					Draw(e.clientX, e.clientY - dy - 25, drawing);
				}
			}

			timer = setInterval(handleTime, 1000);
			checkerTimer = setInterval(sendCanvasToBackend, 3000);
		}

		function Draw(x, y, isDown) {
			if (isDown) {
				ctx.beginPath();
				ctx.moveTo(lastX, lastY);
				ctx.lineTo(x, y);
				ctx.closePath();
				ctx.stroke();
			}
			lastX = x; lastY = y;
		}

		function handleTime() {
            time--;
			$(".timer").text("Осталось времени: " + time + " сек");

			if (time == 0) {
				time = 40;
				generateTask();
				clearCanvas();
			}
		}