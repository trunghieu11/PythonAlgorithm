//==================================================================
//Author        : Nguyen Trung Hieu - vuondenthanhcong11@yahoo.com
//Problem Name  :
//Discription   :
//Reference from:
//==================================================================

// -------------------- Khai bao thu vien --------------------
#include <deque>
#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
using namespace std;
// -------------------- Khai bao cac container --------------------
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef vector <string> vs;
typedef long long int64; //NOTES:int64
typedef unsigned long long uint64; //NOTES:uint64
typedef unsigned uint;
const double pi = acos(-1.0); //NOTES:pi
const double eps = 1e-11; //NOTES:eps
const int MAXI = 0x7fffffff;
const int dx4[] = {1, 0, -1, 0};
const int dy4[] = {0, 1, 0, -1};
const char dz4[] = "SENW";
const int dx8[] = {1, 1, 1, 0, -1, -1, -1, 0};
const int dy8[] = {-1, 0, 1, 1, 1, 0, -1, -1};
// -------------------- Dinh nghia lai cac phep toan --------------------
#define forn(i,a,b)     for (int i=(a),_b=(b); i<_b; i++)
#define rforn(i,b,a)    for (int i=(b)-1,_a=(a); i>=_a; i--)
#define reset(a,b)      memset((a),(b),sizeof(a))
#define endline         putchar('\n')
#define space           putchar(' ')
#define EXIT(x)         {cout << x;return 0;}
#define fi              first
#define se              second
#define pb              push_back
#define all(x)          (x).begin(),(x).end()
#define mp(X,Y)         make_pair(X,Y)
#define foreach(i, c)   for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c, x)   ((c).find(x) != (c).end())
#define two(x)          (1 << (x))
#define two64(x)        (((int64)(1)) << (x))
#define contain(s, x)   (((s) & two(x)) != 0)
#define contain64(s,x)  (((s) & two64(x)) != 0)

// -------------------- Cac ham ve chuyen doi giua cac kieu --------------------
bool isUpperCase(char c){return c>='A'&&c<='Z';}
bool isLowerCase(char c){return c>='a'&&c<='z';}
bool isLetter(char c){return c>='A'&&c<='Z'|c>='a'&&c<='z';}
bool isDigit(char c){return c>='0'&&c<='9';}
char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}
char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}
template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}
int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}
int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}
double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}
template<class T> void stoa(string s,int &n,T A[]){n=0;istringstream sin(s);for(T v;sin>>v;A[n++]=v);}
template<class T> void atos(int n,T A[],string &s){ostringstream sout;for(int i=0;i<n;i++){if(i>0)sout<<' ';sout<<A[i];}s=sout.str();}
template<class T> void atov(int n,T A[],vector<T> &vi){vi.clear();for(int i=0;i<n;i++)vi.push_back(A[i]);}
template<class T> void vtoa(vector<T> vi,int &n,T A[]){n=vi.size();for(int i=0;i<n;i++)A[i]=vi[i];}
template<class T> void stov(string s,vector<T> &vi){vi.clear();istringstream sin(s);for(T v;sin>>v;vi.push_back(v));}
template<class T> void vtos(vector<T> vi,string &s){ostringstream sout;for(int i=0;i<vi.size();i++){if(i>0)sout<<' ';sout<<vi[i];}s=sout.str();}
// =========================== Ket thuc phan Header ===========================

string formatValue(string s) {
    while (s[0] == ' ')
        s.erase(0, 1);
    while (s[s.size() - 1] == ' ')
        s.erase(s.size() - 1, 1);
    while (s[0] == ',')
        s.erase(0, 1);
    while (s[s.size() - 1] == ',')
        s.erase(s.size() - 1, 1);
    return s;
}

string formatArray(string s) {
    while (s[0] == ' ')
        s.erase(0, 1);
    while (s[s.size() - 1] == ' ')
        s.erase(s.size() - 1, 1);
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '{')
            s[i] = '(';
        if (s[i] == '}')
            s[i] = ')';
    }
    if ((int)s.find(',') < 0) {
        s.erase(s.size() - 1, 1);
        s += ",)";
    }
    return s;
}

int main() {
    freopen ("input.txt", "r", stdin);
    //Header template
    string className, funcName;
    int pCount;
    cin >> className >> funcName >> pCount;
    string fileName = "C:\\Users\\trunghieu11\\Documents\\PythonAlgorithm\\Contest\\Topcoder\\current\\" + className + ".py";

    freopen (fileName.c_str(), "w", stdout);

    cout << "class " << className << ":" << endl;
    cout << "    def " << funcName << "(self";
    for (int i = 0; i < pCount; i++) {
        cout << ", val" << i;
    }
    cout << "):" << endl;
    cout << "        return 0\n\n\n";


    cout << "##########################" << endl;
    cout << "#        BEGIN TEST      #" << endl;
    cout << "##########################" << endl;

    cout << "import sys\n";
    cout << "import time\n";
    //cout << "def RunTest(testNum, p0, p1, p2, p3, hasAnswer, p4):\n";
    cout << "def RunTest(testNum, ";
    for (int i = 0; i < pCount; i++) {
        cout << "p" << i << ", ";
    }
    cout << "hasAnswer, p" << pCount << "):\n";
    cout << "    obj = " << className << "()\n";
    cout << "    startTime = time.clock()\n";
    cout << "    answer = obj." << funcName << "(";
    //p0, p1, p2, p3
    for (int i = 0; i < pCount; i++) {
        if (i)
            cout << ", ";
        cout << "p" << i;
    }
    cout << ")\n";
    cout << "    endTime = time.clock()\n";
    cout << "    testTime.append(endTime - startTime)\n";
    cout << "    res = True\n";
    cout << "    if hasAnswer:\n";
    cout << "        res = compare_answer(answer, p" << pCount << ")\n";
    cout << "    if res:\n";
    cout << "        print(str(\"Test #\") + str(testNum) + \": Passed\")\n";
    cout << "        return res\n";
    cout << "    print(str(\"Test #\") + str(testNum) + str(\":\"))\n";
    cout << "    print((\"[\") + ";
    for (int i = 0; i < pCount; i++) {
        if (i)
            cout << " + str(\",\") + ";
        cout << "str(p" << i << ")";
    }
    cout << " + str(\"]\"))\n";
    cout << "    if (hasAnswer):\n";
    cout << "        print(str(\"Expected:\"))\n";
    cout << "        print(str(p" << pCount << "))\n\n";
    cout << "    print(str(\"Received:\"))\n";
    cout << "    print(str(answer))\n";
    cout << "    print(str(\"Verdict:\"))\n";
    cout << "    if (not res):\n";
    cout << "        print((\"Wrong answer!!\"))\n";
    cout << "    elif ((endTime - startTime) >= 20):\n";
    cout << "        print(str(\"FAIL the timeout\"))\n";
    cout << "        res = False\n";
    cout << "    elif (hasAnswer):\n";
    cout << "        print(str(\"OK!!\"))\n";
    cout << "    else:\n";
    cout << "        print(str(\"OK, but is it right?\"))\n";
    cout << "    print(\"Time: %.11f seconds\" % (endTime - startTime))\n";
    cout << "    print(str(\"-----------------------------------------------------------\"))\n";
    cout << "    return res\n";
    cout << "\n";

    count << "def compare_answer(my_answer, correct_answer):\n";
    count << "    if isinstance(my_answer, float) and isinstance(correct_answer, float):\n";
    count << "        return round(my_answer, 6) == round(correct_answer, 6)\n";
    count << "    return my_answer == correct_answer\n";

    cout << "all_right = True\n";
    cout << "tests_disabled = False\n";
    cout << "testTime = []\n";

    //Item template
    int testCount = 0;
    string s;
    while (getline(cin, s)) {
        if (s.size() == 0)
            continue;
        vs splitted;
        stov(s, splitted);
        int sz = splitted.size();
        int isArray = 0;
        int paraCount = 0;
        string curArray = "";

        cout << "# ----- test " << testCount << " -----\n";
        cout << "disabled = False\n";
        for (int i = 0; i < sz - 1; i++) {
            if ((int)splitted[i].find('{') >= 0) {
                isArray++;
                curArray = "";
            }
            if (isArray > 0) {
                curArray += splitted[i] + " ";
                if ((int)splitted[i].find('}') >= 0) {
                    isArray = 0;
                    cout << "p" << paraCount << " = " << formatArray(formatValue(curArray)) << endl;
                    paraCount++;
                }
                continue;
            }
            cout << "p" << paraCount << " = " << formatValue(splitted[i]) << endl;
            paraCount++;
        }
        cout << "all_right = (disabled or RunTest(";
        cout << testCount << ", ";
        for (int i = 0; i < paraCount - 1; i++)
            cout << "p" << i << ", ";
        cout << "True, p" << paraCount - 1;
        cout << ") ) and all_right" << endl;
        cout << "tests_disabled = tests_disabled or disabled\n";
        cout << "# ------------------\n\n";
        testCount++;
    }

    //Footer Template
    cout << "print(\"===========================================================\")\n";
    cout << "if all_right:\n";
    cout << "    if tests_disabled:\n";
    cout << "        print(str(\"All test Passed!! (but some test cases were disabled)!\"))\n";
    cout << "    else:\n";
    cout << "        print(str(\"All test Passed!!\"))\n";
    cout << "else:\n";
    cout << "    print(str(\"Some of the test cases had errors.\"))\n";
    cout << "print(\"Run time: %.11f seconds\" % max(testTime))\n";
}

/*
# ----- test 1 -----
disabled = False
p0 = "RRRRR"
p1 = 3
p2 = 4
p3 = 4
all_right = (disabled or KawigiEdit_RunTest(1, p0, p1, p2, True, p3) ) and all_right
tests_disabled = tests_disabled or disabled
# ------------------
*/
