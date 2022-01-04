
$(document).ready(function(){
	$(function(){
		$.get("/login",function(data){
			if(data==='False'){
				return;
			}else{
				$('.usernameshow').text(data);
				post();
			}
		});
	});
	
	function post(){
		param={
			"":""
		}
		
		$.ajax({
		    url:'/getusergoods',
		    type:'post',
		    dataType:'json',
		    success:function(data){
				var htmlContent='<colgroup><col width="150"><col width="150"><col width="200"><col></colgroup><thead><tr><th>商品ID</th><th>图片缩略图</th><th>商品名称</th><th>商品价格</th><th>下架</th><th>查看</th></tr></thead><tbody>'
				for(i=0;i<data.length;i++){
					var item='<tr><td>';
					item+=data[i]['goods_id']+'</td><td><img src="';
					item+=data[i]['goods_pic_path']+'"></td><td>';
					item+=data[i]['goods_name']+'</td><td>';
					item+=data[i]['goods_price']+'</td><th><button id="del" type="button" class="layui-btn layui-btn-sm layui-btn-danger">下架</button></th><th><a href="/detail?goods_id='+data[i]['goods_id']+'"><button type="button" class="layui-btn layui-btn-sm layui-btn-normal">去查看</button></a></th></tr>'
					
					htmlContent+=item;
				}
				htmlContent+='</tbody>';
				
				$(".u_goods").html(htmlContent);
			}
		});
	}
	
	
	//下架商品
	$(document).on('click', '#del', function () {
	  var goods_id=$(this).parents("tr").find("td").eq(0).text(); //得到ID
	  var d=$(this).parents("tr");
	
	  var param = {
	    "goods_id":goods_id,
	  };
	  
	  $.post("#",param,function(result){
	    if(result==="success"){
	        d.remove();
	        // alert("Change successful!");
	    }else{
	        alert(result);
	    }
	  });
	});
});
