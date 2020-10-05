class Occurrence {

    Occurrence( String inSymbol, int inCountOfOccurrences ) {
        symbol = inSymbol
        countOfOccurrences = inCountOfOccurrences
    }

    String getCompressedString( ){
        String.valueOf(countOfOccurrences) + "{" + symbol + "}"
    }

    int getCountOfOccurrences( ) {
        countOfOccurrences
    }

    private String symbol
    private int countOfOccurrences

}
