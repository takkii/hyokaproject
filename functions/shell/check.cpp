# include "all_check.h"  // IWYU pragma: export

int main(void){ 
        try
        {
            // reading text file.
            typedef istream_iterator<char> Istr;
            string filename = "./effect.txt";
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
                        exit(0);
                    }
                
                it = matched[0].second;
                }

                else {
                    cout << "No, Match Word in " << filename << endl;
                    exit(0);
                }
            }
        } catch (runtime_error& e) {
          cout << "runtime error : " << e.what() << endl;
        } catch (const exception& e) {
          cout << "some exception : " << e.what() << endl;
    }
    return 0;
}