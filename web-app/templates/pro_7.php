<?php
?>
<html>
	<head>
		<title>LEGENDÄRE MOTOREN</title>
		
		<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
		<style type="text/css">
			.sl{
				background-color: rgb(51, 66, 82);
			}
			body{
				background-color:#E9E6E6;
			}
			#carnames{
				font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
			
			}
			
			body,img{
			padding:0;
			margin:0;
			}
			p.logo
			{
			position:relative;
			top:10px;
			left:40px;
			font-family: "Brush Script MT", cursive;
			font-size:70px;
			font-weight:900;
			color:#555454
			
			}
			span.moto
			{
			font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
			font-size:18px;
			font-weight:900;
			}
			

			div.toolbar
			{
				width:100%;
				height:50px;
				background-color:rgb(51, 66, 82);
				position:absolute;
				top:90px;
			}
			span.login,span.brand,span.forsale,span.home
			{	position:relative;
				top:10px;
				left:50px;
				text-decoration:none;
				color:white;
				font-size:20px;
				font-family:Cambria, Cochin, Georgia, Times, Times New Roman, serif;
				
			}
			span.login:hover,span.brand:hover,span.forsale:hover,span.home:hover
			{
				-webkit-stroke-width: 5.3px;
      			-webkit-stroke-color: #FFFFFF;
      			-webkit-fill-color: #FFFFFF;
      			text-shadow: 1px 0px 20px yellow;
			}
			img.demo:hover{
				opacity: 0.3;
				box-shadow:#3B5998;
			}
			
			table.demo
			{
				align:"center";
				width:100%;
			}
			
			
.fa {
			  padding: 15px;
			  font-size: 30px;
			  width: 30px;
			  text-align: center;
			  text-decoration: none;
			  margin: 5px 2px;
			  border-radius: 45%;
			}

			.fa:hover {
				opacity: 0.7;
			}

			.fa-facebook {
			  background: #3B5998;
			  color: white;
			}

			.fa-twitter {
			  background: #55ACEE;
			  color: white;
			}

			.fa-google {
			  background: #dd4b39;
			  color: white;
			}
			.fa-youtube {
			  background: #bb0000;
			  color: white;
			}

			.fa-instagram {
			  background: #125688;
			  color: white;
			}
.button {
    background-color:#079C1B	;/* Green  rgb(25, 25, 112)*/
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
}
.dropbtn {
 
    color:white; 
	background-color:rgb(51, 66, 82);
    
    font-size: 8px;
    border: none;
    cursor: pointer;
}

.dropdown {
    position: relative;
    
}

.dropdown-content {
    display: none;
    position: absolute;
	background-color:rgb(51, 66, 82);
   /*background-color: #f9f9f9;*/
    min-width: 160px;
    
   
}

.dropdown-content a {
    color: white;
    padding: 10px 12px;
    text-decoration: none;
    display: block;
}

.dropdown-content a:hover {background-color: #f1f1f1;
color:black;
}

.dropdown:hover .dropdown-content {
    display: block;
	
}


			
		</style>
		
			<script type="text/javascript">
				var car_name=new Array(12);
						for(var i=1;i<=12;i++)
						{
							car_name[i-1]="cars_"+i+".jpg";
						}
					
					var j=0;
					function slideshow()
					{
						var s=document.querySelector(".slide");
						s.setAttribute("src",car_name[j]);
						j++;
						if(j>10)
							j=0;
					
					}

					
			</script>
	</head>
	
	<body>
		<div >
			<div class="logo">
				 <p class="logo">Legendäre  Moteren 
				<span class="moto">The Roads Will Never Be The Same.</span>
				</p>
			</div>
			
				
			
			<div class="toolbar">
			<table align="center" width="80%" class="toolbar_table">
				<tr > 
				<td> <p> <a href="pro_7.php" style="text-decoration:none;"> <span class="home"> Home</span> </a> </p> </td>
				<td> <p> <a href="login.html" style="text-decoration:none;"> <span class="login"> Login</span> </a> </p> </td>
				<td>  <div class="dropdown">
					<button class="dropbtn"><span class="brand"> Brands</span></button>
					<div class="dropdown-content">
					  <a href="bmw.php">BMW</a>
					  <a href="audi.php">Audi</a>
					  <a href="jaguar.php">Jaguar</a>
					  <a href="toyota.php">Toyota</a>
					  <a href="ford.php">Ford</a>
					  <a href="honda.php">Honda</a>
					  
					</div>
				  </div> </td>
				
				</tr>
			</table>
			</div>
			
			
		<div class="demo">
				<table class="demo" >
					
					<script type="text/javascript">
					
						var car_name=new Array(12);
						for(var i=1;i<=12;i++)
						{
							car_name[i-1]="cars_"+i+".jpg";
						}
						var j=0;
						var car_names=["AMG GT R","BMW Coupe","BMW i8","Chevrolet Camaro","BMW Z4","Range Rover Velar","AMG GTS-D","Corvette ZO6","AMG Coupe"]
						for(var i=0;i<3;i++)
						{	document.writeln("<tr>");
							for(var k=0;k<3;k++)
								{
								
									document.writeln("<th><img src="+car_name[j]+"  class=\"demo\"  width=\"450px\" height=\"300px\" onmouseover=\"\">"+"<br/><p id=\"carnames\">"+car_names[j]+"</p><br/>"+"</th>");
									j++;
								}
							document.writeln("</tr>");

						}
					
						
					</script>
				</table>
			</div>
			
			
			<div align="right" >
			<a class="button"href="forsale.html;" style="text-decoration:none;" >View More</a>
			</div>
			
			
			
			<br/>
			<br/>
		
			<div class="sl">
			<table align="center" width="85%" height="100px" style="background-color:rgb(51, 66, 82);z-index:1">
				<tr> <th align="left"><p style="color:white;font-size:30px;font-family:Arial;font-weight:400;margin-left:20px">Site Links</p></th> <th align="left"><p style="color:white;font-size:30px;font-family:Arial;font-weight:400;">Top Brands</p></th><th></th></tr>
				<tr valign="top"><td><p style="color:gray;font-size:20px;">Home<br/>
															Cars<br/>
															Motorcycles<br/>
															All Brands<br/>
															All Dealers<br/>
															<a href="faq.html" style="text-decoration:None"><span style="color:gray;font-size:20px">FAQs</span></a> 
				</p></td>
				<td><p style="color:gray;font-size:20px">Ferrari<br/>
														Aston Martin<br/>
														Koenigsegg<br/>
														Lamborghini<br/>
														Bugatti<br/>
														Maserati<br/>
														Pagani<br/>
														Porsche<br/>
														Rolls-Royce<br/>
														Ducati</p></td>
				<td> <p style="color:gray;font-size:20px">Audemars Piguet<br/>
																Breguet<br/>
																Bulgari<br/>
																Cartier<br/>
																Piaget<br/>
																Ferretti Yachts<br/>
																Benetti Yachts<br/>
																Boeing<br/>
																Bombardier<br/>
																Cessna<br/>
																Dassault</p></td></tr>
														
				
			</table>
		
			<table  align="right"  style="z-index:2;position:relative;bottom:100px;background-color:rgb(51, 66, 82);">
			<tr><td>
				<a href="#" class="fa fa-facebook"></a>
				<a href="#" class="fa fa-twitter"></a>
				<a href="#" class="fa fa-google"></a>
				<a href="#" class="fa fa-youtube"></a>
				<a href="#" class="fa fa-instagram"></a>
			</td></tr>
			</table>
			</div>
			
			
			
			
	</body>
</html>