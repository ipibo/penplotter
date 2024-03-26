const express = require("express")
const app = express()
const port = 3000
const { exec } = require("child_process")
const fs = require("fs")
const path = require("path")

// Require the upload middleware
const upload = require("./upload")

// Set up a route for file uploads
app.post("/upload", upload.single("file"), (req, res) => {
  // Handle the uploaded file
  // res.json({ message: "File uploaded successfully!" })
  // Redirect the user back to the page
  console.log(req.file.path)
  exec(
    `python /home/pi/svg2gcode_grbl/convert.py /home/pi/penplotter/server/${req.file.path} /home/pi/out.gcode`,
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error executing script: ${error}`)
        res.statusCode = 500
        res.end("Internal Server Error")
      } else {
        console.log(`Script output: ${stdout}`)
        res.statusCode = 200
        res.end("Script executed successfully")

        exec(
          "python /home/pi/penplotter/plotting/readFile.py",
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
      }
    }
  )

  res.redirect("/")
})

app.post("/run-script", (req, res) => {
  exec(
    "python /home/pi/penplotter/plotting/manualControl.py",
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
})

app.listen(port, () => {
  console.log(`Server is running on port ${port}`)
})
app.get("/", function (req, res) {
  res.sendFile(__dirname + "/index.html")
})
