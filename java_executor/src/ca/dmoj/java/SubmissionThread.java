package ca.dmoj.java;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;

public class SubmissionThread extends Thread {
    private final Class submission;
    private boolean tle = false;
    private boolean mle = false;
    private int error = 0;
    private Throwable exception;

    public SubmissionThread(Class process) {
        super(null, null, "Submission-Grading-Thread(" + process.getSimpleName() + ")", 8000000 /* Some pretty large stack size */);
        this.submission = process;
    }

    @Override
    @SuppressWarnings("unchecked")
    public void run() {
        Method handle;
        try {
            handle = submission.getMethod("main", String[].class);
            if (!Modifier.isStatic(handle.getModifiers())) System.exit(JavaSafeExecutor.NO_ENTRY_POINT_ERROR_CODE);
            try {
                handle.invoke(null, new Object[]{new String[0]});
            } catch (InvocationTargetException e) {
                // All program errors will be wrapped in an InvocationTargetException
                Throwable ex = e.getCause();
                if (ex == JavaSafeExecutor.TLE) {
                    // We've caught the ThreadDeath we threw to kill the submission thread in case of TLE.
                    tle = true;
                    return;
                } else if (ex instanceof OutOfMemoryError) {
                    // TODO: prevent `throw new OutOfMemoryError()` as being counted as MLE
                    mle = true;
                    return;
                } else {
                    ex.printStackTrace();
                    exception = e.getCause();
                    error = JavaSafeExecutor.PROGRAM_ERROR_CODE;
                }
            } catch (IllegalAccessException e) {
                e.printStackTrace();
                error = JavaSafeExecutor.ACCESS_ERROR_CODE;
            } catch (Throwable throwable) {
                throwable.printStackTrace();
                exception = throwable.getCause();
                error = JavaSafeExecutor.PROGRAM_ERROR_CODE;
            }
        } catch (NoSuchMethodException e) {
            e.printStackTrace();
            error = JavaSafeExecutor.NO_ENTRY_POINT_ERROR_CODE;
        }
        JavaSafeExecutor._safeBlock = true;
        JavaSafeExecutor.shockerThread.stop();
    }

    public Class getSubmission() {
        return submission;
    }

    public boolean isTle() {
        return tle;
    }

    public boolean isMle() {
        return mle;
    }

    public int getError() {
        return error;
    }

    public Throwable getException() {
        return exception;
    }
}