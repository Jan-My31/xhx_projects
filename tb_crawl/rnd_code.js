
        //证书
        var keyBase64;
        //证书序列号
        var keySerialNum;
        //证书软序列号
        var certificateSerialNum;
        window.onload=function(){
           initKey();
        };
        //证书初始化
        function initKey(){
            init(function(){
                //获取第一个设备序列号
                GetDeviceSNByIndex(0,function(data){
                    keySerialNum = data.retVal;
                    // $("#keySerialNum").val(keySerialNum);
                    //获取base64证书
                    SOF_ExportUserCert(keySerialNum,function (data) {
                        keyBase64 = data.retVal;
                        //获取证书软序列
                        SOF_GetCertInfo(keyBase64,2,function (data) {
                            certificateSerialNum = data.retVal;
                            //$("#certificateSerialNum").val(certificateSerialNum);
                            if(isEmpty(keySerialNum)||isEmpty(certificateSerialNum)){
                                $("#keyDiscernTip").val("未识别到证书");
                            } else {
                                $("#keyDiscernTip").val("已识别到证书，可登录");
                            }
                        });
                    });
                });
            },function(){
            });
        }
        layui.use(['config', 'layer', 'jquery', 'admin'], function () {
            var $ = layui.jquery;
            var config = layui.config;
            var admin = layui.admin;
            var layer = layui.layer;
            var explore = getExplore();
            var ldevice = "Unkonwn";
            var device = layui.device();
            if (isNotEmpty(device)) {
                ldevice = loginDevice(device);
            }

           /* /!*手机号自动获取焦点*!/
            $(document).ready(function(){
                $('#mobilePhone').focus();
            });*/
                        window.loginSubmit = function loginSubmit(loginType) {
                if (loginType === 1) {
                    mobilePhoneLogin();
                } else if (loginType === 2) {
                    keyLogin();
                } else if (loginType === 3) {
                    randomCodeLogin();
                } else {
                    layer.alert("登录非法参数，请刷新界面重试或联系管理员", {icon: 2});
                }
            };
            function mobilePhoneLogin() {
                var tip = $("#tipMobile");
                tip.html("");
                var mobilePhone = $("#mobilePhone").val();
                if (isEmpty(mobilePhone) || !checkMobilePhone(mobilePhone)) {
                    tip.html("提示：手机号不能为空或格式不对。请重新输入");
                    $("#mobilePhone").focus();
                    return;
                }
                var mobilePhoneCode = $("#mobilePhoneCode").val();
                if (isEmpty(mobilePhoneCode)) {
                    tip.html("提示：请输入手机验证吗");
                    $("#mobilePhoneCode").focus();
                    return;
                }
                var returnUrl = $("#returnUrl").val();
                var userPassword = $("#mobilePhoneUserPassword").val();
                if (isEmpty(userPassword)) {
                    tip.html("提示：密码不能为空。请重新输入");
                    $("#mobilePhoneUserPassword").focus();
                    return;
                }
                // 是否弱口令
                var isWeakPwd = isWeakPwdCheck(userPassword);
                var SHA512 = hex_md5_wz($("#mobilePhoneUserPassword").val());
                $("#mobilePhoneUserPassword").val(SHA512);
                userPassword = $("#mobilePhoneUserPassword").val()
                var d = {
                    "loginType": 1,
                    "returnUrl": returnUrl,
                    "mobilePhone": mobilePhone,
                    "userPassword": userPassword,
                    "mobilePhoneCode": mobilePhoneCode,
                    "isWeakPwd": isWeakPwd
                };
                loginPost(d, tip);
            }

            var countdown = 60;
            var interval = null;
            window.getPhoneCode = function getPhoneCode() {
                var tip = $("#tipMobile");
                tip.html("");
                var mobilePhone = $("#mobilePhone").val();
                if (isEmpty(mobilePhone) || !checkMobilePhone(mobilePhone)) {
                    tip.html("提示：手机号不能为空或格式不对。请重新输入");
                    $("#mobilePhone").focus();
                    return;
                }else {
                    var mcode = document.getElementById("mcode");
                    mcode.setAttribute("disabled", true);
                    admin.reqProxy("/phoneCode/send/"+mobilePhone, {}, function (res) {
                        if (!res.success){
                            mcode.removeAttribute("disabled");
                            tip.html(res.msg);
                        }else {
                            interval = window.setInterval(function () {
                                if (countdown == 0) {
                                    window.clearInterval(interval);
                                    mcode.removeAttribute("disabled");
                                    mcode.value = "获取验证码";
                                    countdown = 60;
                                } else {
                                    mcode.setAttribute("disabled", true);
                                    mcode.value = "重新发送(" + countdown + ")";
                                    countdown--;
                                }
                            },1000);
                        }
                    }, "POST");
                }
            };

            //刷新证书
            window.flushKey = function flushKey(){
                initKey();
            }
            function keyLogin() {
                var tip = $("#tipKey");
                tip.html("");
                var returnUrl = $("#returnUrl").val();
                var keyPassword = $("#keyPassword").val();
                //参数校验
                if (isEmpty(keyPassword)) {
                    tip.html("提示：证书密码不能为空。请重新输入");
                    $("#keyPassword").focus();
                    return;
                }
                //证书校验
                if(isEmpty(keyBase64)){
                    tip.html("提示：未检测到证书，请刷新页面或重新插入设备后尝试");
                    return;
                }
                //对设备数量校验
                GetDeviceCount(function(data){
                    if(data.retVal!=1){
                        tip.html("提示：检测到插入多个设备，请您仅插入一个设备后尝试");
                        return;
                    }
                });
                if(isEmpty(keySerialNum)){
                    tip.html("提示：未获取到证书信息，请重新插入证书尝试");
                    return;
                }
                if(isEmpty(certificateSerialNum)){
                    tip.html("提示：证书信息获取失败，请重新插入证书尝试");
                    return;
                }
                //证书密码校验
                SOF_Login(keySerialNum,keyPassword,function (data) {
                    if(!data.retVal){
                        tip.html("提示：证书密码错误，请重新输入");
                        return;
                    }else{
                        admin.reqProxy("/getLoginCode",
                            {
                                'keySerialNum': keySerialNum,
                                'certificateSerialNum':certificateSerialNum,
                                'keyEncoded': keyBase64
                            },
                            function (res) {
                            if (res.success) {
                                var code = res.data;
                                var encryption = hex_md5_wz(code);
                                SOF_SignMessage(0,keySerialNum,code,function (data) {
                                    /*发送请求*/
                                    var d = {
                                        "loginType": 2,
                                        "returnUrl":returnUrl,
                                        'keyEncoded': keyBase64,
                                        "keySerialNum": keySerialNum,
                                        "certificateSerialNum": certificateSerialNum,
                                        "keyValue": data.retVal,
                                        "encryption": encryption,
                                        "loginMedia": explore,
                                        "loginDevice": ldevice
                                    };
                                    loginPost(d, tip);
                                });
                            } else {
                                tip.html(res.msg);
                            }
                        }, "GET");

                    }
                });
            }

            function randomCodeLogin() {
                var tip = $("#tipRandomCode");
                tip.html("");
                var returnUrl = $("#returnUrl").val();
                var codeUserAccount = $("#codeUserAccount").val();
                if (isEmpty(codeUserAccount) || !checkUserAccount(codeUserAccount)) {
                    //tip.html("提示：用户名不能为空或格式不对。请重新输入");
                    tip.html("提示：用户名、随机码或密码错误，请确认用户名、随机码和密码再次登录");
                    $("#codeUserAccount").focus();
                    return;
                }
                var codeUserPassword = $("#codeUserPassword").val();
                if (isEmpty(codeUserPassword)) {
                    tip.html("提示：密码不能为空。请重新输入");
                    $("#codeUserPassword").focus();
                    return;
                }
                var rndCode1 = $("#rndCode1").val();
                var rndCode2 = $("#rndCode2").val();
                var rndCode3 = $("#rndCode3").val();
                if (isEmpty(rndCode1)) {
                    tip.html("提示：请输入随机码");
                    $("#rndCode1").focus();
                    return;
                }
                if (isEmpty(rndCode2)) {
                    tip.html("提示：请输入随机码");
                    $("#rndCode2").focus();
                    return;
                }
                if (isEmpty(rndCode3)) {
                    tip.html("提示：请输入随机码");
                    $("#rndCode3").focus();
                    return;
                }
                var requestFlag = $("#rndFlag").val();
                if (isEmpty(requestFlag)) {
                    tip.html("提示：登录失败，参数异常！");
                    return;
                }
                // 是否弱口令
                var isWeakPwd = isWeakPwdCheck(codeUserPassword);
                var rndCode = hex_md5_wz(requestFlag + rndCode1 + rndCode2 + rndCode3);
                var SHA512 = hex_md5_wz($("#codeUserPassword").val());
                $("#codeUserPassword").val(SHA512);
                codeUserPassword = $("#codeUserPassword").val();
                var d = {
                    "loginType": 3,
                    "returnUrl":returnUrl,
                    "requestFlag": requestFlag,
                    "userAccount": codeUserAccount,
                    "userPassword": codeUserPassword,
                    "rndCode": rndCode,
                    "loginMedia": explore,
                    "loginDevice": ldevice,
                    "isWeakPwd": isWeakPwd
                };
                loginPost(d, tip);
            }

            window.flushRnd = function flushRnd() {
                //清空填写的验证码
                $("#rndCode1").val("");
                $("#rndCode2").val("");
                $("#rndCode3").val("");
                randInit();
            };

            function loginPost(d, tip) {
                layer.load(2);
                $.ajax({
                    url: config.proxy_server + "/submit",
                    type: "POST",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify(d),
                    success: function (result) {
                        layer.closeAll("loading");
                        if (!result.success) {
                            tip.html(result.msg);
                        } else {
                            domainSt(result.msg, result.data, tip);
                        }
                    },
                    error: function () {
                        layer.closeAll("loading");
                        tip.html("提示：登陆失败,请刷新界面重试或联系管理员");
                    }
                });
            }
            // 弱口令校验
            function isWeakPwdCheck(pass){
                if(!checkPassword(pass) || pass.length<8){
                   return "1";
                }else {
                   return "0";
                }
            }

            /*跳转证书申请*/
            window.caApply = function caApply() {
                layer.load(2);
                window.location.href = "https://ca.95306.cn/";
            };

        });
