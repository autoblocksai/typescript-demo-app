import { run } from '../src/app';
import { AutoblocksAppClient } from '@autoblocks/client';
import { getSelectedDatasets } from '@autoblocks/client';
import { TestCase } from '../src/models';

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

  for (const testCase of testCases) {
    const result = await run(testCase.question);
    console.log(result);
  }
}

runTests();
