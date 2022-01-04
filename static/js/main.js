$(document).ready(function () {
    $(function () {
        $.get("/login", function (data) {
            if (data === 'False') {
                return;
            } else {
                $('.usernameshow').text(data);
            }
        });
    });


    layui.use(['carousel', 'form'], function () {
        var carousel = layui.carousel
            , form = layui.form;

        //常规轮播
        carousel.render({
            elem: '#test1'
            , arrow: 'always'
            , height: '380px'
            , width: '960px'
        });


    });

    $(".usernameshow").click(function () {
        if ($(".usernameshow").text() === "未登录") {
            layer.open({
                type: 2,
                title: false,
                closeBtn: 0,
                area: ['400px', '260px'],
                shadeClose: true,
                skin: 'yourclass',
                content: '/static/login_up.html',
                scrollbar: false,//屏蔽浏览器滚动条
                // content:  $('#login_up')

                success: function (layero, index) {
                    var frameId = $(layero).find("iframe").attr('id');

                    $($(window.frames[frameId].document).find("#login")).click(function () {

                        var u = $(window.frames[frameId].document).find("#username").val();
                        var p = $(window.frames[frameId].document).find("#password").val();
                        var param = {"username": u, "password": p};
                        $.post("/login", param, function (result) {
                            console.log(result)
                            if (result === "success") {
                                layer.closeAll();
                                $('.usernameshow').text(u);

                                url1 = window.location.href;
                                if (url1.indexOf('getShopCart') != -1) {
                                    $.ajax({
                                        url: '/getShopCart',
                                        type: 'post',
                                        dataType: 'json',
                                        success: function (data) {

                                            var htmlContent = ''
                                            for (i = 0; i < data.length - 1; i++) {
                                                var item = '<div class="list_frame"><input type="checkbox" name="select" class="checkbox" id="checkbox"><img src="/';
                                                item += data[i]['goods_pic_path'] + '" class="img" id="img"><div class="item_text"><div class="item_text_name" id="name">';
                                                item += data[i]['goods_name'] + '</div></div><div class="price_buss">¥';
                                                item += data[i]['price'] + '</div><input type="button" name="purchase" id="';
                                                item += data[i]['id'] + '" value="购买" class="btn_buss"/></div>'

                                                htmlContent += item;
                                            }

                                            console.log(data[data.length - 1]['price_sum']);

                                            $('.price_all').text(data[data.length - 1]['price_sum']);

                                            $(".mid").html(htmlContent);
                                        }
                                    });
                                }
                            } else {
                                alert("用户名或者密码错误!");
                            }
                        });


                        console.log(u + " " + p);
                        // setTimeout((function(){
                        //  layer.close();
                        // }),1000);

                    });
                }
            });
        } else {
            window.location.href = "/myhome";
        }

    });
    $('.search_Bt').click(function () {
        console.log("测试点2");
    });


    // function getChildrenData(data){
    // 	console.log('从子页面传递回到数据：');
    // 	console.log(data);
    // });

    function post() {
        $.post("http://127.0.0.1:8000/login", param, function (result) {
            console.log(result)
            if (result === "success") {
                setTimeout((function () {
                    layer.closeAll();
                    alert("登陆成功!");
                    $('.usernameshow').text(u);
                }), 1000);
            } else {
                alert("用户名或者密码错误!");
            }
        });
    }

});
