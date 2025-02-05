import java.io.File

var enabled = true

fun computeInstr(instr: String): Int {
    return instr.substring(4, instr.length-1)
        .split(',')
        .map { it.toInt() }
        .reduce { prod, ele -> prod*ele }
}

fun scanMem(mem: String): Int {
    val regex = "mul\\(\\d{1,3},\\d{1,3}\\)".toRegex()
    return regex.findAll(mem).sumOf { computeInstr(it.value) }
}

fun scanMemAdv(mem: String): Int {
    val regex = "mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don't\\(\\)".toRegex()
    var memRes = 0
    regex.findAll(mem).forEach {
        val curInstr = it.value
        when (curInstr) {
            "do()" -> enabled = true
            "don't()" -> enabled = false
            else -> if (enabled) {
                memRes += computeInstr(curInstr)
            }
        }
    }
    return memRes
}

fun main() {
    val memArr = File("./2024/03/in.txt").readLines()
    // part 1
//    println(memArr.sumOf { scanMem(it) })
    // part 2
    println(memArr.sumOf { scanMemAdv(it) })
}