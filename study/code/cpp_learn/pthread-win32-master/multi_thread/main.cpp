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

// 生产者消费者
typedef struct
{
	int * buf;
	int n;
	int front;
	int end;

	sem_t mutex;	//互斥锁
	sem_t items;	//item是否存在
	sem_t slots;	//位置

}sbuf_t;

void sbuf_init(sbuf_t *sp,int n)
{

}

void sbuf_insert(sbuf_t *sp, int )
{}

// ------------------------------------------------------------------------------ 读写锁 ------------------------------------------------------------------------------

namespace Sem_and_Mutex
{
	// 一个信号量和一把锁
	// 关键是写的时候要判断当前的读者状态以及写者状态

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