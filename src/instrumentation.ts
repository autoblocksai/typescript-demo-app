import { initAutoTracer } from '@autoblocks/client';
import { OpenAIInstrumentation } from '@traceloop/instrumentation-openai';

initAutoTracer({
  instrumentations: [new OpenAIInstrumentation()],
  isBatchDisabled: true,
});
