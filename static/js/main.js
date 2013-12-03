// 全局配置
require.config({
    baseUrl: '/static/js',
    paths: {
        jquery: 'lib/jquery',
        bootstrap: 'lib/bootstrap',
        common: 'app/common',
        register: 'app/register',
        login: 'app/login',
        validator: 'app/validator',
    }
});

require(['jquery', 'register', 'login', 'comment', 'bootstrap'],
function($, register, login, comment, common) {
    // 禁用cache
    $.ajaxSetup({
        cache : false
    });

    // $(document).ready(function() {...})
	$(function() {
		register.init();
		login.init();
		common.init();
	});
});
