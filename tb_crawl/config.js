layui.define(function(exports) {
	var config = {
		//对应配置里的server_servlet_path
		server_servlet_path: '/passport',
		proxy_server: '/proxy/passport',
		// ajax请求的header
		getAjaxHeaders: function(requestUrl) {
			var headers = [];
			/*需要添加的基础固定的请求头请在此添加
            headers.push({
                name: 'Authorization',
                value: token
            });
            */
			return headers;
		},
		// ajax请求结束后的处理，返回false阻止代码执行
		ajaxSuccessBefore: function(res, requestUrl) {
			if (res.code == 401) {
				layer.msg('身份认证过期或未登录', {
					icon: 2,
					time: 1500
				}, function() {
					location.reload();
				});
				return false;
			} else if (res.code == 400) {
				layer.msg('请求错误', {
					icon: 2
				});
			} else if (res.code == 403) {
				layer.msg('没有访问权限', {
					icon: 2
				});
			} else if (res.code == 404) {
				layer.msg('404访问不存在', {
					icon: 2
				});
			}
			return true;
		}
	};

	exports('config', config);
});