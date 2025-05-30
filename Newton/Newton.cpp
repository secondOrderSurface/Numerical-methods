#include <iostream>
#include <fstream>
using namespace std;
void FillMassive(float[], int); // Заполняет массив размера n 
void ShowMassive(float[], int); // Выводит массив размера n 
float* arange(float, float, float); // Аналог np.arange из Python: массив чисел от [start, stop) с шагом step
float Newton(float[], float[], int, float); // Интерполяция полиномом Ньютона



int main()
{
	bool run = 1;
	while (run)
	{
		int n;
		cout << "Number of points: ";
		cin >> n;

		float* x = new float[n];
		float* f = new float[n];

		cout << "Print x :" << "\n";
		FillMassive(x, n);

		cout << "Print f(x) :" << "\n";
		FillMassive(f, n);


		float* borders = new float[3];
		cout << "Print start, stop, step : \n";
		FillMassive(borders, 3);

		// Пределы для графика
		float* xRange = arange(borders[0], borders[1], borders[2]);
		int points = ceil((borders[1] - borders[0]) / borders[2]);

		float* yRange = new float[points];

		for (int i = 0; i < points; i++)
		{
			yRange[i] = Newton(x, f, n, xRange[i]);
		}

		// Выводим данные в файл
		ofstream out;
		out.open("Newton.txt");
		if (out.is_open())
		{
			for (int i = 0; i < points; i++)
			{
				out << xRange[i] << " ";
			}

			out << "\n";

			for (int i = 0; i < points; i++)
			{
				out << yRange[i] << " ";
			}
		}
		out.close();

		// Запуск скрипта python для графиков
		system("Newton.py");

		cout << "Again ? (1, 0)" << "\n";
		cin >> run;
	}
}

void FillMassive(float mas[], int n)
{
	for (int i = 0; i < n; i++)
	{
		cin >> mas[i];
	}
}

void ShowMassive(float mas[], int n)
{
	for (int i = 0; i < n; i++)
	{
		cout << mas[i] << " ";
	}
}

float* arange(float start, float stop, float step)
{
	int n = ceil((stop - start) / step);
	float* mas = new float[n];
	for (int i = 0; i < n; i++)
	{
		mas[i] = start + i * step;
	}

	return mas;
}

float Newton(float x[], float f[], int n, float point)
{	
	float p = f[0];
	float* a = new float[n];
	a[0] = f[0];

	// Вычисление коэфицентов a_k
	for (int k = 1; k < n; k++)
	{
		float NewtonPol = 1;
		float sum = 0;
		for (int i = 0; i < k; i++)
		{			
			sum += a[i] * NewtonPol;
			NewtonPol *= (x[k] - x[i]);
		}

		a[k] = (f[k] - sum) / NewtonPol;

	}

	float NewtonPol = 1;
	for (int k = 1; k < n; k++)
	{
		NewtonPol *= (point - x[k-1]);
		p += a[k] * NewtonPol;
	}

	return p;

}

