import { BaseTestEvaluator, Evaluation } from '@autoblocks/client/testing';
import { TestCase, Output } from '../src/models';
import OpenAI from 'openai';

// Initialize OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

/**
 * LLM-based evaluator that uses GPT tool calling to assess if the output answer contains expected content
 */
class HasExpectedContent extends BaseTestEvaluator<TestCase, Output> {
  id = 'has-expected-content';

  async evaluateTestCase(args: {
    testCase: TestCase;
    output: Output;
  }): Promise<Evaluation> {
    const { testCase, output } = args;

    const evaluationPrompt = `You are an expert medical evaluator. Your task is to determine if the given answer contains the expected content or covers the key information.

Question: "${testCase.question}"
Expected Answer: "${testCase.expectedAnswer}"
Actual Answer: "${output.answer}"

Does the actual answer contain the expected content or adequately address the same medical concepts? Consider:
- Semantic similarity (same meaning with different wording)
- Coverage of key medical concepts
- Clinical accuracy and relevance`;

    try {
      const response = await openai.chat.completions.create({
        model: 'gpt-4o',
        temperature: 0.1,
        messages: [
          {
            role: 'user',
            content: evaluationPrompt,
          },
        ],
        tools: [
          {
            type: 'function',
            function: {
              name: 'evaluate_content_match',
              description:
                'Evaluate if the actual answer contains the expected content',
              parameters: {
                type: 'object',
                properties: {
                  score: {
                    type: 'integer',
                    enum: [0, 1],
                    description:
                      "1 if the answer contains expected content, 0 if it doesn't",
                  },
                  reasoning: {
                    type: 'string',
                    description: 'Brief explanation of your evaluation',
                  },
                  confidence: {
                    type: 'number',
                    minimum: 0.0,
                    maximum: 1.0,
                    description: 'Your confidence level (0.0 to 1.0)',
                  },
                },
                required: ['score', 'reasoning', 'confidence'],
              },
            },
          },
        ],
        tool_choice: {
          type: 'function',
          function: { name: 'evaluate_content_match' },
        },
      });

      const toolCall = response.choices[0]?.message?.tool_calls?.[0];
      if (!toolCall || toolCall.type !== 'function') {
        throw new Error('No valid tool call in response');
      }

      const evaluation = JSON.parse(toolCall.function.arguments);

      return {
        score: evaluation.score,
        threshold: { gte: 1 },
        metadata: {
          expectedAnswer: testCase.expectedAnswer,
          actualAnswer: output.answer,
          reason: evaluation.reasoning,
          confidence: evaluation.confidence,
          toolCall: toolCall.function.arguments,
        },
      };
    } catch (error) {
      console.error('Error in LLM evaluation:', error);
      // Fallback to simple string matching if LLM fails
      const containsExpected = output.answer
        .toLowerCase()
        .includes(testCase.expectedAnswer.toLowerCase());

      return {
        score: containsExpected ? 1 : 0,
        threshold: { gte: 1 },
        metadata: {
          expectedAnswer: testCase.expectedAnswer,
          actualAnswer: output.answer,
          reason: 'LLM evaluation failed, used string matching fallback',
          confidence: 0.5,
          error: error instanceof Error ? error.message : 'Unknown error',
        },
      };
    }
  }
}

/**
 * LLM-based evaluator that uses GPT tool calling to assess answer quality and accuracy
 */
class AnswerAccuracy extends BaseTestEvaluator<TestCase, Output> {
  id = 'answer-accuracy';

  async evaluateTestCase(args: {
    testCase: TestCase;
    output: Output;
  }): Promise<Evaluation> {
    const { testCase, output } = args;

    const evaluationPrompt = `You are an expert medical evaluator. Your task is to assess the accuracy and quality of a medical answer.

Question: "${testCase.question}"
Expected Answer: "${testCase.expectedAnswer}"
Actual Answer: "${output.answer}"

Evaluate the actual answer based on:
1. Medical accuracy and correctness
2. Completeness compared to expected answer
3. Clinical relevance and appropriateness
4. Safety considerations (appropriate caveats, referrals to guidelines)

Provide a score from 0.0 to 1.0 where:
- 1.0 = Excellent answer that matches or exceeds expected quality
- 0.8-0.9 = Good answer with minor gaps or slight differences
- 0.6-0.7 = Adequate answer but missing some important aspects
- 0.4-0.5 = Poor answer with significant issues
- 0.0-0.3 = Incorrect or dangerous answer`;

    try {
      const response = await openai.chat.completions.create({
        model: 'gpt-4o',
        temperature: 0.1,
        messages: [
          {
            role: 'user',
            content: evaluationPrompt,
          },
        ],
        tools: [
          {
            type: 'function',
            function: {
              name: 'evaluate_answer_accuracy',
              description:
                'Evaluate the accuracy and quality of a medical answer',
              parameters: {
                type: 'object',
                properties: {
                  score: {
                    type: 'number',
                    minimum: 0.0,
                    maximum: 1.0,
                    description: 'Numerical score from 0.0 to 1.0',
                  },
                  reasoning: {
                    type: 'string',
                    description: 'Detailed explanation of your evaluation',
                  },
                  confidence: {
                    type: 'number',
                    minimum: 0.0,
                    maximum: 1.0,
                    description: 'Your confidence level (0.0 to 1.0)',
                  },
                  medical_accuracy: {
                    type: 'string',
                    description: 'Assessment of medical accuracy',
                  },
                  completeness: {
                    type: 'string',
                    description:
                      'Assessment of completeness compared to expected answer',
                  },
                  safety_considerations: {
                    type: 'string',
                    description:
                      'Assessment of safety considerations and appropriate caveats',
                  },
                },
                required: [
                  'score',
                  'reasoning',
                  'confidence',
                  'medical_accuracy',
                  'completeness',
                  'safety_considerations',
                ],
              },
            },
          },
        ],
        tool_choice: {
          type: 'function',
          function: { name: 'evaluate_answer_accuracy' },
        },
      });

      const toolCall = response.choices[0]?.message?.tool_calls?.[0];
      if (!toolCall || toolCall.type !== 'function') {
        throw new Error('No valid tool call in response');
      }

      const evaluation = JSON.parse(toolCall.function.arguments);

      return {
        score: evaluation.score,
        threshold: { gte: 0.7 }, // Set threshold at 70% for passing
        metadata: {
          expectedAnswer: testCase.expectedAnswer,
          actualAnswer: output.answer,
          reason: evaluation.reasoning,
          confidence: evaluation.confidence,
          medicalAccuracy: evaluation.medical_accuracy,
          completeness: evaluation.completeness,
          safetyConsiderations: evaluation.safety_considerations,
          toolCall: toolCall.function.arguments,
        },
      };
    } catch (error) {
      console.error('Error in LLM evaluation:', error);
      // Fallback to simple exact match if LLM fails
      const normalizedExpected = testCase.expectedAnswer.trim().toLowerCase();
      const normalizedActual = output.answer.trim().toLowerCase();
      const isExactMatch = normalizedExpected === normalizedActual;

      return {
        score: isExactMatch ? 1 : 0,
        threshold: { gte: 1 },
        metadata: {
          expectedAnswer: testCase.expectedAnswer,
          actualAnswer: output.answer,
          reason: 'LLM evaluation failed, used exact match fallback',
          confidence: 0.5,
          error: error instanceof Error ? error.message : 'Unknown error',
        },
      };
    }
  }
}

export { HasExpectedContent, AnswerAccuracy };
