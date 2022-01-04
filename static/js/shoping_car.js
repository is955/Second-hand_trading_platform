
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
		// $.post("/getShopCart",param,function(result){
		// 	console.log(result)
		// });
		
		$.ajax({
		    url:'/getShopCart',
		    type:'post',
		    dataType:'json',
		    success:function(data){
				
				var htmlContent=''
				for(i=0;i<data.length-1;i++){
					var item='<div class="list_frame"><input type="checkbox" name="select" class="checkbox" id="checkbox"><img src="/';
					item+=data[i]['goods_pic_path']+'" class="img" id="img"><div class="item_text"><div class="item_text_name" id="name">';
					item+=data[i]['goods_name']+'</div></div><div class="price_buss">¥';
					item+=data[i]['price']+'</div><input type="button" name="purchase" id="';
					item+=data[i]['id']+'" value="购买" class="btn_buss"/></div>'
					
					htmlContent+=item;
				}
				
				console.log(data[data.length-1]['price_sum']);
				
				$('.price_all').text(data[data.length-1]['price_sum']);
				
				$(".mid").html(htmlContent);
			}
		});
	}
});
