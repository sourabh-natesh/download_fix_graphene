#include "pal.h"
#include "pal_debug.h"

static PAL_HANDLE event1;

int count = 0;

static int thread_func(void* args) {
    DkThreadDelayExecution(1000);

    pal_printf("In thread 1\n");

    while (count < 100)
        count++;

    DkEventSet(event1);
    DkThreadExit(/*clear_child_tid=*/NULL);
    /* UNREACHABLE */
}

int main(int argc, char** argv) {
    pal_printf("Enter main thread\n");

    int ret = DkNotificationEventCreate(0, &event1);
    if (ret < 0 || !event1) {
        pal_printf("DkNotificationEventCreate failed\n");
        return -1;
    }

    PAL_HANDLE thd1;
    ret = DkThreadCreate(&thread_func, 0, &thd1);
    if (ret < 0) {
        pal_printf("DkThreadCreate failed\n");
        return -1;
    }

    /* wait till thread thd1 is done */
    DkSynchronizationObjectWait(event1, NO_TIMEOUT);

    if (count != 100)
        return -1;

    /* this wait should return immediately */
    DkSynchronizationObjectWait(event1, NO_TIMEOUT);

    pal_printf("Success, leave main thread\n");
    return 0;
}
