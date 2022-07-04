//C++ Program to implement Floyd Warshall Algorithm 

#include <iostream.h>

using namespace std;

void floyds(int c[][7])
{
    int i, j, m;
    for (m = 0; m < 7; m++)
    {
        for (i = 0; i < 7; i++)
        {
            for (j = 0; j < 7; j++)
            {
                if ((c[i][m] * c[m][j] != 0) && (i != j))
                {
                    if ((c[i][m] + c[m][j] < c[i][j]) || (c[i][j] == 0))
                    {
                        c[i][j] = c[i][m] + c[m][j];
                    }
                }
            }
        }
    }
    for (i = 0; i < 7; i++)
    {
        cout<<"nMinimum Cost With Respect to Node:"<<i<<endl;
        for (j = 0; j < 7; j++)
        {
            cout<<c[i][j]<<"t";
        }
    }
}
int main()
{
        int c[7][7];
        cout<<"ENTER VALUES OF ADJACENCY MATRIXnn";
        for (int i = 0; i < 7; i++)
        {
                cout<<"enter values for "<<(i+1)<<" row"<<endl;
                for (int j = 0; j < 7; j++)
                cin>>c[i][j];
        }
        floyds(c);
        return 0;
}











