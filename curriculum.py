# curriculum.py

lessons_data = [
    {
        "id": 1,
        "title": "Level 1: Variables as Attributes",
        "theory": """
            <h3>Concept: The Container</h3>
            <p>In GIS, every feature on a map has attributes (Name, ID, Population). In Python, we store these single pieces of information in <strong>Variables</strong>.</p>
            <p>Think of a variable as a labeled box. You can put data in, and when you ask for the box by name, it gives you the data back.</p>
            <div class="code-block">
            city_name = "Durban"  # String (Text)
            elevation = 12        # Integer (Whole number)
            is_coastal = True     # Boolean (True/False)
            </div>
        """,
        "instruction": """
            <ol>
                <li>Create a variable named <code>dam_name</code> and set it to the text <code>"Gariep Dam"</code>.</li>
                <li>Create a variable named <code>capacity_pct</code> and set it to <code>98</code>.</li>
                <li><strong>Print</strong> the dam name exactly as stored.</li>
            </ol>
        """,
        "default_code": "# 1. Define the name\n\n# 2. Define the capacity\n\n# 3. Print only the name\n",
        "expected_output": "Gariep Dam",
        "hint": "Python is case-sensitive. 'Gariep Dam' is not the same as 'gariep dam'. Use print(dam_name) to finish."
    },
    {
        "id": 2,
        "title": "Level 2: Lists as Survey Points",
        "theory": """
            <h3>Concept: Ordered Collections</h3>
            <p>A Data Analyst rarely looks at one number. You look at thousands. A <strong>List</strong> allows you to hold many items in a specific order, like a list of stops on a taxi route or a sequence of survey points.</p>
            <p>Lists use square brackets <code>[]</code>.</p>
            <div class="code-block">
            # A list of rainfall measurements (mm)
            rainfall = [12, 45, 0, 8, 22]
            
            # Accessing data: Computers count from 0!
            print(rainfall[0]) # Prints 12
            </div>
        """,
        "instruction": """
            <ol>
                <li>Create a list named <code>provinces</code> containing exactly these three strings: <code>"Gauteng"</code>, <code>"KZN"</code>, and <code>"Western Cape"</code>.</li>
                <li>Print the <strong>last</strong> item in the list using its index.</li>
            </ol>
        """,
        "default_code": "provinces = []\n\n# Remember: The first item is index 0, the second is 1...\nprint()",
        "expected_output": "Western Cape",
        "hint": "Since there are 3 items, the indices are 0, 1, and 2. The last item is at index 2."
    },
    {
        "id": 3,
        "title": "Level 3: Dictionaries as Attribute Tables",
        "theory": """
            <h3>Concept: Key-Value Pairs</h3>
            <p>This is the most important structure for a Data Analyst. A <strong>Dictionary</strong> is exactly like a row in a GIS attribute table. It allows you to look up values based on a 'Key' rather than a number index.</p>
            <p>Dictionaries use curly braces <code>{}</code>.</p>
            <div class="code-block">
            feature = {
                "type": "School",
                "students": 1200,
                "active": True
            }
            print(feature["students"]) # Prints 1200
            </div>
        """,
        "instruction": """
            <ol>
                <li>Create a dictionary named <code>station</code> representing a weather station.</li>
                <li>It must have two keys: <code>"code"</code> set to <code>"JHB-01"</code> and <code>"temp"</code> set to <code>24</code>.</li>
                <li>Print the value associated with the <code>"code"</code> key.</li>
            </ol>
        """,
        "default_code": "station = {\n    # key: value\n}\n\n# Access the code using square brackets ['key']\nprint()",
        "expected_output": "JHB-01",
        "hint": "Make sure you use colons (:) between the key and value, and commas (,) to separate items."
    },
    {
        "id": 4,
        "title": "Level 4: Loops for Batch Processing",
        "theory": """
            <h3>Concept: Automation</h3>
            <p>If you have to update 10,000 map features, you don't do it manually. You use a <strong>Loop</strong>. A loop takes a list and runs the same code for every item inside it.</p>
            <div class="code-block">
            measurements = [10, 20, 30]
            
            for m in measurements:
                print(m + 5) 
            # This prints 15, then 25, then 35
            </div>
        """,
        "instruction": """
            <p>We have a list of river pH levels. We want to simply print each level.</p>
            <ol>
                <li>Create a list <code>ph_levels</code> with values: <code>7.0</code>, <code>6.5</code>, <code>8.1</code>.</li>
                <li>Write a <code>for</code> loop to iterate through the list.</li>
                <li>Inside the loop, simply <code>print</code> the current value.</li>
            </ol>
        """,
        "default_code": "ph_levels = [7.0, 6.5, 8.1]\n\nfor val in ph_levels:\n    # Indentation is CRITICAL in Python\n    # Type your print statement indented here\n    pass",
        "expected_output": "7.0\n6.5\n8.1",
        "hint": "The code inside the loop must be indented (press Tab). It should look like: print(val)"
    },
    {
        "id": 5,
        "title": "Level 5: Logic for Classification",
        "theory": """
            <h3>Concept: Decision Making</h3>
            <p>Data Analysis is often about classifying data. 'If population > 1 million, it is a Metro.' 'If rainfall < 200mm, it is arid.'</p>
            <p>We use <code>if</code>, <code>elif</code>, and <code>else</code>.</p>
        """,
        "instruction": """
            <p>Classify a population density.</p>
            <ol>
                <li>Set a variable <code>density</code> to <code>550</code>.</li>
                <li>Write an if-statement:
                    <ul>
                        <li>If density is greater than 500, print <code>"Urban"</code>.</li>
                        <li>Else, print <code>"Rural"</code>.</li>
                    </ul>
                </li>
            </ol>
        """,
        "default_code": "density = 550\n\nif density > 500:\n    # print Urban\nelse:\n    # print Rural",
        "expected_output": "Urban",
        "hint": "Don't forget the colon (:) at the end of the 'if' and 'else' lines."
    }
]