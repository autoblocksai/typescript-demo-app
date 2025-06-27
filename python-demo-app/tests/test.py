from dataclasses import dataclass
import logging
from autoblocks.api.app_client import AutoblocksAppClient
from autoblocks.datasets.utils import get_selected_datasets
from autoblocks.testing.models import BaseTestCase
from autoblocks.testing.util import md5
from autoblocks.testing.v2.run import run_test_suite
from dotenv import load_dotenv

from python_demo_app.app import run
from python_demo_app.models import Output
from autoblocks.testing.models import CreateHumanReviewJob

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

client = AutoblocksAppClient(
    app_slug="doctor-gpt",
)


@dataclass
class TestCase(BaseTestCase):
    question: str
    expected_router_output: str
    expected_answer: str

    def hash(self) -> str:
        return md5(self.question)


def run_tests():
    test_cases: list[TestCase] = []
    # Get all selected
    selected_datasets = get_selected_datasets()
    if len(selected_datasets) == 0:
        selected_datasets = ["test-cases"]

    for dataset in selected_datasets:
        dataset_items = client.datasets.get_items(external_id=dataset)
        test_cases.extend(
            [
                TestCase(
                    question=item.data["Question"],
                    expected_router_output=item.data["Expected Router Output"],
                    expected_answer=item.data["Expected Answer"],
                )
                for item in dataset_items
            ]
        )

    async def test_fn(test_case: TestCase) -> Output:
        return await run(test_case.question)

    run_test_suite(id="doctor-gpt",
                    app_slug="doctor-gpt",
                    test_cases=test_cases,
                    fn=test_fn,
                    evaluators=[],
                    human_review_job=CreateHumanReviewJob(
                        name="Review for accuracy",
                        assignee_email_address=["adam@autoblocks.ai", "haroon@autoblocks.ai"],
                        # rubric_id="tewic742it2p62847lfan3ii"
                    )
    )
