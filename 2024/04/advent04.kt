import java.io.File

val dir = listOf(0, 1, -1)

class WordSearch(private val board: List<String>) {
    private val rowCount = board.size
    private val colCount = board[0].length
    private val rowRange = 0 until rowCount
    private val colRange = 0 until colCount

    fun countXmas() {
        var count = 0
        for (i in 0 until rowCount) {
            for (j in 0 until colCount) {
                if (board[i][j] == 'X') {
                    count += countXmas(i, j)
                }
            }
        }
        println(count)
    }

    fun countXMAS() {
        var count = 0
        for (i in 1 until rowCount-1) {
            for (j in 1 until colCount-1) {
                if (board[i][j] == 'A') {
                    val slash1 = listOf(board[i-1][j-1], board[i+1][j+1])
                    val slash2 = listOf(board[i+1][j-1], board[i-1][j+1])
                    if (slash1.containsAll(listOf('M', 'S')) &&
                        slash2.containsAll(listOf('M', 'S'))) {
                        count++
                    }
                }
            }
        }
        println(count)
    }

    private fun countXmas(i: Int, j: Int): Int {
        var count = 0
        dir.forEach { dx ->
            dir.forEach { dy ->
                if (rowRange.contains(i + 3 * dx) && colRange.contains(j + 3 * dy)) {
                    if (board[i + dx][j + dy] == 'M' &&
                        board[i + 2 * dx][j + 2 * dy] == 'A' &&
                        board[i + 3 * dx][j + 3 * dy] == 'S') {
                        count++
                    }
                }
            }
        }
        return count
    }
}

fun main() {
    val board = File("./2024/04/in.txt").readLines()
    WordSearch(board).countXmas()
    WordSearch(board).countXMAS()
}
