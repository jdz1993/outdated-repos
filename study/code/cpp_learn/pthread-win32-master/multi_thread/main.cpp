//
#ifdef __cplusplus 
extern "C" {
#endif

#include "..\pthread.h"
#include "..\semaphore.h"
#include "..\sched.h"

#ifdef __cplusplus
}
#endif

// ������������
typedef struct
{
	int * buf;
	int n;
	int front;
	int end;

	sem_t mutex;	//������
	sem_t items;	//item�Ƿ����
	sem_t slots;	//λ��

}sbuf_t;

void sbuf_init(sbuf_t *sp,int n)
{

}

void sbuf_insert(sbuf_t *sp, int )
{}

// ------------------------------------------------------------------------------ ��д�� ------------------------------------------------------------------------------

namespace Sem_and_Mutex
{
	// һ���ź�����һ����
	// �ؼ���д��ʱ��Ҫ�жϵ�ǰ�Ķ���״̬�Լ�д��״̬

	// Nothing just for example
	void ReadWork() {}
	void WriteWork() {}

	pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
	pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
	int w = 0;
	int r = 0;

	void DoRead()
	{

	}

	void DoWrite()
	{
		pthread_mutex_lock(&mutex);

		while (w != 0 || r > 0)
		{
			pthread_cond_wait(&cond, &mutex);
		}
		w = 1;

		pthread_mutex_unlock(&mutex);

		WriteWork();

		pthread_mutex_lock(&mutex);
		w = 0;
		pthread_cond_broadcast(&cond);
		pthread_mutex_unlock(&mutex);
	}
}

int main()
{

}