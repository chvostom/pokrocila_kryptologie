/*Zakomentované části slouží k sestavení výsledného komprimovaného řetězce*/
List<String> names = ['/f15', '/f14', '/f13', '/f12', '/f11', '/f10', '/f9', '/f8', '/f7', '/f6', '/f5', '/f4', '/f3', '/f2', '/f1', '/f0' ]
for ( String name : names ) {
    /*Inicializace proměnných*/
    File file = new File( this.getClass( ).getResource( name ).getPath( ) )
    List<Occurrence> occurrences = new ArrayList<>()
    String content = file.getText()
    int counter = 1
    int resultSizeCounter = 0
    int avarageOccurrences = 0
    //String result = ""

    /*Identifikace opakujících se bitů*/
    for ( int i = 0 ; i < content.size() - 1 ; i++ ){
        if (content[i] == content[i+1] ) {
            counter++
        }
        else {
            occurrences.add( new Occurrence(content[i], counter))
            resultSizeCounter += String.valueOf(counter).size() + 4
            counter = 1
        }
    }

    /*Započtení posledního bitu*/
    occurrences.add( new Occurrence(content[content.size() - 1], counter))
    resultSizeCounter += String.valueOf(counter).size() + 4

    /*Výpočet průměrné délky opakujících se posloupností případně sestavení komprimovaného řetězce*/
    for ( Occurrence occurrence : occurrences) {
        //result += occurrence.getCompressedString()
        avarageOccurrences += occurrence.getCountOfOccurrences()
    }
    avarageOccurrences /= occurrences.size()

    /*Výpis výsledků*/
    //println(result)
    println("=================================================================")
    println("Název souboru: " + name)
    println("Zkomprimováno na " + 100 * resultSizeCounter / content.size() + "% původní velikosti" )
    println("Průměrná velikost opakující se podposloupnosti: " + avarageOccurrences)
    println("Šance, že následující bit bude stejný: " + 100 * Double.valueOf( ( avarageOccurrences - 1 ) / avarageOccurrences) + "%" )
}
println("=================================================================")