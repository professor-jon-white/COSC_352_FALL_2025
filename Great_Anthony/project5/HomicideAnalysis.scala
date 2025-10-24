import scala.io.Source
import scala.util.{Try, Using}
import java.time.LocalDate
import java.time.format.DateTimeFormatter
import scala.collection.mutable.ListBuffer
import java.io.PrintWriter
import java.nio.charset.CodingErrorAction
import scala.io.Codec

case class HomicideRecord(
  uid: String,
  date: LocalDate,
  victimName: String,
  age: Option[Int],
  city: String,
  state: String,
  disposition: String
)

object HomicideAnalysis {
  def main(args: Array[String]): Unit = {
    val outputFormat = if (args.length > 0) args(0) else "stdout"
    
    println(s"Starting Baltimore Homicide Analysis with output format: $outputFormat")
    
    val records = readHomicideData("data/homicide-data.csv")
    
    println(s"Successfully loaded ${records.length} records")
    
    val analysis = analyzeData(records)
    
    outputFormat.toLowerCase match {
      case "csv" => writeCSV(analysis)
      case "json" => writeJSON(analysis)
      case _ => writeStdout(analysis)
    }
  }
  
  def readHomicideData(filename: String): List[HomicideRecord] = {
    // Handle encoding issues
    implicit val codec: Codec = Codec("UTF-8")
    codec.onMalformedInput(CodingErrorAction.REPLACE)
    codec.onUnmappableCharacter(CodingErrorAction.REPLACE)
    
    val dateFormatter = DateTimeFormatter.ofPattern("yyyyMMdd")
    val records = ListBuffer[HomicideRecord]()
    
    Using(Source.fromFile(filename)) { source =>
      val lines = source.getLines().toList
      val dataLines = lines.tail
      
      dataLines.foreach { line =>
        try {
          val parts = line.split(",")
          if (parts.length >= 12) {
            val uid = parts(0).trim
            val date = Try(LocalDate.parse(parts(1).trim, dateFormatter)).getOrElse(LocalDate.now())
            val victimName = s"${parts(3).trim} ${parts(2).trim}"
            val age = Try(parts(5).trim.toInt).toOption
            val city = parts(7).trim
            val state = parts(8).trim
            val disposition = parts(11).trim
            
            records += HomicideRecord(uid, date, victimName, age, city, state, disposition)
          }
        } catch {
          case e: Exception => 
            // Skip malformed lines
        }
      }
    }
    
    records.toList
  }
  
  def analyzeData(records: List[HomicideRecord]): Map[String, Any] = {
    // Filter for Baltimore (case-insensitive)
    val baltimoreRecords = records.filter(r => r.city.equalsIgnoreCase("Baltimore"))
    println(s"Found ${baltimoreRecords.length} Baltimore records")
    
    val closedCases = baltimoreRecords.count(_.disposition.toLowerCase.contains("closed"))
    
    Map(
      "total_homicides" -> baltimoreRecords.length,
      "cases_closed" -> closedCases,
      "cases_open" -> (baltimoreRecords.length - closedCases),
      "average_age" -> {
        val ages = baltimoreRecords.flatMap(_.age)
        if (ages.nonEmpty) ages.sum.toDouble / ages.length else 0.0
      },
      "by_year" -> baltimoreRecords.groupBy(_.date.getYear).view.mapValues(_.length).toList.sortBy(_._1),
      "by_month" -> baltimoreRecords.groupBy(_.date.getMonthValue).view.mapValues(_.length).toList.sortBy(_._1),
      "by_disposition" -> baltimoreRecords.groupBy(_.disposition).view.mapValues(_.length).toList.sortBy(-_._2)
    )
  }
  
  def writeStdout(analysis: Map[String, Any]): Unit = {
    println("\n=== Baltimore Homicide Statistics ===")
    println(s"Total Homicides: ${analysis("total_homicides")}")
    println(s"Cases Closed: ${analysis("cases_closed")}")
    println(s"Cases Open: ${analysis("cases_open")}")
    println(f"Average Age: ${analysis("average_age").asInstanceOf[Double]}%.1f")
    
    println("\n=== Homicides by Year ===")
    analysis("by_year").asInstanceOf[List[(Int, Int)]].foreach { case (year, count) =>
      println(f"$year: $count")
    }
    
    println("\n=== Homicides by Month ===")
    analysis("by_month").asInstanceOf[List[(Int, Int)]].foreach { case (month, count) =>
      println(f"Month $month: $count")
    }
    
    println("\n=== Top Dispositions ===")
    analysis("by_disposition").asInstanceOf[List[(String, Int)]].take(5).foreach { case (disp, count) =>
      println(f"$disp: $count")
    }
  }
  
  def writeCSV(analysis: Map[String, Any]): Unit = {
    val writer = new PrintWriter("output.csv")
    
    writer.println("Metric,Value")
    writer.println(s"Total Homicides,${analysis("total_homicides")}")
    writer.println(s"Cases Closed,${analysis("cases_closed")}")
    writer.println(s"Cases Open,${analysis("cases_open")}")
    writer.println(f"Average Age,${analysis("average_age").asInstanceOf[Double]}%.1f")
    
    writer.println("\nYear,Count")
    analysis("by_year").asInstanceOf[List[(Int, Int)]].foreach { case (year, count) =>
      writer.println(s"$year,$count")
    }
    
    writer.println("\nMonth,Count")
    analysis("by_month").asInstanceOf[List[(Int, Int)]].foreach { case (month, count) =>
      writer.println(s"$month,$count")
    }
    
    writer.println("\nDisposition,Count")
    analysis("by_disposition").asInstanceOf[List[(String, Int)]].foreach { case (disp, count) =>
      writer.println(s"$disp,$count")
    }
    
    writer.close()
    println("Output written to output.csv")
  }
  
  def writeJSON(analysis: Map[String, Any]): Unit = {
    val writer = new PrintWriter("output.json")
    
    writer.println("{")
    writer.println(s"""  "total_homicides": ${analysis("total_homicides")},""")
    writer.println(s"""  "cases_closed": ${analysis("cases_closed")},""")
    writer.println(s"""  "cases_open": ${analysis("cases_open")},""")
    writer.println(f"""  "average_age": ${analysis("average_age").asInstanceOf[Double]}%.1f,""")
    
    writer.println("""  "by_year": [""")
    val byYear = analysis("by_year").asInstanceOf[List[(Int, Int)]]
    byYear.zipWithIndex.foreach { case ((year, count), idx) =>
      val comma = if (idx < byYear.length - 1) "," else ""
      writer.println(s"""    {"year": $year, "count": $count}$comma""")
    }
    writer.println("  ],")
    
    writer.println("""  "by_month": [""")
    val byMonth = analysis("by_month").asInstanceOf[List[(Int, Int)]]
    byMonth.zipWithIndex.foreach { case ((month, count), idx) =>
      val comma = if (idx < byMonth.length - 1) "," else ""
      writer.println(s"""    {"month": $month, "count": $count}$comma""")
    }
    writer.println("  ],")
    
    writer.println("""  "by_disposition": [""")
    val byDisp = analysis("by_disposition").asInstanceOf[List[(String, Int)]]
    byDisp.zipWithIndex.foreach { case ((disp, count), idx) =>
      val comma = if (idx < byDisp.length - 1) "," else ""
      val cleanDisp = disp.replace("\"", "\\\"")
      writer.println(s"""    {"disposition": "$cleanDisp", "count": $count}$comma""")
    }
    writer.println("  ]")
    
    writer.println("}")
    writer.close()
    println("Output written to output.json")
  }
}
