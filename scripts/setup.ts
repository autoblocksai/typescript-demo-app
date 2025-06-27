#!/usr/bin/env tsx

import { create as createPrompts } from './create-prompts';
import { create as createDataset } from './create-dataset';

// Configure logging
const logger = {
  info: (message: string) => console.log(`${new Date().toISOString()} - INFO - ${message}`),
  error: (message: string) => console.error(`${new Date().toISOString()} - ERROR - ${message}`)
};

async function setup(): Promise<void> {
  try {
    logger.info('Starting setup process...');
    
    logger.info('Creating prompts...');
    await createPrompts();
    logger.info('Prompts created successfully');
    
    logger.info('Creating dataset...');
    await createDataset();
    logger.info('Dataset created successfully');
    
    logger.info('Setup completed successfully!');
  } catch (error) {
    logger.error(`Setup failed: ${error}`);
    process.exit(1);
  }
}

// Run the script if called directly
if (require.main === module) {
  setup();
}

export { setup }; 