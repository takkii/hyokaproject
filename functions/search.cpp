# include "all.h"  // IWYU pragma: export

namespace Rice::detail {
class Validation {
public:
    Validation() {};
    void check() { 
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
    }
};

extern "C" {
void Init_validation() {
    Data_Type<Validation> rb_cValidation = define_class<Validation>("Validation")
    .define_constructor(Constructor<Validation>())
    .define_method("check", &Validation::check);
    }
  }
}