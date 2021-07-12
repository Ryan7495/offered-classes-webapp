<html>
<head>
	<title>Course credit table search</title>
	<style type="text/css"></style>
</head>
<body>
	<h1>Search Builder</h1>

	<?php 
		search_bar();
				

		function search_bar ()
		{
			echo '<div class="topnav">';
			echo '<form name="form" action="result.php" method="post">';
			echo '<input type="text" id="search0" name="search0" placeholder="by host university">';
			echo '<input type="text" id="search1" name="search1" placeholder="by host course">';
			echo '<input type="text" id="search2" name="search2" placeholder="by dal course">';
			echo '<input type="text" id="search3" name="search3" placeholder="by credit hours">';
			echo '<input type="text" id="search4" name="search4" placeholder="by date">';
			echo '<input type="submit" id="button" value="submit">';
			echo '</form>';
			echo '</div>';
			echo '<br>';
		}

	?>


</body>
</html>