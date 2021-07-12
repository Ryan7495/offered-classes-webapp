<html>
<head>
	<title>Course credit table search</title>
	<style type="text/css"></style>
</head>
<body>
	<h1>Search Results</h1>

	<?php 
		$servername = "";
		$username = "";
		$password = "";
		$database = "";

		$mysql = new mysqli($servername, $username, $password, $database);

		if ($mysql -> connect_errno)
		{
			printf("Connect failed: %s\n", $mysqli -> connect_error);
			exit();
		}

		// Relavant SQL DB attributes to the search fields
		$search_by = ["institution", "other_class", "dal_class", "other_credit_hours", "date"];
		$query = "SELECT * FROM csci3172_lab6";
		$lock = 0;

		// Find all search fields with an entry and build a SQL
		// query to search by all fields.
		for ($i = 0; $i < 5; $i++)
		{
			$name = "search" . $i;
			if (strlen($_POST[$name]) > 0)
			{
				if ($lock == 0)
				{
					$query .= " WHERE ";
				}
				else
				{
					$query .= " AND ";
				}
				$lock++;

				$query .= $search_by[$i] . " = \"$_POST[$name]\"";
			}
		}
		$query .= ";";
		echo $query;
		echo "<br>";
 		
		// Execute the SQL query
		if ($result = $mysql -> query($query)) 
		{	
			print_table($result);
		}
		else
		{
			echo "Error: " . $sql . "<br>" . $mysql -> error;
		}
		

		//DEPRICATED
		function search_by_host_university ()
		{
			if ($result = $mysql -> query("SELECT * FROM csci3172_lab6 WHERE institution = \"$search\";")) 
			//if ($result = $mysql -> query("SELECT * FROM csci3172_lab6 LIMIT 12"))
			{	
				print_table($result);
			}
			else
			{
				echo "Error: " . $sql . "<br>" . $mysql -> error;
			}
		}

		// Print the table of returned values
		function print_table ($result)
		{
			echo '<table>';
			echo '<tr><th>Other Course</th><th>Credit Hours</th><th>Dal Course</th><th>Credit Hours</th><th>Date</th><th>Institution</th><th>Subject</th></tr>';

			while ($row = mysqli_fetch_array($result))
			{
				echo '<tr><td>';
				echo $row['other_class'];
				echo '</td><td>';
				echo $row['other_credit_hours'];
				echo '</td><td>';
				echo $row['dal_class'];
				echo '</td><td>';
				echo $row['dal_credit_hours'];
				echo '</td><td>';
				echo $row['date'];
				echo '</td><td>';
				echo $row['institution'];
				echo '</td><td>';
				echo $row['subject'];
				echo '</td></tr>';
			}
			echo '</table>';
		}

	?>


</body>
</html>
