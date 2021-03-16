
$(function() {
	// 判断标题
	var host = window.location.host;
	if (host.indexOf('cg.') >= 0 || host.indexOf('cr.') >= 0) {
		//武清生产
		$('#isTestLogo').text('国铁采购平台')
	} else {
		$('#isTestLogo').text('国铁采购平台(测试)')
	}
	//登录方式切换
	$(".login-way").off("click").on("click", function() {
		var index = $(this).index();
		$(this).addClass("on").siblings().removeClass("on");
		$(".form").eq(index).show().siblings('.form').hide();
		$(".form").eq(index).find('.itxt:first').focus();
		//为当前登录方式 登陆按钮添加ID
		$('.enterBtn').children('a').removeAttr('id', 'loginEnter');
		//移除其他登陆方式 登陆按钮ID
		$('.enterBtn').children('a').attr('id', 'loginEnter');
		//随机码登陆方式
		if (index == 1) {
			$('.enterBtn').children('a').removeAttr('id', 'loginEnter');
			$('.form').eq(index).find('.enterBtn>a').attr('id', 'loginEnter');
			//初始化随机码
			var oldFlag = $("#rndFlag").val();
			if (isNotEmpty(oldFlag)) {
				$("#rndFlag").val(oldFlag);
			} else {
				$("#rndFlag").val(hex_md5_wz(new Date()));
			}
			randInit();
		} else if (index == 2) {
			flushKey();
		}
	});
	$('.itxt')
		.focus(function() {
		/*$(this).siblings('.clear-btn').show();*/
		$(this).siblings('.login-label').css('background-color', '#949393')
	})
		.blur(function() {
		if ($(this).val() == '') {
			$(this).siblings('.clear-btn').hide();
		}
		$(this).siblings('.login-label').css('background-color', '#b5b4b4')
	})
		.bind('input', function() {
		if ($(this).val() == '') {
			$(this).siblings('.clear-btn').hide();
		} else {
			$(this).siblings('.clear-btn').show();
		}
	});
	$(".clear-btn").click(function() {
		$(this).parent().find('.itxt').val('');
		$(this).hide();
	})
å
});

//配置都在layui里，这里引入
layui.use(['config', 'admin'], function() {
	var config = layui.config;
	var admin = layui.admin;
	//初始化随机码
	window.randInit = function randInit() {
		var requestFlag = $("#rndFlag").val();
		$.ajax({
			url: config.proxy_server + "/randInit/" + requestFlag,
			type: "POST",
			success: function(res) {
				if (res.success) {
					$("#rndFlag").val(res.data);
					$("#img1").attr("src", config.proxy_server + "/coordinate/v1/" + res.data);
					$("#img2").attr("src", config.proxy_server + "/coordinate/v2/" + res.data);
					$("#img3").attr("src", config.proxy_server + "/coordinate/v3/" + res.data);
				}
			}
		});
	}
});

/*按键Enter触发登陆事件*/
function keyLog() {
	if (event.keyCode == 13) {
		document.getElementById("loginEnter").click();
	}
}

function domainSt(msg, data, tip) {
	tip.html("");
	$.ajax({
		url: "/passport/setSt",
		type: "POST",
		dataType: "json",
		contentType: "application/json; charset=utf-8",
		data: JSON.stringify({
			"ticket": msg,
			"data": data
		}),
		success: function(result) {
			if (!result.success) {
				tip.html(result.msg);
				$("#returnUrl").val(result.data);
			} else {
				window.location.href = result.data;
			}
		},
		error: function() {
			tip.html("提示：登陆失败,请刷新界面重试或联系管理员");
		}
	});
}