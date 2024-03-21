const http = require("http")
const { exec } = require("child_process")

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
    res.setHeader("Content-Type", "text/plain")
    res.end("Hello, world!")
  }
})

const port = 3000
server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`)
})
