$(document).ready(function() {
	$('.chat_icon_sec').hide();

	$('.chat_icon_one').click(function() {
		$('.chat_box').addClass('active');
	});

	$('.chat_icon_one').click(() => {
		$('.chat_icon').removeAttr('style').hide()
	})

	$('.chat_icon_one').click(() => {
		$('.chat_icon_sec').show()
	})

	$('.chat_icon_two').click(function() {
		$('.chat_box').removeClass('active');
	});

	$('.chat_icon_two').click(() => {
		$('.chat_icon_sec').removeAttr('style').hide()
	})

	$('.chat_icon_two').click(() => {
		$('.chat_icon_one').show()
	})

	$('.my-conv-form-wrapper').convform({selectInputStyle: 'disable'})
});
