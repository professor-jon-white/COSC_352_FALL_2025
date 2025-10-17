import scala.io.Source
import java.net.URL
import java.io._

object HomicideAnalysis {
  def main(args: Array[String]): Unit = {
    println("=" * 60)
    println("Baltimore City Homicide Data Analysis")
    println("=" * 60)
    println()

    // Download CSV from the website
    val url = "https://chamspage.blogspot.com/p/baltimore-homicides.html" 
    val csvFile = "homicides.csv"

    if (!new File(csvFile).exists()) {
      try {
        val source = Source.fromURL(new URL(url))
        val lines = source.getLines().toList
        source.close()
        val writer = new PrintWriter(new File(csvFile))
        lines.foreach(writer.println)
        writer.close()
        println(s"Downloaded CSV to $csvFile")
      } catch {
        case e: Exception =>
          println(s"Failed to download CSV: ${e.getMessage}")
          System.exit(1)
      }
    }

    // Read CSV
    val dataLines = Source.fromFile(csvFile).getLines().toList
    if (dataLines.isEmpty) {
      println("CSV file is empty or missing data")
      System.exit(1)
    }

    val header = dataLines.head.split(",").map(_.trim)
    val data = dataLines.tail

    // Question 1: Average victim age in 2025
    val victims2025 = data.filter { line =>
      val cols = line.split(",").map(_.trim)
      cols(1).contains("/25") 
    }
    val ages2025 = victims2025.map(line => line.split(",")(3).toInt)
    val avgAge2025 = if (ages2025.nonEmpty) ages2025.sum.toDouble / ages2025.length else 0.0
    println("Question 1: Average victim age in 2025")
    println(f"Answer: $avgAge2025%.2f years")
    println()

    // Question 2: Most common camera count in homicide cases
    val cameraCounts = data.map(line => line.split(",")(6).trim)
    val mostCommonCamera = cameraCounts.groupBy(identity).mapValues(_.size).maxBy(_._2)._1
    println("Question 2: Most common number of cameras capturing homicides")
    println(s"Answer: $mostCommonCamera")
    println()
    
    println("=" * 60)
    println("Analysis Complete")
    println("=" * 60)
  }
}
