# This file holds the lesson data. 
# You can write your own lessons here to test yourself later!

lessons_data = [
    {
        "id": 1,
        "title": "Level 1: The Coordinates (Variables)",
        "theory": """
            <p>In Python, a <strong>variable</strong> is like a container on a map. You give it a name, and store data inside it.</p>
            <p>For a Data Analyst, variables often hold values like population counts, city names, or coordinates.</p>
            <p>Syntax: <code>variable_name = value</code></p>
        """,
        "instruction": "Create a variable named <code>city</code> and set it to 'Pretoria'. Then, create a variable <code>population</code> and set it to 741651. Finally, print the city.",
        "default_code": "# Create your variables below\n\n\n# Print the city\n",
        "expected_output": "Pretoria",
        "hint": "Use print(city) to show the output."
    },
    {
        "id": 2,
        "title": "Level 2: The Survey List (Lists)",
        "theory": """
            <p>As a Geographer, you rarely deal with one city. You deal with lists of them.</p>
            <p>A <strong>List</strong> is a collection of items ordered by index.</p>
            <p>Syntax: <code>cities = ['JHB', 'CPT', 'DBN']</code></p>
        """,
        "instruction": "Create a list named <code>provinces</code> containing 'Gauteng', 'Limpopo', and 'Natal'. Then print the <strong>second</strong> item in the list.",
        "default_code": "provinces = []\n\n# Remember: Python starts counting at 0!\nprint()",
        "expected_output": "Limpopo",
        "hint": "Access the second item using brackets: provinces[1]"
    },
    {
        "id": 3,
        "title": "Level 3: Temperature Logic (If/Else)",
        "theory": """
            <p>Data Analysis requires logic. If the rainfall is high, do X. If low, do Y.</p>
            <p>We use <code>if</code>, <code>elif</code>, and <code>else</code> statements.</p>
        """,
        "instruction": "Write an if-statement. Set a variable <code>temp = 35</code>. If temp is greater than 30, print 'Heatwave'. Otherwise, print 'Normal'.",
        "default_code": "temp = 35\n\nif temp > 30:\n    # code here\nelse:\n    # code here",
        "expected_output": "Heatwave",
        "hint": "Make sure your indentation (spacing) is correct inside the if statement."
    }
]