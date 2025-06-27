export interface Output {
  answer: string;
}

export interface TestCase {
  question: string;
  expectedRouterOutput: string;
  expectedAnswer: string;
}

export type DoctorIntent = 
  | "clinical" 
  | "soap" 
  | "history" 
  | "summary";

export interface OpenAIMessage {
  role: "system" | "user" | "assistant";
  content: string;
}

export interface OpenAIParams {
  model: string;
  temperature?: number;
  messages: OpenAIMessage[];
} 