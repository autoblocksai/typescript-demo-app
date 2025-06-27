import { run } from '../src/app';
import { AutoblocksAppClient, getSelectedDatasets } from '@autoblocks/client';
import { runTestSuite } from '@autoblocks/client/testing/v2';
import { TestCase, Output } from '../src/models';
import { AnswerAccuracy, HasExpectedContent } from './evaluators';

const client = new AutoblocksAppClient({
  appSlug: 'doctor-gpt',
});

async function runTests() {
  const selectedDatasetsFromEnv = getSelectedDatasets();
  const selectedDatasets: string[] = [];
  if (selectedDatasetsFromEnv.length === 0) {
    selectedDatasets.push('test-cases');
  } else {
    selectedDatasets.push(...selectedDatasetsFromEnv);
  }

  const testCases: TestCase[] = [];
  for (const dataset of selectedDatasets) {
    const datasetItems = await client.datasets.getItems({
      externalId: dataset,
    });
    for (const item of datasetItems) {
      testCases.push({
        question: item.data['Question'] as string,
        expectedRouterOutput: item.data['Expected Router Output'] as string,
        expectedAnswer: item.data['Expected Answer'] as string,
      });
    }
  }

  runTestSuite<TestCase, Output>({
    id: 'doctor-gpt-test-suite',
    appSlug: 'doctor-gpt',
    testCases,
    testCaseHash: ['question'],
    fn: ({ testCase }) => run(testCase.question),
    evaluators: [new HasExpectedContent(), new AnswerAccuracy()],
  });
}

runTests();
