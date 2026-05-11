# include "all.h"  // IWYU pragma: export

int main(void) {
    // reading text file.
    typedef istream_iterator<char> Istr;
    string filename = "../effect.txt";
    ifstream fin(filename, ios::in);
    fin >> noskipws;
    Istr in(fin), eof;
    string buf;
    copy(in, eof, back_inserter(buf));
    
    // regex objects
    regex regex("Doe");
    match_results<string::iterator> matched;
 
    for (auto it = begin(buf); it != end(buf); ++it) {
        if (regex_search(it, end(buf), matched, regex)) {
            for (unsigned int i = 0; i < matched.size(); i++) {
                cout << "Match word contain " << matched[i] << " in " << filename << endl;
                return 0;
            }
            it = matched[0].second;
        }
        else {
            cout << "No, Match Word in " << filename << endl;
            return 0;
        }
    }
 
    return 0;
}