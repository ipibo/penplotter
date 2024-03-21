const http = require("http")
const { exec } = require("child_process")
const fs = require("fs")
const path = require("path")

const server = http.createServer((req, res) => {
  if (req.url === "/run-script") {
    // Execute the Python script
    exec(
      "python /home/pi/Desktop/penplotter/plotting/manualControl.py",
      (error, stdout, stderr) => {
        if (error) {
          console.error(`Error executing script: ${error}`)
          res.statusCode = 500
          res.end("Internal Server Error")
        } else {
          console.log(`Script output: ${stdout}`)
          res.statusCode = 200
          res.end("Script executed successfully")
        }
      }
    )
  } else {
    res.statusCode = 200
    const filePath = path.join(__dirname, "index.html")
    fs.readFile(filePath, (error, content) => {
      if (error) {
        console.error(`Error reading file: ${error}`)
        res.statusCode = 500
        res.end("Internal s Error")
      } else {
        res.setHeader("Content-Type", "text/html")
        res.end(content)
      }
    })
  }
})

const port = 3000
server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`)
})
