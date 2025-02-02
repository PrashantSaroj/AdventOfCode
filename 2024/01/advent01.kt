import java.io.File
import kotlin.math.abs

fun similarityScores(l1: List<Int>, l2: List<Int>) {
    val freq = mutableMapOf<Int, Int>()
    l2.forEach {
        freq[it] = freq.getOrDefault(it, 0) + 1
    }

    var similarity = 0
    l1.forEach {
        similarity += freq.getOrDefault(it, 0)*it
    }
    println(similarity)
}

fun distanceLists(l1: List<Int>, l2: List<Int>) {
    var totalDistance = 0
    l1.zip(l2) { n1, n2 ->
        totalDistance += abs(n1 - n2)
    }
    println(totalDistance)
}

fun main() {
    val rawInput = File("./2024/01/in.txt").readLines().map { it.split(" ") }
    val list1 = mutableListOf<Int>()
    val list2 = mutableListOf<Int>()

    rawInput.forEach {
        list1.add(it[0].toInt())
        list2.add(it[1].toInt())
    }
    list1.sort()
    list2.sort()

    distanceLists(list1, list2)
    similarityScores(list1, list2)
}