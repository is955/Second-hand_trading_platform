$(document).ready(function(){
	
	var goods_id = getUrlParam('goods_id');
	$("#buya").attr('href','/buy?goods_id='+goods_id);
	
	layui.use(['carousel', 'form'], function(){
	  var carousel = layui.carousel
	  ,form = layui.form;
	
	  //常规轮播
	  carousel.render({
	    elem: '#goods_img'
	    ,arrow: 'always'
		,height: '350px'
		,width: '350px'
	  });
	});
	
	// //加入购物车
	// $("#join").click(function(){
	// 	var goods_id = getUrlParam('goods_id');

	// 	var param = {
	// 	  "goods_id":goods_id,
	// 	};

	// 	$.post("/scoreAdd",param,function(result){
	// 	  if(result==="success"){
			  
	// 	  }else{
	// 		  alert(result);
	// 	  }
	// 	});
	// });
	
	// //去购买
	// $("#buy").click(function(){
	// 	console.log("123");
	// 	var goods_id = getUrlParam('goods_id');
	// 	console.log(goods_id);
	
		
	// 	$.get("/buy?goods_id="+goods_id,function(data){

 //        });
	
	// });
	
	function getUrlParam(name) {
	
	     var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)"); //构造一个含有目标参数的正则表达式对象
	
	     var r = window.location.search.substr(1).match(reg);  //匹配目标参数
	
	     if (r != null) return unescape(r[2]); return null; //返回参数值
	
	 }
});