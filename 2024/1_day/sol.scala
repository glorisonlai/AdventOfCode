import scala.io.Source
import scala.math.abs

@main
def main(): Unit = {
  val source = Source.fromFile("input.txt")
  val lBuilder = List.newBuilder[Int]
  val rBuilder = List.newBuilder[Int]
  for (line <- source.getLines()) {
    val Array(l, r) = line.split("\\s+").map(_.toInt)
    (lBuilder += l, rBuilder += r)
  }
  val lList = lBuilder.result().sorted
  val rList = rBuilder.result().sorted

  val sum = lList.zip(rList).map((a,b) => abs(a-b)).reduceLeft((sum, e) => sum + e)
  print(sum)
}
  
