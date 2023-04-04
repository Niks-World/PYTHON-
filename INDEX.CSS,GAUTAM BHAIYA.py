div {
  display: flex;
  justify-content: space-around;
}
form {
  margin: 0 auto;
  margin-top: 50px;
  width: 30%;
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  padding: 30px;
}

label {
  font-size: 20px;
}

table {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 60%;
  margin: auto;
  margin-top: 50px;
  text-align: center;
}

table td,
table th {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

table tr:nth-child(even) {
  background-color: #8caacf;
}

table tr:hover {
  background-color: #ddd;
}

table th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #0468aa;
  color: white;
  text-align: center;
}

* {
  box-sizing: border-box;
}

input[type="text"],
select,
textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}

input[type="submit"] {
  background-color: #2b619e;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  width: 100%;
  font-size: 20px;
}

input[type="submit"]:hover {
  background-color: #3973b6;
}

h1 {
  text-align: center;
  font-size: 50px;
  text-transform: uppercase;
  font-family: monospace;
  color: #2b619e;
  text-decoration: underline;
}
