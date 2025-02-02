import java.io.File
import kotlin.math.abs

const val MIN_DIFF = 1
const val MAX_DIFF = 3

fun increasing(report: List<Int>, reportSize: Int): Boolean {
    for (i in 1 until reportSize) {
        if (report[i] <= report[i - 1]) {
            return false
        }
    }
    return true
}

fun decreasing(report: List<Int>, reportSize: Int): Boolean {
    for (i in 1 until reportSize) {
        if (report[i] >= report[i - 1]) {
            return false
        }
    }
    return true
}

// part 1 function
fun isSafe(report: List<Int>): Boolean {
    val reportSize = report.size;
    if (!increasing(report, reportSize) and !decreasing(report, reportSize)) {
        return false;
    }
    for (i in 1 until reportSize) {
        val diff = abs(report[i] - report[i - 1])
        if (diff < MIN_DIFF || diff > MAX_DIFF) {
            return false
        }
    }
    return true
}

// part 2 function
fun isSafeAfterRemoving(report: List<Int>): Boolean {
    val reportSize = report.size
    for (i in 0 until reportSize) {
        val mutatedReport = report.filterIndexed { j, _ -> j != i }
        if (isSafe(mutatedReport)) {
            return true;
        }
    }
    return false
}

fun countSafeReports(reports: List<List<Int>>) {
    println(reports.count { isSafe(it) || isSafeAfterRemoving(it) })
}

fun main() {
    val reports = File("./2024/02/in.txt")
        .readLines()
        .map { it.split(" ") }
        .map { it.map { str -> str.toInt() } }
    countSafeReports(reports)
}