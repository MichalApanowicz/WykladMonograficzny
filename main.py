import losowanie
import znajdowanie
import redukcja

#pairs = [((1,1),(2,2)),((1,1),(4,4)),((1,1),(5,5)),((2,2),(3,3)),((2,2),(4,4)),((2,2),(5,5)),((3,3),(4,4)),((4,4),(5,5))]
#pairs = [((1,1),(2,2)),((1,1),(3,3)),((2,2),(3,3))]

pairs = losowanie.losujPunkty(X=100, N=100, R=10, debbug=True)
#print ("pary: " + str(pairs))

dictionary = znajdowanie.znajdzKrawedzie(pairs, debug=True)
#print ("dictionary: " + str(dictionary))

arrays = redukcja.mapDictionaryToTuples(dictionary, debug=True)
#print ("arrays: " + str(arrays))